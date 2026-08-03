# AIF-C01 Mock Questions (60 questions + detailed explanations)

> **Instructions:** Day 6 — do all 60 in one 90-minute sitting, no notes. Target ≥ 75%.
> **Format:** 50 single-answer + 10 multiple-response (like the real exam).
> Answers + explanations are at the bottom — don't peek!

---

## 📋 Domain 1 — AI & ML Fundamentals (12 questions)

**1. A retailer wants to group customers into segments based on purchasing behavior. They have no predefined categories. Which type of ML?**
A. Supervised
B. Unsupervised
C. Reinforcement
D. Semi-supervised

**2. Which AWS service extracts text and key-value pairs from scanned PDF invoices?**
A. Amazon Comprehend
B. Amazon Rekognition
C. Amazon Textract
D. Amazon Transcribe

**3. Six months after deploying a fraud-detection model, accuracy dropped from 94% to 79%. What most likely happened?**
A. Underfitting
B. Data leakage
C. Model drift
D. Overfitting

**4. A company needs real-time, sub-100ms inference on individual transactions. Which inference type?**
A. Batch inference
B. Real-time (online) inference
C. Asynchronous inference
D. Serverless inference

**5. Convert a 60-minute doctor-patient conversation into structured clinical notes. Which AWS service?**
A. Amazon Transcribe
B. Amazon Polly
C. AWS HealthScribe
D. Amazon Comprehend Medical

**6. Predict whether a customer will cancel their subscription within 30 days, using a labeled historical dataset. Which ML type?**
A. Unsupervised clustering
B. Reinforcement learning
C. Supervised classification
D. Generative AI

**7. A business analyst with no coding experience needs to build an ML model on a customer churn dataset. Which AWS tool?**
A. Amazon SageMaker Studio
B. Amazon SageMaker Canvas
C. AWS Glue
D. Amazon Bedrock

**8. Which AWS service provides human labeling for a dataset of medical images?**
A. SageMaker Ground Truth
B. SageMaker Feature Store
C. SageMaker JumpStart
D. SageMaker Pipelines

**9. Forecasting next quarter's product demand. Which AWS service?**
A. Amazon Personalize
B. Amazon Forecast
C. Amazon Rekognition
D. Amazon Lex

**10. Build a conversational voice bot (Alexa-style) that books appointments. Which AWS service?**
A. Amazon Polly
B. Amazon Lex
C. Amazon Transcribe
D. Amazon Kendra

**11. Detect offensive images uploaded to a social app. Which AWS service?**
A. Amazon Comprehend
B. Amazon Rekognition
C. Amazon Polly
D. Amazon Textract

**12. Extract sentiment and key phrases from customer reviews. Which AWS service?**
A. Amazon Comprehend
B. Amazon Rekognition
C. Amazon Forecast
D. Amazon Translate

---

## 📋 Domain 2 — GenAI Fundamentals (15 questions)

**13. A customer-service bot must return identical responses to identical prompts. Which inference parameter should be set?**
A. Top-P = 1.0
B. Temperature = 0
C. Max tokens = 100
D. Top-K = 50

**14. A company has 8,000 internal HR PDFs and wants an accurate Q&A assistant. Which approach is MOST appropriate?**
A. Fine-tune an LLM on the PDFs
B. Use prompt engineering
C. RAG with a knowledge base of the PDFs
D. Train a new LLM from scratch

**15. Which metric is best for evaluating an automated text summarization feature?**
A. BLEU
B. ROUGE
C. Perplexity
D. Accuracy

**16. A foundation model confidently states facts about events from last week, but the events never happened. What limitation is this?**
A. Knowledge cutoff
B. Hallucination
C. Bias
D. Overfitting

**17. Embeddings are MOST useful for:**
A. Generating images
B. Semantic search and similarity matching
C. Translating languages
D. Compressing models

**18. A team wants an LLM to query a database and book meetings on the user's behalf. Which AWS feature?**
A. Bedrock Knowledge Bases
B. Bedrock Agents
C. SageMaker Pipelines
D. Amazon Q Developer

**19. Which is a recommended way to reduce hallucination in a GenAI application?**
A. Increase temperature
B. Use RAG to ground answers in retrieved context
C. Reduce max tokens
D. Use a smaller model

**20. Few-shot prompting means:**
A. Asking the model to do something with zero context
B. Including 2–5 example input/output pairs in the prompt
C. Training the model on a few examples
D. Calling the model multiple times

**21. Which best describes a foundation model's context window?**
A. Maximum number of parameters
B. Maximum number of tokens (input + output) the model can process
C. The number of training examples
D. The model's training data size

**22. A vendor wants the cheapest approach to make an LLM answer questions in a specific tone. Where should they start?**
A. Train a model from scratch
B. Fine-tune
C. Prompt engineering
D. Continued pre-training

**23. Company X wants semantic search across 100,000 wiki pages. Which combination is most idiomatic on AWS?**
A. Comprehend + S3
B. Bedrock embeddings model + OpenSearch Serverless
C. Polly + Lex
D. Rekognition + Kendra

**24. "Chain-of-Thought" prompting is BEST suited for:**
A. Generating images
B. Multi-step reasoning problems
C. Sentiment classification
D. Translation

**25. Which is NOT a typical limitation of GenAI?**
A. Hallucination
B. Knowledge cutoff
C. Perfect mathematical reliability
D. High compute cost

**26. Embeddings on AWS can be generated by:**
A. Amazon Titan Embeddings
B. Amazon Polly
C. Amazon Rekognition
D. Amazon Transcribe

**27. RAG typically uses which sequence?**
A. Retrieve → Augment → Generate
B. Generate → Retrieve → Augment
C. Augment → Generate → Retrieve
D. Retrieve → Generate → Augment

---

## 📋 Domain 3 — Foundation Models (17 questions)

**28. A startup wants to use Claude 3 in production with NO infrastructure to manage. Which AWS service?**
A. Amazon SageMaker Hosting
B. Amazon EC2 with GPU
C. Amazon Bedrock
D. AWS Lambda

**29. Need RAG over Confluence + S3 with the LEAST engineering effort. Which AWS feature?**
A. Bedrock Agents
B. Bedrock Knowledge Bases
C. SageMaker Pipelines
D. AWS Glue

**30. An e-commerce site needs embeddings for 1 million product descriptions. Which Bedrock model family?**
A. Titan Text
B. Titan Embeddings
C. Titan Image Generator
D. Claude

**31. Need guaranteed throughput for high-volume Bedrock inference at predictable cost. Which feature?**
A. On-Demand
B. Provisioned Throughput
C. Batch inference
D. Async inference

**32. Block SSNs and hate speech in a Bedrock-powered app. Which feature?**
A. IAM policy
B. Bedrock Guardrails
C. SageMaker Clarify
D. Macie

**33. Fine-tune an open-source Llama model with full control over training hyperparameters. Bedrock or SageMaker?**
A. Amazon Bedrock
B. Amazon SageMaker

**34. Cheapest model class for simple summarization at scale:**
A. Claude Opus
B. Claude Haiku / Titan Lite
C. Stable Diffusion
D. Titan Image Generator

**35. Which SageMaker feature provides pre-trained FMs and one-click deploy?**
A. SageMaker Ground Truth
B. SageMaker JumpStart
C. SageMaker Feature Store
D. SageMaker Canvas

**36. An enterprise assistant that answers from internal data in SharePoint + S3 + Confluence. Which AWS product?**
A. Amazon Q Business
B. Amazon Kendra
C. Amazon Lex
D. Amazon Polly

**37. A developer IDE assistant that generates Python code inline. Which AWS product?**
A. Amazon Q Developer
B. Amazon CodeCatalyst
C. Amazon Comprehend
D. AWS HealthScribe

**38. Need an LLM with a very large context window to summarize a 200-page contract. Best Bedrock choice?**
A. Titan Image Generator
B. Claude (Anthropic)
C. Titan Lite
D. Stable Diffusion

**39. Compare three Bedrock models on accuracy and toxicity automatically. Which feature?**
A. Bedrock Agents
B. Bedrock Model Evaluation
C. Bedrock Guardrails
D. SageMaker Clarify

**40. RAG fixes which two problems of vanilla LLMs?**
A. Cost + latency
B. Hallucination + knowledge cutoff / private data
C. Bias + overfitting
D. Bias + cost

**41. In Bedrock, what happens to customer prompts and outputs?**
A. They are shared with model providers to improve models
B. They are NOT used to train base models and NOT shared with providers
C. They are stored publicly
D. They are deleted after 30 days and shared anonymized

**42. Need a managed vector database for RAG with minimal ops. Most common AWS picks include:**
A. EC2 + Redis, self-managed
B. OpenSearch Serverless or RDS pgvector or Kendra
C. DynamoDB Streams
D. S3 + Athena

**43. An agent in Bedrock wants to call a third-party API. The Bedrock feature enabling this is:**
A. Knowledge Bases
B. Agents (with action groups / tools)
C. Guardrails
D. Model Evaluation

**44. Cost optimization technique that lowers unit cost for processing millions of records overnight:**
A. Increase temperature
B. Batch inference
C. Provisioned Throughput
D. Use a larger model

---

## 📋 Domain 4 — Responsible AI (8 questions)

**45. A loan-approval model treats older applicants unfairly. What kind of issue, and which AWS tool detects it?**
A. Cost / AWS Cost Explorer
B. Bias / SageMaker Clarify
C. Latency / CloudWatch
D. Drift / Model Monitor

**46. Documenting a model's intended use, training data, performance, and risks is done with:**
A. SageMaker Model Cards
B. CloudTrail logs
C. IAM policies
D. CloudWatch alarms

**47. A team actively tries to elicit harmful outputs from a GenAI model before launch. This practice is called:**
A. Blue-teaming
B. Red-teaming
C. Green-teaming
D. Shadow testing

**48. Two ways to reduce hallucination in a GenAI app are:**
A. Increase temperature + use a larger model
B. Use RAG + lower temperature
C. Remove Guardrails + fine-tune
D. Increase max tokens + remove citations

**49. Interpretability differs from explainability in that interpretability refers to:**
A. Models that are intrinsically understandable (e.g., decision trees)
B. Post-hoc explanations of black-box models
C. Visualization tools
D. Human-readable API docs

**50. The MOST cost-effective stage to mitigate bias is:**
A. During deployment
B. After deployment, via monitoring
C. During data collection and pre-processing
D. After model training, via post-processing

**51. AWS provides transparency documents for each AI service describing intended use and limitations. These are called:**
A. AWS AI Service Cards
B. AWS Whitepapers
C. AWS Well-Architected Framework
D. AWS Compliance Reports

**52. Which Bedrock feature helps enforce responsible AI by blocking harmful content and PII?**
A. Bedrock Agents
B. Bedrock Guardrails
C. Bedrock Provisioned Throughput
D. Bedrock Model Evaluation

---

## 📋 Domain 5 — Security & Governance (8 questions)

**53. Who is responsible for prompts sent to Amazon Bedrock?**
A. AWS
B. The model provider (e.g., Anthropic)
C. The customer (you)
D. AWS and the provider jointly

**54. A healthcare startup wants to use Bedrock with patient data. Which controls are required? (pick best set)**
A. Confirm model is HIPAA-eligible, encrypt with KMS, restrict via IAM
B. Make the bucket public
C. Disable CloudTrail
D. Use IAM users with long-lived keys

**55. Audit "who invoked which Bedrock model and when." Which AWS service?**
A. CloudWatch Metrics
B. AWS CloudTrail
C. AWS Config
D. Amazon Macie

**56. Block prompt injection and mask emails in Bedrock responses. Which feature?**
A. IAM policy
B. Bedrock Guardrails
C. KMS
D. PrivateLink

**57. Detect that production model quality degraded because input distribution shifted. Which service?**
A. SageMaker Model Monitor
B. CloudTrail
C. Macie
D. IAM

**58. Call Bedrock from a VPC without traversing the public internet. Which AWS feature?**
A. Internet Gateway
B. AWS PrivateLink (VPC endpoint)
C. NAT Gateway
D. Public IP on EC2

**59. Encrypt training data stored in S3. Which AWS service?**
A. AWS KMS (SSE-KMS)
B. IAM
C. CloudWatch
D. CloudTrail

**60. Discover and protect PII stored in S3 buckets automatically. Which AWS service?**
A. Amazon Macie
B. Amazon Polly
C. Amazon Lex
D. AWS Glue

---

---

# ✅ Answer Key + Explanations

## Domain 1

| Q | Answer | Why |
|---|---|---|
| 1 | **B. Unsupervised** | No predefined labels/categories → clustering. |
| 2 | **C. Amazon Textract** | OCR for scanned docs/forms. Comprehend does NLP on text already extracted. |
| 3 | **C. Model drift** | Real-world data changed over time → retrain with fresh data. |
| 4 | **B. Real-time (online) inference** | Low-latency single requests. |
| 5 | **C. AWS HealthScribe** | Specifically for clinical notes from doctor-patient audio. |
| 6 | **C. Supervised classification** | Labeled data + binary outcome. |
| 7 | **B. SageMaker Canvas** | No-code ML for business users. |
| 8 | **A. SageMaker Ground Truth** | Human labeling service. |
| 9 | **B. Amazon Forecast** | Time-series forecasting. |
| 10 | **B. Amazon Lex** | Conversational bots (Alexa tech). |
| 11 | **B. Amazon Rekognition** | Image/video moderation. |
| 12 | **A. Amazon Comprehend** | NLP: sentiment, entities, key phrases. |

## Domain 2

| Q | Answer | Why |
|---|---|---|
| 13 | **B. Temperature = 0** | Deterministic, repeatable outputs. |
| 14 | **C. RAG** | Cheaper than fine-tuning; grounds answers; easy to update. |
| 15 | **B. ROUGE** | Recall-oriented metric for summarization. BLEU = translation. |
| 16 | **B. Hallucination** | Confidently stating false information. (Knowledge cutoff is about events after training date — here the issue is the model inventing facts.) |
| 17 | **B. Semantic search and similarity** | Embeddings turn text into vectors for nearest-neighbor search. |
| 18 | **B. Bedrock Agents** | LLM + tools (Lambda, APIs). |
| 19 | **B. RAG** | Grounds answers in retrieved context. |
| 20 | **B. Including 2–5 example pairs in the prompt** | Few-shot = examples in the prompt; no training. |
| 21 | **B. Max tokens (input+output)** | Defines how much text the model can ingest. |
| 22 | **C. Prompt engineering** | Cheapest starting point; try before fine-tune. |
| 23 | **B. Bedrock embeddings + OpenSearch Serverless** | Canonical RAG stack. |
| 24 | **B. Multi-step reasoning** | "Let's think step by step" improves math/logic. |
| 25 | **C. Perfect mathematical reliability** | LLMs are famously BAD at reliable math. |
| 26 | **A. Titan Embeddings** | Embedding model in Bedrock. |
| 27 | **A. Retrieve → Augment → Generate** | That's literally the acronym. |

## Domain 3

| Q | Answer | Why |
|---|---|---|
| 28 | **C. Amazon Bedrock** | Serverless FM service. |
| 29 | **B. Bedrock Knowledge Bases** | Managed RAG; minimal engineering. |
| 30 | **B. Titan Embeddings** | Embedding model. |
| 31 | **B. Provisioned Throughput** | Flat-rate capacity for predictable high-volume cost. |
| 32 | **B. Bedrock Guardrails** | Content filters + PII redaction. |
| 33 | **B. Amazon SageMaker** | Full control over training hyperparams. |
| 34 | **B. Claude Haiku / Titan Lite** | Smallest, cheapest variants. |
| 35 | **B. SageMaker JumpStart** | Pre-trained model hub. |
| 36 | **A. Amazon Q Business** | Enterprise assistant across data sources. (Kendra = the search; Q Business = GenAI assistant on top.) |
| 37 | **A. Amazon Q Developer** | IDE code assistant. |
| 38 | **B. Claude (Anthropic)** | Known for very large context windows. |
| 39 | **B. Bedrock Model Evaluation** | Compare models on criteria. |
| 40 | **B. Hallucination + knowledge cutoff / private data** | RAG = grounded + current + private. |
| 41 | **B. Not used to train base models, not shared** | Bedrock's privacy guarantee. |
| 42 | **B. OpenSearch Serverless / pgvector / Kendra** | The common managed choices. |
| 43 | **B. Agents (action groups)** | Tools/APIs callable by the LLM. |
| 44 | **B. Batch inference** | Lower unit cost for non-real-time workloads. |

## Domain 4

| Q | Answer | Why |
|---|---|---|
| 45 | **B. Bias / SageMaker Clarify** | Detects bias in data and model. |
| 46 | **A. SageMaker Model Cards** | Model documentation artifact. |
| 47 | **B. Red-teaming** | Adversarial testing pre-launch. |
| 48 | **B. RAG + lower temperature** | Both reduce hallucination. |
| 49 | **A. Intrinsically understandable models** | Interpretability = built-in; explainability = post-hoc. |
| 50 | **C. Data collection / pre-processing** | Cheapest and most effective. |
| 51 | **A. AWS AI Service Cards** | Per-service transparency docs. |
| 52 | **B. Bedrock Guardrails** | Harmful content + PII filters. |

## Domain 5

| Q | Answer | Why |
|---|---|---|
| 53 | **C. The customer (you)** | You always own your prompts/data. |
| 54 | **A. HIPAA-eligible model + KMS + IAM** | Standard healthcare controls. |
| 55 | **B. AWS CloudTrail** | API audit log. |
| 56 | **B. Bedrock Guardrails** | Prompt-attack filter + PII mask. |
| 57 | **A. SageMaker Model Monitor** | Detects data/model drift in production. |
| 58 | **B. AWS PrivateLink** | Private connectivity; no public internet. |
| 59 | **A. AWS KMS (SSE-KMS)** | Encryption at rest in S3. |
| 60 | **A. Amazon Macie** | Discovers/protects PII in S3. |

---

## 📊 Scoring guide

- **≥ 50/60 (83%+):** You're ready. Book the exam.
- **45–49 (75–82%):** Solid — drill flashcards on weak domains.
- **38–44 (63–74%):** Borderline. Re-read cheat sheets for wrong domains.
- **< 38:** Not ready yet — extend study to 10–14 days.

---

## ✅ Self-check question answers (from cheat sheets)

### Domain 1 self-checks
1. **Unsupervised (clustering)** — e.g., K-Means.
2. **Amazon Textract** (OCR) + optionally Comprehend for PII classification.
3. **Model drift** → retrain with recent data.
4. **Real-time / online inference.**
5. **AWS HealthScribe.**

### Domain 2 self-checks
1. **Temperature = 0.**
2. **RAG** (likely via Bedrock Knowledge Bases).
3. **ROUGE.**
4. **Knowledge cutoff** (or hallucination if it fabricated details).
5. **Bedrock Agents.**

### Domain 3 self-checks
1. **Amazon Bedrock.**
2. **Bedrock Knowledge Bases.**
3. **Amazon Titan Embeddings.**
4. **Provisioned Throughput.**
5. **Bedrock Guardrails.**
6. **Amazon SageMaker** (full control).
7. **Claude Haiku / Titan Lite.**

### Domain 4 self-checks
1. **Bias → SageMaker Clarify.**
2. **SageMaker Clarify.**
3. **SageMaker Model Cards.**
4. **Red-teaming.**
5. **RAG + lower temperature (+ citations).**

### Domain 5 self-checks
1. **The customer (you).**
2. **HIPAA-eligible model + KMS + IAM + CloudTrail.**
3. **AWS CloudTrail.**
4. **Bedrock Guardrails.**
5. **SageMaker Model Monitor.**
6. **AWS PrivateLink / VPC endpoint.**

---

_Generated 2026-07-04. These questions are original and written in the style of AIF-C01; they are not official AWS exam questions._
