# AIF-C01 Flashcards — Active Recall Drill

> **How to use:** Cover the answer column. Say the answer out loud in < 5 seconds. If wrong, mark it and revisit.
> **Goal:** Two full passes on Day 7 — every card should be reflexive.

---

## 🧠 D1 — AI/ML Fundamentals

| # | Question | Answer |
|---|---|---|
| 1 | Hierarchy: AI ⊃ ? ⊃ ? ⊃ GenAI | ML ⊃ Deep Learning ⊃ GenAI |
| 2 | ML type with **labeled** data (input, label) | Supervised |
| 3 | ML type to **cluster** unlabeled data | Unsupervised |
| 4 | ML type using **rewards** | Reinforcement Learning |
| 5 | 6 stages of ML lifecycle | Problem → Data collection → Prep → Train → Evaluate → Deploy & monitor |
| 6 | Performance dropped months after deploy | **Model drift** → retrain |
| 7 | Inference type: sub-100ms per request | Real-time / online |
| 8 | Inference type: process millions of rows overnight | Batch |
| 9 | Service: OCR on scanned PDFs | Amazon **Textract** |
| 10 | Service: sentiment + key phrases in text | Amazon **Comprehend** |
| 11 | Service: object/face detection in images | Amazon **Rekognition** |
| 12 | Service: speech → text | Amazon **Transcribe** |
| 13 | Service: text → speech | Amazon **Polly** |
| 14 | Service: build chatbot/voice bot | Amazon **Lex** |
| 15 | Service: time-series forecasting (sales, demand) | Amazon **Forecast** |
| 16 | Service: real-time recommendations | Amazon **Personalize** |
| 17 | Service: clinical notes from doctor-patient audio | **AWS HealthScribe** |
| 18 | Service: human labeling of datasets | SageMaker **Ground Truth** |
| 19 | No-code ML for business analysts | SageMaker **Canvas** |
| 20 | Pre-trained models + 1-click deploy in SageMaker | SageMaker **JumpStart** |
| 21 | Enterprise natural-language search | Amazon **Kendra** |

---

## 🧠 D2 — GenAI Fundamentals

| # | Question | Answer |
|---|---|---|
| 22 | LLMs process text in chunks called | **Tokens** (~4 chars each) |
| 23 | Max tokens a model can take (input+output) | **Context window** |
| 24 | Parameter to make outputs **deterministic** | **Temperature = 0** |
| 25 | Parameter to make outputs **more creative** | Higher temperature (e.g., 0.8+) |
| 26 | LLM confidently states false facts | **Hallucination** |
| 27 | LLM doesn't know recent events | **Knowledge cutoff** |
| 28 | Best fix for hallucination + private data | **RAG** |
| 29 | RAG pipeline acronym | **R**etrieve → **A**ugment → **G**enerate |
| 30 | Vector for semantic search comes from | **Embeddings model** |
| 31 | Metric for summarization | **ROUGE** |
| 32 | Metric for translation | **BLEU** |
| 33 | Prompting with 2–5 examples | **Few-shot** |
| 34 | Prompting with no examples | **Zero-shot** |
| 35 | "Let's think step by step" technique | **Chain-of-Thought (CoT)** |
| 36 | Cheapest customization tier | **Prompt engineering** |
| 37 | Most expensive customization tier | **Train from scratch** |
| 38 | Bedrock feature: LLM + tool/API calls | **Agents** |
| 39 | Anthropic model family on Bedrock | **Claude** |
| 40 | AWS embedding model | **Titan Embeddings** |

---

## 🧠 D3 — Foundation Models & Bedrock

| # | Question | Answer |
|---|---|---|
| 41 | Serverless service for using FMs (no infra) | **Amazon Bedrock** |
| 42 | End-to-end ML platform for full control | **Amazon SageMaker** |
| 43 | Bedrock feature for **managed RAG** | **Knowledge Bases** |
| 44 | Bedrock feature for LLM tool use | **Agents** |
| 45 | Bedrock feature for content filters + PII | **Guardrails** |
| 46 | Bedrock feature to compare models | **Model Evaluation** |
| 47 | Bedrock feature for high-volume predictable cost | **Provisioned Throughput** |
| 48 | Bedrock: are prompts shared with providers? | **No** |
| 49 | Bedrock: are prompts used to train base models? | **No** |
| 50 | Bedrock model best for very long context | **Claude** |
| 51 | Bedrock model class for cheap summarization | Haiku / Titan Lite |
| 52 | Bedrock model for image generation | Titan Image Generator / Stable Diffusion |
| 53 | AWS vector store options (4) | **OpenSearch Serverless, pgvector (RDS/Aurora), Kendra, MemoryDB** |
| 54 | GenAI assistant for business data | **Amazon Q Business** |
| 55 | IDE code assistant | **Amazon Q Developer** |
| 56 | RAG vs. fine-tune: pick for **new knowledge** | **RAG** |
| 57 | RAG vs. fine-tune: pick for **new style** | **Fine-tune** |
| 58 | Tech that aligns LLMs to be helpful/harmless | **RLHF** |

---

## 🧠 D4 — Responsible AI

| # | Question | Answer |
|---|---|---|
| 59 | Tool: bias detection + SHAP explainability | **SageMaker Clarify** |
| 60 | Artifact: model documentation (intent, data, risks) | **SageMaker Model Cards** |
| 61 | Per-service transparency document from AWS | **AWS AI Service Cards** |
| 62 | Pre-launch adversarial testing | **Red-teaming** |
| 63 | Cheapest stage to fix bias | **Pre-processing / data collection** |
| 64 | Intrinsically understandable model (e.g., trees) | **Interpretable** |
| 65 | Post-hoc explanation of black-box (e.g., SHAP/LIME) | **Explainable** |
| 66 | Bedrock feature enforcing responsible AI | **Guardrails** |

---

## 🧠 D5 — Security & Governance

| # | Question | Answer |
|---|---|---|
| 67 | Who owns/responsibility for prompts in Bedrock? | **Customer (you)** |
| 68 | Encryption of data in S3 | **AWS KMS (SSE-KMS)** |
| 69 | Encryption of data over network | **TLS / HTTPS** |
| 70 | Audit who called which API | **AWS CloudTrail** |
| 71 | Detect production model quality drop from input shift | **SageMaker Model Monitor** |
| 72 | Discover PII in S3 automatically | **Amazon Macie** |
| 73 | Call Bedrock without public internet | **AWS PrivateLink / VPC endpoint** |
| 74 | Bedrock feature: block prompt injection + mask PII | **Guardrails** |
| 75 | Threat detection service | **Amazon GuardDuty** |
| 76 | Centralized security findings | **AWS Security Hub** |
| 77 | AI-specific compliance: EU framework | **EU AI Act** |
| 78 | AI-specific compliance: US voluntary framework | **NIST AI RMF** |
| 79 | AI management system ISO standard | **ISO/IEC 42001** |
| 80 | Download SOC/ISO/PCI reports | **AWS Artifact** |
| 81 | Best practice for EC2/Lambda calling Bedrock | **IAM role (not access keys)** |
| 82 | Restrict which Bedrock models a user can call | **IAM policy** |

---

## 🎯 High-frequency "traps" to remember

| Trap | Correct answer |
|---|---|
| "Use Claude with least ops" | **Bedrock** (not SageMaker) |
| "Internal docs Q&A" | **RAG / Bedrock Knowledge Bases** (not fine-tune) |
| "Identical answers to identical prompts" | **Temperature = 0** |
| "Block harmful content + PII" | **Bedrock Guardrails** |
| "Who's responsible for prompts?" | **Customer** |
| "Audit model invocations" | **CloudTrail** (not CloudWatch) |
| "Detect drift in production" | **SageMaker Model Monitor** |
| "OCR scanned forms" | **Textract** (not Comprehend) |
| "Find PII in S3" | **Macie** |
| "Long contract → summarize" | **Claude** (large context) |
| "Private Bedrock access" | **PrivateLink / VPC endpoint** |
| "Cost optimization at high volume" | **Provisioned Throughput** |
| "Bias detection" | **SageMaker Clarify** |
| "Cheapest customization" | **Prompt engineering** |

---

## ⏱️ Speed round (one-word answers)

1. Serverless FM service? — **Bedrock**
2. RAG acronym? — **Retrieve-Augment-Generate**
3. Determinism parameter? — **Temperature**
4. Summarization metric? — **ROUGE**
5. Translation metric? — **BLEU**
6. OCR service? — **Textract**
7. Image analysis? — **Rekognition**
8. Speech → text? — **Transcribe**
9. Text → speech? — **Polly**
10. Chatbot? — **Lex**
11. Forecasting? — **Forecast**
12. Recommendations? — **Personalize**
13. Bias detection? — **Clarify**
14. PII in S3? — **Macie**
15. Audit log? — **CloudTrail**
16. Drift monitor? — **Model Monitor**
17. LLM tools? — **Agents**
18. Harmful content filter? — **Guardrails**
19. Model docs? — **Model Cards**
20. Pre-launch attack testing? — **Red-teaming**
21. Who owns prompts? — **Customer**
22. Long context model? — **Claude**
23. Embeddings model? — **Titan Embeddings**
24. Enterprise GenAI assistant? — **Amazon Q Business**
25. Code assistant? — **Amazon Q Developer**

You're ready. 🚀 Go pass it.
