# Domain 5 — Security, Compliance, and Governance for AI Solutions (14%)

> **What AWS tests:** AWS shared-responsibility model applied to AI, data protection (in transit / at rest), IAM, monitoring, and compliance/regulatory frameworks relevant to AI workloads.

---

## 5.1 AWS shared responsibility — for AI services

AWS = responsible **for** security OF the cloud; you = responsible **for** security IN the cloud. With AI, the line depends on the service abstraction:

| Layer | Bedrock (serverless) | SageMaker (managed infra) |
|---|---|---|
| Models / providers | AWS + provider | You (if custom) |
| Model hosting infra | **AWS** | **Shared** (you pick instances, VPC) |
| OS / patching | AWS | **You** (unless SageMaker managed) |
| Network / firewall | AWS | You (Security Groups, VPC) |
| Data / prompts / fine-tune data | **YOU** | **YOU** |
| IAM, encryption keys | **YOU** | **YOU** |

> 🧠 **Exam trick:** "Who is responsible for the prompts and fine-tuning data?" → **Always the customer (you).** Even on Bedrock.

### Bedrock data privacy guarantee
- Customer prompts/outputs are **NOT** used to train base models.
- **NOT** shared with model providers.
- Stay in **your account**, in the **region** you call.

---

## 5.2 Data protection

### Encryption — three states
| State | Where | AWS feature |
|---|---|---|
| **At rest** | S3, EBS, RDS, vector DB | AWS KMS (SSE-KMS, SSE-S3) |
| **In transit** | Network | TLS / HTTPS |
| **In use** | Memory | (confidential computing — niche) |

> 🧠 **Exam trick:** "Encrypt prompts stored in S3" → **KMS with SSE-KMS**.
> "Secure data flowing between app and Bedrock" → **TLS/HTTPS**.

### AWS KMS (Key Management Service)
- Create & manage encryption keys.
- **Customer Managed Keys (CMK)** give full control (rotation, policies).
- **AWS managed keys** are auto-created per service.
- Bedrock / SageMaker support **bring-your-own-key** for some models.

### Macie / Glue
- **Amazon Macie** — automatically discover & protect sensitive data (PII) in S3.
- **AWS Glue DataBrew / Comprehend** — detect PII for cleaning.

---

## 5.3 IAM for AI workloads

- Apply **least privilege** — grant only the permissions needed.
- Use **roles** (not access keys) for EC2/Lambda/SageMaker calling Bedrock.
- Use **resource-based policies** on S3 buckets holding training data.
- **Bedrock** is controlled via IAM: `bedrock:InvokeModel`, `bedrock:CreateGuardrail`, etc.

> 🧠 **Exam trick:** "SageMaker notebook needs to read training data in S3" → **IAM role** attached to the notebook with read-only S3 permission.

### Controlling access to specific models
- Use IAM **policies** to restrict which Bedrock models an IAM user/role can invoke.
- Combine with **Service Control Policies (SCPs)** at the organization level.

---

## 5.4 VPC & network security

- **PrivateLink** — privately access AWS services (Bedrock, SageMaker) without going over the public internet.
- **SageMaker in VPC** — train/host in private subnets; no public IP.
- **Security Groups / NACLs** — restrict traffic.
- **S3 VPC endpoints** — keep data within VPC.

> 🧠 **Exam trick:** "Regulated industry wants to call Bedrock without traversing the public internet." → **AWS PrivateLink / VPC endpoint**.

---

## 5.5 Monitoring & auditing

| Service | Purpose |
|---|---|
| **AWS CloudTrail** | API audit log — who called what, when |
| **Amazon CloudWatch** | Metrics, logs, alarms |
| **CloudWatch Logs Insights** | Query logs |
| **SageMaker Model Monitor** | Detect data drift / model quality in production |
| **AWS Config** | Track config changes, compliance rules |
| **AWS Security Hub** | Central security findings |
| **Amazon GuardDuty** | Threat detection |
| **AWS Audit Manager** | Automate compliance evidence collection |

> 🧠 **Exam trick:** "Audit who invoked a Bedrock model and when" → **CloudTrail**.
> "Detect that production model quality dropped because input data changed" → **SageMaker Model Monitor**.

---

## 5.6 Generative-AI-specific security concerns

| Risk | Mitigation on AWS |
|---|---|
| **Prompt injection / jailbreak** | Bedrock Guardrails (prompt attack filter), input validation |
| **PII leakage** | Guardrails PII filter, Macie, Comprehend PII detection |
| **Toxic / harmful output** | Guardrails content filters, lower temperature |
| **Data poisoning** | Validate training data, SageMaker Ground Truth reviews |
| **Model exfiltration** | IAM, SCPs, restrict `InvokeModel` / download |
| **Over-permissioned apps** | Scoped IAM roles for Agents/Lambda |

### Bedrock Guardrails — key filters
- **Content filters** — hate, insults, sexual, violence (configurable severity).
- **Denied topics** — block subjects (e.g., medical advice).
- **Word filters** — block/allow lists.
- **PII filter** — redact SSN, email, phone, etc.
- **Contextual grounding check** — detect hallucinations vs. retrieved context.

> 🧠 **Exam trick:** "Block prompt injection AND mask SSNs in Bedrock responses" → **Guardrails**.

---

## 5.7 Compliance frameworks relevant to AI

| Framework | What |
|---|---|
| **GDPR** | EU data privacy — right to explanation, data deletion |
| **HIPAA** | US healthcare data (PHI) |
| **PCI-DSS** | Payment card data |
| **EU AI Act** | Risk-based regulation of AI systems (banned / high-risk / limited / minimal) |
| **NIST AI RMF** | US voluntary AI risk-management framework |
| **ISO/IEC 42001** | AI management system standard |
| **SOC 2** | Security/availability controls audit |

### AWS compliance artifacts
- **AWS Artifact** — download SOC, ISO, PCI reports.
- **AWS Audit Manager** — automate evidence collection.
- Many AWS AI services are **HIPAA-eligible** and **GDPR-ready** — but the customer remains the **data controller**.

> 🧠 **Exam trick:** "Healthcare startup processes patient records with GenAI" → confirm the chosen Bedrock model is **HIPAA-eligible**, encrypt with **KMS**, restrict access via **IAM**, audit with **CloudTrail**.

---

## 5.8 Governance framework for AI

Typical governance components:
1. **Inventory** — what models exist, who owns them.
2. **Risk classification** — high-risk use cases get extra review.
3. **Review board / AI council** — approves deployments.
4. **Documentation** — Model Cards, AI Service Cards.
5. **Monitoring** — drift, bias, security findings.
6. **Incident response** — what happens when AI misbehaves.
7. **Audit & compliance** — periodic evidence collection.

### AWS services for governance
| Service | Role |
|---|---|
| **AWS Config** | Config rules for compliance |
| **AWS CloudTrail** | Audit API calls |
| **AWS Audit Manager** | Evidence collection |
| **AWS Security Hub** | Findings aggregation |
| **SageMaker Model Cards / Registry** | Model governance |

---

## 🔑 Domain 5 key takeaways

1. **Customer is ALWAYS responsible for prompts/fine-tuning data**, even on Bedrock.
2. **Encryption states:** at rest (KMS/SSE), in transit (TLS), in use.
3. **IAM least privilege + roles**; restrict which Bedrock models can be invoked.
4. **PrivateLink / VPC endpoints** → keep AI calls off public internet.
5. **CloudTrail = audit; Model Monitor = drift; Macie = PII in S3; GuardDuty = threats.**
6. **Bedrock Guardrails** = the GenAI safety layer (prompt injection, PII, toxicity).
7. **AI compliance frameworks:** EU AI Act, NIST AI RMF, ISO 42001, GDPR, HIPAA.
8. AWS provides **HIPAA-eligible / GDPR-ready** services — but you're the **data controller**.

---

## ✅ Self-check questions (answers in `06-mock-questions.md`)

1. Who is responsible for prompts sent to Amazon Bedrock?
2. Healthcare startup wants to use Bedrock with patient data. Three controls?
3. Audit "who invoked which Bedrock model, and when" — which service?
4. Block prompt injection + mask emails in Bedrock responses. Which feature?
5. Detect that production model predictions degraded because input distribution shifted. Which service?
6. Call Bedrock from a VPC without traversing the public internet. Which AWS feature?
