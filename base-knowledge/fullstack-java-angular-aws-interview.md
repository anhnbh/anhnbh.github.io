# Full-Stack Interview Base Knowledge — Java · Spring · AWS · Angular

> Consolidated from senior full-stack interview prep (Savycom R1, 2026-10). Topics: Kafka, Elasticsearch, Spring Batch, `@Transactional`, REST exception handling, Spring Cloud, AWS, and Angular (data binding, Observables/RxJS, interceptors, authorization).
>
> **Strategy:** Every topic lives in one reference project — a **mobile-banking orchestration platform** (Java 17/Spring Boot microservices, Kafka event backbone, Angular 15+ portal, on AWS EKS). Lead every answer with that project.
>
> **Numbers to quote:** 40% avg API response time reduction (query optimization + Redis caching), ~40% portal initial-load reduction (bundle budgets, lazy routes), 75%+ test coverage, Kafka as event backbone across services.

---

## 0. The 30-second pitch (memorize)

"I've spent the last 4+ years as senior fullstack on a mobile-banking orchestration platform: Java 17/Spring Boot microservices on Spring Cloud, Kafka as the event backbone, Spring Batch for reconciliation and compliance jobs, Elasticsearch for centralized logging and transaction search, running on AWS (EKS, MSK, RDS). On the frontend I own the Angular 15+ portal — admin dashboards and partner consoles — with reactive forms, RxJS, NgRx, and interceptors for JWT/RBAC. I'm strongest where backend Java meets real integration work: exactly-once processing, transactional boundaries, and API design."

---

# BACKEND (main focus)

## 1. Apache Kafka

**Where in the story:** event backbone of the orchestration platform — payment orchestration events, notification dispatch (email/SMS), audit trail. Multiple consumer services read the same events.

### Core answers
- **Why Kafka over RabbitMQ:** pull-based log with retention → consumers can replay history (audit/recovery), much higher throughput, multiple independent consumer groups on the same topic. RabbitMQ = per-message routing/ack queues; Kafka = distributed append-only log.
- **Delivery semantics:** default is **at-least-once**. We make processing **effectively-once** by: (1) idempotent producer (`enable.idempotence=true`, `acks=all`, `min.insync.replicas=2`), (2) **idempotent consumers** — dedupe by `event_id` in Redis/DB table.
- **Ordering:** guaranteed only **within a partition**. We key messages by `transactionId`/`accountId`, so all events for one entity are ordered; global ordering isn't needed.
- **Error handling (they WILL ask):** Spring Kafka `@RetryableTopic` — non-blocking retries with exponential backoff on retry topics → after N attempts, publish to **DLT (dead-letter topic)**; alerting to Grafana, ops dashboard for DLT triage.
- **Offset management:** manual ack after successful processing; commit = checkpoint. Poison pill → seek past + record, never block the partition.
- **Rebalance:** consumer group rebalances when a member dies; tune `max.poll.interval.ms` so slow batches don't trigger rebalance storms, cooperative-sticky assignor for smoother handover.

### Senior kill-shot: **Transactional Outbox pattern**
Problem: dual-write — if you commit DB tx then publish to Kafka and the publish fails (or vice versa), you lose consistency.
Solution: write the event to an `outbox` table **inside the same DB transaction** as the business change; a relay (or Debezium CDC) publishes it to Kafka. Kafka publish is never inside the DB transaction.
→ Say this when they ask "how do you keep DB and Kafka consistent?"

### Trap questions
- "Is Kafka exactly-once?" → Transactional producer gives EOS for **Kafka→Kafka** consume-transform-produce flows; for side-effectful consumers you still dedupe (at-least-once + idempotency).
- "Consumer lag spikes at peak — what do you do?" → increase partitions + listener `concurrency`, batch listens, monitor lag with exporter → Grafana alert.

---

## 2. Elasticsearch

**Where in the story:** centralized logging for all microservices (with Grafana dashboards on top), plus transaction search module.

### Core answers
- **Why not SQL `LIKE '%x%'`:** leading wildcard = full table scan, no index. ES uses an **inverted index** (token → list of documents) built at index time → fast full-text + filters.
- **Our pipeline:** services log structured JSON with `trace_id` → Filebeat → Logstash (parse/enrich) → ES → Grafana/Kibana. Trace ID correlates one user request across gateway → services → Kafka consumers.
- **NRT:** searchable after ~1s refresh interval; durability comes from translog + flush, not refresh.
- **Cluster basics:** data nodes hold shards; each index = primary shards + replicas (replica = HA + read throughput); explicit **mapping** (never rely on dynamic mapping in prod — a wrong `text` vs `keyword` mapping ruins aggregation); `keyword` for exact/filter/aggregation, `text` for full-text with analyzer.
- **Ops we did:** ILM policy — rollover daily alias, delete after 30 days (logs are huge); shard sizing ~30–50GB max; yellow cluster status = replicas unassigned.
- **Zero-downtime mapping change:** reindex into new index behind an **alias**, swap alias when done.

### Trap questions
- "Is ES a primary datastore?" → No: no joins/ACID across docs, eventual consistency — keep PostgreSQL as source of truth, ES is a search/projection.
- "Filter vs query context?" → filter context is non-scoring and **cacheable** — put exact conditions (status, date range) in `filter`, only relevance terms in `must`.

---

## 3. Spring Batch

**Where in the story:** nightly reconciliation (bank statements vs internal ledger), monthly compliance reports, partner data sync, backup validation — millions of records.

### Core answers
- **Chunk-oriented model:** read items → process → write per chunk; **each chunk = its own transaction** (commit-interval). ItemReader → ItemProcessor → ItemWriter.
- **Metadata tables:** JobRepository persists JOB_INSTANCE / JOB_EXECUTION / STEP_EXECUTION in the DB → **restartable**: a failed job restarts from where it stopped (ExecutionContext checkpoints), and a completed instance with same params won't rerun (idempotent scheduling).
- **Fault tolerance:** `skip` (SkipPolicy + skip-limit; bad rows → SkipListener logs them to a dead-letter table for review) and `retry` (retry-limit, e.g. transient partner API errors) — configured per step: `faultTolerant().skip(FlatFileParseException.class).skipLimit(100).retry(DeadlockLoserDataAccessException.class).retryLimit(3)`.
- **Scaling:** multi-threaded step (simple), **partitioning** (manager splits by date-range into worker steps — the default for reconciliation), remote partitioning via Kafka for really big loads.
- **Tuning:** chunk size 500–1000, page size on readers, avoid loading all in memory; listeners (JobExecutionListener, StepExecutionListener) push duration/skip-count metrics to Grafana.
- **Scheduling:** Spring `@Scheduled` / Quartz, plus a distributed lock (ShedLock/DB lock) so only one node runs the job in a multi-pod deployment.

### Trap questions
- "Chunk transaction fails at item 990 — what happens?" → whole chunk rolls back; with skip configured, Spring re-reads the chunk item-by-item and skips only the offender (that's why skip + restart semantics matter).
- "JdbcCursorItemReader restartable?" → cursor readers are not transactional-restartable by themselves; use paging readers or the **process-indicator pattern** (mark rows processed) for restartability.

---

## 4. @Transactional in Spring

**Where in the story:** anywhere money moves — orchestration sagas, payment records, audit logs.

### Core answers
- **How it works:** Spring AOP wraps the bean in a **proxy**; the proxy begins/commits/rollbacks the tx around public method calls. JDK dynamic proxy (interface) or CGLIB (subclass).
- **Rollback rules (classic question):** default rolls back on **RuntimeException and Error only** — checked exceptions do NOT roll back unless `rollbackFor = Exception.class`. Always set it explicitly on money-path methods.
- **Propagation:**
  - `REQUIRED` (default) — join existing or create new.
  - `REQUIRES_NEW` — suspends outer tx, independent commit/rollback. Use case: **audit/security log of a failed attempt must persist even when the main payment tx rolls back.**
  - `NESTED` — savepoint within the same tx (JDBC only).
  - `MANDATORY / NEVER / SUPPORTS / NOT_SUPPORTED` — know names.
- **Isolation:** DB default (PostgreSQL = READ_COMMITTED, MySQL InnoDB = REPEATABLE_READ); phenomena: dirty read / non-repeatable read / phantom read. Concurrency in practice: **optimistic locking with `@Version`** for entity updates; pessimistic (`SELECT ... FOR UPDATE`) only for hot contention.
- **The two classic bugs:**
  1. **Self-invocation:** `this.method2()` inside the same bean bypasses the proxy → no new transaction. Fix: move to another bean (or self-injection).
  2. `@Transactional` on **private/final** methods doesn't work (proxy can't intercept/override).
- **Keep transactions short:** never call Kafka/HTTP/SMTP inside a DB transaction → connection-pool exhaustion under load + dual-write problem → **outbox pattern** (links to the Kafka answer).
- `readOnly = true` for report/query methods: Hibernate skips dirty-checking (flush MANUAL), driver hint to DB.

### Trap questions
- "Outer REQUIRED + inner REQUIRES_NEW; inner rolls back, what does outer see/do?" → inner committed-then-rolled-back independently; outer continues and can still commit — unless the inner exception propagates out and hits outer's rollback rule.
- "How do you test transactions?" → `@DataJpaTest` is transactional-rollback by default; for REQUIRES_NEW you must test with a real commit (Testcontainers) because the test tx hides it.

---

## 5. Exception handling in REST APIs

**Where in the story:** platform-wide error contract used by web + mobile + partner clients.

### Core answers
- **Central handler:** `@RestControllerAdvice` + `@ExceptionHandler(SomeException.class)` returning a consistent envelope. Local `@ExceptionHandler` on a controller only as rare exception.
- **Custom hierarchy:** base `ApiException(code, message)` → `NotFoundException` (404), `ValidationException` (400), `ConflictException` (409), `ExternalServiceException` (502), `AuthException` (401/403). `ErrorCode` enum = stable machine-readable code (`PAY-4021`) so clients can branch on it.
- **Validation:** `@Valid` + Bean Validation annotations on DTOs; catch `MethodArgumentNotValidException` globally → 400 with per-field `field, message` list.
- **Error body shape:** `timestamp, status, code, message, path, traceId` — traceId lets support jump straight to the logs in ELK. Never leak stack traces or SQL messages.
- **Modern note:** Spring 6 supports **RFC 7807 Problem Details** (`ProblemDetail`) — know it even if keeping a custom envelope for legacy clients.
- **Log once, in the advice** (warn for 4xx, error for 5xx) with MDC traceId — not scattered in every catch block.
- Same discipline beyond REST: Kafka listeners use a listener error handler → DLT; WebClient/RestClient `onStatus` maps partner errors to `ExternalServiceException`.

### Trap questions
- "Order of two @ControllerAdvice with overlapping handlers?" → `@Order` decides; more specific one should win.
- "How do you handle exceptions thrown in a filter (before controllers)?" → advice doesn't catch filter errors; use an error filter / extend OncePerRequestFilter handling, or map via ErrorController.

---

## 6. Spring Cloud

**Where in the story:** microservices layer — but be smart: on **Kubernetes**, tell the modern version of the story.

### Core answers (reference stack)
- **API Gateway — Spring Cloud Gateway:** single edge for all clients — routing, JWT validation at the edge, rate limiting (**Redis RequestRateLimiter** filter) per client/API-key, retry + timeout filters for resilience, CORS centralized.
- **Service discovery:** on K8s do **not run Eureka** — K8s Services + DNS is the registry (platform-native, one less stateful system; Eureka/Consul for VM/on-prem deployments).
- **Circuit breaking — Resilience4j** (Hystrix is dead): `CircuitBreaker` + `TimeLimiter` + `Retry` around partner/banking integrations with fallbacks (return last-known status / queue for retry). Sliding-window ratio opens the breaker; half-open probes recovery.
- **Config:** Spring Cloud Config Server for externalized config (on-prem variant); in K8s → ConfigMaps + Secrets. Modern Spring Cloud dropped `bootstrap.yml` → `spring.config.import`.
- **Load balancing:** Spring Cloud LoadBalancer (replaced Ribbon) for client-side balancing when calling non-K8s services.
- **Distributed tracing:** Micrometer Tracing (ex-Sleuth) + Zipkin/Tempo — `traceId` propagated gateway → service → **Kafka header** → consumer; ties into the ELK traceId story. Cross-Kafka propagation detail impresses.
- **OpenFeign:** declarative REST clients with custom ErrorDecoder mapping partner 4xx/5xx to domain exceptions — an option alongside WebClient/RestClient.

### Trap questions
- "Why circuit breaker at all if the LB retries?" → retry without a breaker amplifies an overloaded dependency (retry storm); breaker sheds load and fails fast — use both with backoff.
- "What breaks when the config server is down at startup?" → services fail fast unless config is cached / `fail-fast=false` + retry — shows production scars.

---

## 7. AWS

**Where in the story:** the whole platform runs there. Map services to platform components — that's how to prove it:

| Platform component | AWS service | Talking point |
|---|---|---|
| Microservices | **EKS** | Helm deployments, HPA autoscaling, pods across multi-AZ |
| Kafka | **MSK** | managed 3-broker multi-AZ cluster; tune partitions/retention, not zookeeping |
| PostgreSQL | **RDS multi-AZ** | sync standby + failover; read replica for reporting queries |
| Redis | **ElastiCache** | token blacklist, hot-data cache, rate-limit counters |
| Files/reports | **S3** | report archive + audit export, lifecycle → Glacier |
| Secrets | **Secrets Manager + KMS** | no credentials in images/env; rotation; encryption at rest |
| Observability | CloudWatch + Grafana | metrics/logs; ELK/ES for logs, CloudWatch for infra alarms |
| Network | VPC | private subnets for data tier, SGs per layer, NAT for egress |

### Core answers
- **IAM done right:** **IRSA** — EKS service accounts mapped to IAM roles; no static access keys in pods.
- **CI/CD on AWS:** GitHub Actions → build + SonarQube gate → push to **ECR** → Helm upgrade to EKS (canary for risky services).
- **HA story:** everything multi-AZ; RDS automated backups + PITR; DR = infra-as-code (Terraform) so region rebuild is scripted.
- **Cost awareness:** right-size from Grafana usage data, Savings Plans for steady baseline, S3 lifecycle policies — one sentence each is enough.
- **Security:** encryption in transit (TLS) + at rest (KMS: RDS/S3/MSK), security groups least-privilege, private-only data tier.

### Trap questions
- "Security group vs NACL?" → SG = stateful, instance/ENI level; NACL = stateless, subnet level (need both directions).
- "RDS multi-AZ vs read replica?" → multi-AZ = availability (synchronous standby, failover); read replica = scalability/read (async, can be promoted).
- "App is slow — how do you find the bottleneck on AWS?" → follow the chain: CloudWatch infra metrics → Grafana app metrics/traces → ELK logs by traceId → narrow to DB/GC/dependency; shows a method, not guesses.

---

# FRONTEND (Angular)

## 8. Data binding

- **Four forms** (one example each, fast):
  - Interpolation `{{ user.name }}` — display.
  - Property binding `[disabled]="isSaving"` — DOM property ← component.
  - Event binding `(click)="save()"` — component ← DOM.
  - Two-way `[(ngModel)]="form.name"` — both (needs `FormsModule`).
- **Component communication:** parent→child `@Input()`, child→parent `@Output() + EventEmitter`.
- **Change detection:** default checks everything; use **OnPush** + immutable updates + **`async` pipe** so Angular checks only on input reference change / event / observable emission — ties to the ~40% load/interaction improvements story.
- "What's new": on Angular 17+ move to **signals** (`signal()`, `computed()`) for fine-grained reactivity; signal = value + dependency tracking, no zone-based tree walk.

## 9. Observables / RxJS

- **What:** a lazy push-based stream of values over time; subscriber gets next/error/complete. `HttpClient` returns a **cold** observable — nothing happens until subscribe.
- **Unsubscribe discipline (always asked):** `async` pipe (auto-unsubscribes, works with OnPush) or `takeUntilDestroyed(this.destroyRef)`; leaking subscriptions = memory leaks and stale API calls.
- **Operators with real examples:**
  - `debounceTime(300)` + `distinctUntilChanged()` — transaction search box.
  - **`switchMap`** — typeahead/search: cancels the stale request when input changes. The trio: `switchMap` (cancel stale — searches), `concatMap` (order matters — sequential saves), `exhaustMap` (ignore while in-flight — login submits).
  - `forkJoin` — parallel dashboard API loads, render when all done; `combineLatest` — live filter + data streams.
  - `catchError` inside a stream → `throwError(() => new ApiError(...))` or `EMPTY` + user toast; retry API with `retry({ count: 2, delay: 500 })`.
  - `shareReplay(1)` — cache reference data (currencies, branches) so multiple components share one HTTP call.
- **State:** `BehaviorSubject` for local service state; **NgRx** for cross-module state — component dispatches action → reducer produces new state → selectors → `async` pipe in templates; effects isolate side effects. One line: "state as immutable single source of truth."

## 10. Interceptors

- **What:** middleware on every HTTP call in/out (chain, order matters — register auth → trace-id → error).
- **Angular 15+ style:** functional interceptor `authInterceptor: HttpInterceptorFn = (req, next) => ...`.
- **Auth interceptor:** `req.clone({ setHeaders: { Authorization: 'Bearer ' + token } })`.
- **The 401 refresh flow (know it step by step):**
  1. Call fails with 401 → `catchError` → skip if the request IS the refresh call (marker header/context) → call `authService.refresh()` → **share the in-flight refresh observable** so 10 parallel 401s trigger ONE refresh (queue the rest) → on success, `switchMap` retry the original request with the new token.
  2. Refresh also fails → logout + redirect.
- **Other uses:** inject `X-Trace-Id` header (correlates with backend ELK logs), normalize HTTP errors into the app's error model, logging in dev.

## 11. Authorization (Authorized) in Angular

- **Guards — functional style (v15+):** `canActivate: [authGuard, roleGuard]`; guard returns `boolean | UrlTree` (UrlTree redirect to `/login` or `/403`).
  - `authGuard`: checks token exists/expiry; async token validation returns `Observable<boolean>`.
  - `roleGuard`: reads required roles from **route data** (`data: { roles: ['ADMIN'] }`), compares with decoded JWT claims (`jwt-decode`).
- **Guard types:** `CanActivate` (page), `CanActivateChild` (subtree), **`CanMatch`** (v15+, replaces CanLoad — blocks even downloading the lazy chunk), `CanDeactivate` (unsaved form warning).
- **UI-level:** structural directive `*appHasRole="'ADMIN'"` to hide buttons; role-based menu config.
- **The line that scores points:** "Frontend authorization is UX only — every route/action is re-authorized server-side: JWT verified at the **Spring Cloud Gateway**, method-level with `@PreAuthorize` in the services, and data-layer checks. If someone bypasses the UI they still hit 403."

---

# QUICK-FIRE (expect a few)

- **Java 17/21:** records (immutable DTOs), sealed interfaces (closed domain hierarchies), switch expressions, text blocks; **virtual threads (21)** — cheap blocking IO threads; pilot for IO-heavy partner calls (honest: not prod-critical yet).
- **Streams vs loops:** streams for declarative transform of collections; not for everything — readability first.
- **REST versioning:** URL `/v1/` for breaking changes (simple, cacheable, gateway-routable) and header `Accept: version=2` for internal clients; deprecation window + Sunset header.
- **Microservices vs monolith:** start modular monolith; split when scaling/deployment/teams demand it; cost = distributed tx, tracing, eventual consistency.
- **Idempotency in payments:** idempotency key on write APIs — first call executes, retries return the same result (ties to Kafka dedupe answer).

# STAR STORY (rehearse 90 seconds)

**Duplicate notification events at peak:** peak load → consumer rebalance caused redelivery → customers got duplicate SMS/email.
Fix: event_id dedupe table + Redis TTL cache before processing; manual offset commit only after successful processing; cooperative-sticky assignor to reduce rebalances; DLT + alerting for anything still failing.
Result: zero duplicate sends after rollout; consumer lag alarm tuned on Grafana.

# Questions to ask THEM (leaves a good impression)

1. Current architecture — monolith being split, or greenfield microservices? Team split BE/FE or fullstack squads?
2. Which Angular version and state management are you on today — any migration planned (e.g. to signals)?
3. How do you run Kafka and search today — MSK/self-managed? Who owns DevOps vs the dev team?
4. What does success look like in the first 3 months for this role?
