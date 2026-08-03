# Domain 4 — Guidelines for Responsible AI (14%)

> **What AWS tests:** Bias & fairness, explainability, transparency, and AWS's responsible-AI frameworks. Lighter on services, heavier on concepts & vocabulary.

---

## 4.1 Core principles of responsible AI

Most organizations (incl. AWS) align around these principles:

| Principle | Meaning |
|---|---|
| **Fairness / Bias mitigation** | Treat groups equitably |
| **Explainability / Interpretability** | Humans can understand decisions |
| **Privacy & Security** | Protect user data |
| **Transparency** | Disclose AI use, limitations |
| **Accountability** | Humans remain responsible |
| **Veracity / Reliability** | Outputs are accurate & robust |
| **Robustness & Safety** | Resists misuse, errors, adversarial attacks |
| **Contestability** | Users can challenge AI decisions |
| **Inclusivity** | Benefits broad populations |

> 🧠 **Exam trick:** If a question describes "model rejects loan applications from a specific zip code more often" → **fairness / bias** issue.

---

## 4.2 Bias — types and sources

### Where bias enters
1. **Data bias** — historical, representation, measurement bias in training data.
2. **Algorithmic bias** — model amplifies patterns.
3. **Human / annotation bias** — labelers inject prejudice.
4. **Deployment bias** — used in a context it wasn't designed for.

### Types of bias
| Type | What |
|---|---|
| **Selection / sampling bias** | Training data not representative |
| **Historical bias** | Real-world inequalities baked into data |
| **Measurement bias** | Features are proxies for protected attributes |
| **Aggregation bias** | One model fits none when subgroups differ |
| **Evaluation bias** | Benchmarks don't reflect real users |
| **Deployment bias** | Misused outside intended scope |

### Stages to mitigate bias
- **Pre-processing** — fix the data (reweighing, resampling, synthetic data).
- **In-training** — fairness constraints, adversarial debiasing.
- **Post-processing** — adjust predictions / thresholds per group.

> 🧠 **Exam trick:** "Best place to detect and fix bias?" → **During data collection & before training (pre-processing)** — cheapest and most effective.

---

## 4.3 Explainability vs. Interpretability

| Term | Meaning |
|---|---|
| **Interpretability** | Model is *intrinsically* understandable (linear regression, decision trees). |
| **Explainability** | Use techniques to explain a **black-box** model (SHAP, LIME). |

### Why it matters
- **Trust** — users accept decisions they understand.
- **Compliance** — GDPR "right to explanation", finance/health regulators.
- **Debugging** — find why a model made a wrong call.

### AWS tool: SageMaker Clarify
- Detects **bias** in data and model.
- Provides **feature importance** (explainability) via SHAP.
- Works across the ML lifecycle (pre-training, post-training, monitoring).

> 🧠 **Exam trick:** "Detect bias in training data and explain predictions" → **SageMaker Clarify**.

---

## 4.4 Transparency & disclosure

- Tell users they are interacting with AI.
- Disclose capabilities & limitations (knowledge cutoff, hallucination risk).
- Maintain documentation: **Model Cards**.

### AWS tool: SageMaker Model Cards
- Single source of truth for a model: intent, data, performance, risks.
- Helps audits and governance.

---

## 4.5 Veracity / reliability (GenAI-specific)

| Risk | Mitigation |
|---|---|
| **Hallucination** | RAG, grounding, citations, lower temperature |
| **Inconsistent outputs** | Temperature = 0, prompt templates |
| **Drift** | Monitor + retrain |
| **Prompt injection / jailbreaks** | Bedrock Guardrails, input validation |

---

## 4.6 Robustness & safety

- **Adversarial robustness** — model resists malicious inputs.
- **Out-of-distribution handling** — fails gracefully on unfamiliar inputs.
- **Red-teaming** — humans actively try to break the model before release.
- **Safety evaluations** — automated + human safety tests.

> 🧠 **Exam trick:** "Team needs to actively find harmful outputs before launch" → **Red teaming**.

---

## 4.7 AWS responsible-AI frameworks

| Resource | Purpose |
|---|---|
| **AWS AI Service Cards** | Transparency documents for each AWS AI service (intended use, limitations) |
| **SageMaker Clarify** | Bias detection + explainability |
| **SageMaker Model Cards** | Model documentation |
| **Bedrock Guardrails** | Block harmful content, filter PII, deny topics |
| **AWS Responsible ML Guide** | Best-practices whitepaper |
| **AWS AI Acceptable Use Policy** | What you can/can't do with AWS AI services |

---

## 4.8 Integration into the ML lifecycle

| Stage | Responsible-AI action |
|---|---|
| Problem framing | Define fairness metric up-front |
| Data collection | Check representativeness; run Clarify |
| Training | Constrained optimization; debias |
| Evaluation | Test across subgroups; document with Model Cards |
| Deployment | Disclose AI to users; provide contestability |
| Monitoring | Watch for drift, bias re-emergence |

---

## 🔑 Domain 4 key takeaways

1. **Bias is best fixed early** — pre-processing > post-processing.
2. **Interpretability = intrinsic; Explainability = tools (SHAP, LIME).**
3. **SageMaker Clarify** = bias detection + explainability on AWS.
4. **SageMaker Model Cards / AI Service Cards** = transparency documents.
5. **Bedrock Guardrails** = safety for GenAI.
6. **Red teaming** = pre-launch adversarial testing.
7. **Responsible-AI principles:** fairness, explainability, privacy, transparency, accountability, robustness, contestability.

---

## ✅ Self-check questions (answers in `06-mock-questions.md`)

1. Loan-approval model treats older applicants unfairly. What kind of issue, and which AWS tool detects it?
2. Need to detect bias in your training dataset. Which single AWS tool?
3. Documenting a model's intended use, data, and limitations — which AWS feature?
4. Pre-launch activity where team tries to elicit harmful outputs. Term?
5. Two ways to reduce hallucination in a GenAI app.
