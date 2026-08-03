# Domain 3 — Applications of Foundation Models (28%)

> **Highest-weighted domain.** Tests your ability to choose & customize foundation models on AWS, primarily **Amazon Bedrock** vs. **Amazon SageMaker**, plus RAG, fine-tuning, evaluation, and inference cost optimization.

---

## 3.1 Foundation Models (FMs) — basics

- **Foundation model** = large pretrained model adaptable to many tasks.
- **Training stages:**
  1. **Pre-training** — train on massive unlabelled data (most expensive).
  2. **Fine-tuning** — adapt with labeled examples.
  3. **Alignment (RLHF / DPO)** — make outputs helpful, harmless, honest.
  4. **Evaluation** — measure quality & safety.
  5. **Deployment** — serve at scale.
  6. **Inference** — generate predictions.

### RLHF — Reinforcement Learning from Human Feedback
- Humans rank model outputs → a reward model is trained → RL improves the LLM.
- This is what makes modern chat models "helpful" and aligned.

> 🧠 **Exam trick:** "How did vendors make LLMs follow instructions and avoid harmful replies?" → **RLHF**.

---

## 3.2 Amazon Bedrock — the centerpiece 🔥

**Amazon Bedrock** = fully managed, **serverless** service to use foundation models from multiple providers via a single API.

### Key characteristics
- **No infrastructure to manage** (no GPUs to provision).
- **No data used to train models** — your prompts/outputs are NOT shared with model providers.
- Pay-per-use pricing (per token).
- Models from multiple providers:
  - **Amazon** — Titan (text, multimodal, embeddings, image).
  - **Anthropic** — Claude (strong reasoning, long context).
  - **Meta** — Llama.
  - **Mistral AI** — Mistral / Mixtral.
  - **Cohere** — Command (good for RAG/embeddings).
  - **AI21 Labs** — Jurrasic.
  - **Stability AI** — Stable Diffusion (image).

### Bedrock features you MUST know
| Feature | What it does | Trigger words |
|---|---|---|
| **Bedrock Models / On-Demand** | Invoke any FM by API | "call LLM via API" |
| **Provisioned Throughput** | Reserve capacity for high volume | "predictable cost at scale" |
| **Knowledge Bases** | Managed **RAG** (upload docs → vector store → auto retrieval) | "RAG without building pipeline" |
| **Agents** | LLM calls APIs/tools (Lambda, third-party) to take actions | "LLM needs to query DB / call API" |
| **Guardrails** | Block harmful content, filter PII, deny topics | "block toxic content", "redact SSN" |
| **Model Evaluation** | Auto-evaluate models on custom criteria | "compare model A vs. B" |
| **Custom Model** | Fine-tune a Bedrock model on your data | "fine-tune on proprietary data" |
| **Marketplace** | Discover & subscribe to models | "browse models" |

### Bedrock vs. SageMaker — DECISION TABLE (most-tested!)

| Criterion | Amazon Bedrock | Amazon SageMaker |
|---|---|---|
| **Setup effort** | None (serverless API) | High (manage instances, code) |
| **Model selection** | Curated list (Titan, Claude, Llama…) | Any open model or your own |
| **Customization** | Light fine-tuning only | Full training/fine-tuning control |
| **Infrastructure** | Fully managed, no GPUs to manage | You manage instances, scaling |
| **Best for** | Quick GenAI apps, RAG, multi-model | Custom training, niche models, MLOps |
| **Time to production** | Minutes | Days–weeks |

> 🧠 **Exam trick (very common):**
> - "We want to use Claude/Titan with **minimum ops overhead**" → **Bedrock**.
> - "We need to **train a custom model from scratch** on our data" → **SageMaker**.
> - "We want **multiple models from different vendors** behind one API" → **Bedrock**.

---

## 3.3 Choosing the right FM

| Use case | Pick |
|---|---|
| General text generation, chat | Claude 3.x, Titan Text, Llama 3 |
| **Long documents** (100K+ tokens) | **Claude** (large context window) |
| **Reasoning / coding** | Claude 3.5 Sonnet / Opus, Llama 3.1 405B |
| **Cost-sensitive, lightweight** | Titan Lite, Mistral 7B, Llama 3 8B |
| **Embeddings** (for RAG/search) | **Titan Embeddings**, Cohere Embed |
| **Image generation** | Titan Image Generator, Stable Diffusion |
| **Multimodal** (text + image input) | Claude 3 (vision), Titan Multimodal Embeddings |

### Size vs. capability trade-off
- **Larger models**: better quality, slower, pricier.
- **Smaller models**: faster, cheaper, good enough for simple tasks.
- **Bedrock lets you swap models instantly** — start small, upgrade if quality isn't enough.

> 🧠 **Exam trick:** "Application needs cheapest model that meets quality bar" → start with **Titan Text Lite / Haiku**, then scale up if needed.

---

## 3.4 Prompt engineering for FMs (Bedrock context)

Same principles as Domain 2 (zero/few-shot, CoT, role). Bedrock-specific tips:
- Use **system prompts** to set behavior.
- Use **templated prompts** for consistency in production.
- Use **Guardrails** for input/output filtering in production — don't rely only on prompt.

---

## 3.5 RAG on AWS — the canonical architecture

```
User question
    ↓
[Embeddings model]  ── converts query → vector
    ↓
[Vector store]      ── similarity search
    ↓
[Retrieve top-k chunks]
    ↓
[LLM in Bedrock]    ── generates grounded answer
```

### AWS building blocks for RAG
| Layer | Options |
|---|---|
| **Embeddings model** | Amazon Titan Embeddings, Cohere Embed (via Bedrock) |
| **Vector store** | OpenSearch Serverless, RDS PostgreSQL + **pgvector**, Aurora PostgreSQL + pgvector, Amazon Kendra, MemoryDB for Redis, DocumentDB, Neptune Analytics |
| **Managed RAG pipeline** | **Bedrock Knowledge Bases** (orchestrates everything) |
| **LLM** | Any Bedrock model |

### Bedrock Knowledge Bases (highlight)
- **Managed RAG**: upload docs → Bedrock chunks, embeds, stores, retrieves automatically.
- Connects to S3, Confluence, SharePoint, web URLs, etc.
- Returns **citations** to source documents → reduces hallucination.

> 🧠 **Exam trick:** "Want RAG with the **least engineering effort**" → **Bedrock Knowledge Bases**.

### Vector store choice
| Need | Pick |
|---|---|
| Fully managed, simple, semantic search | **Amazon Kendra** |
| Open-source, scalable vector DB | **OpenSearch Serverless** |
| Already on RDS/Aurora | **pgvector** extension |
| Real-time, low-latency cache | **MemoryDB for Redis** |

---

## 3.6 Fine-tuning on AWS

### Bedrock fine-tuning
- **Lightweight fine-tuning** of supported models (e.g., Titan Text, Claude via custom model).
- Provide **JSONL training file** in S3: `{"prompt": "...", "completion": "..."}`.
- Output: a **custom model** you invoke like the base model.
- **Training data is NOT used to train the base model for other customers.**

### SageMaker fine-tuning
- Full control: any algorithm, any framework (PyTorch, TensorFlow, Hugging Face).
- Use **SageMaker JumpStart** for fine-tuning scripts of popular models.
- Use **SageMaker Training Jobs** for distributed training.

### When NOT to fine-tune
- **If the problem is "out-of-date knowledge"** → use **RAG**, not fine-tuning.
- **If you have < a few hundred examples** → use **prompt engineering / few-shot**.
- **Fine-tuning mostly changes style/tone/format**, not facts.

---

## 3.7 Evaluation of foundation models

### Approaches
| Approach | When |
|---|---|
| **Human evaluation** | Gold standard, subjective tasks |
| **Automated metrics** (ROUGE, BLEU, BERTScore) | Scale, reproducibility |
| **LLM-as-a-judge** | Use a strong LLM to grade outputs |
| **Bedrock Model Evaluation jobs** | Compare models side-by-side on custom datasets |
| **Benchmark datasets** (MMLU, HellaSwag, GSM8K) | Standardized capability tests |

### What to evaluate
- **Accuracy / groundedness** (no hallucinations).
- **Toxicity / safety**.
- **Latency & throughput**.
- **Cost per 1K tokens**.
- **Robustness** (prompt variations, adversarial inputs).

> 🧠 **Exam trick:** "Compare 3 models on accuracy + toxicity automatically" → **Bedrock Model Evaluation**.

---

## 3.8 Inference, cost, and optimization

### Cost drivers
- **Token count** (input + output).
- **Model size** (Haiku << Sonnet << Opus).
- **Throughput mode**: on-demand (pay-per-token) vs. **Provisioned Throughput** (flat fee for high volume).

### Optimization techniques
| Technique | Effect |
|---|---|
| **Right-size the model** (Haiku vs. Opus) | Lower $/token |
| **Prompt compression / shorter prompts** | Fewer input tokens |
| **Limit max output tokens** | Fewer output tokens |
| **Caching** (e.g., prompt caching) | Skip redundant calls |
| **Batch inference** | Lower unit cost for non-real-time |
| **Provisioned Throughput** | Predictable cost at very high volume |

### Latency optimization
- Smaller model = faster.
- Smaller context = faster.
- Co-locate in **same AWS region** as your app.
- Use **streaming responses** for perceived speed.

---

## 3.9 SageMaker building blocks (for FM work)

| SageMaker feature | Purpose |
|---|---|
| **SageMaker Studio** | IDE for ML |
| **SageMaker JumpStart** | Pre-trained FMs + 1-click deploy / fine-tune templates |
| **SageMaker Training Jobs** | Distributed training |
| **SageMaker Endpoints** | Real-time inference hosting |
| **SageMaker Asynchronous / Batch Inference** | Non-real-time |
| **SageMaker Pipelines** | MLOps workflows |
| **SageMaker Model Registry** | Version & approve models |
| **SageMaker Feature Store** | Feature management |
| **SageMaker Ground Truth** | Data labeling |

---

## 3.10 Other relevant AWS AI services

| Service | Purpose |
|---|---|
| **Amazon Q** | GenAI assistant for business (Q Business) and for developers (Q Developer) |
| **Amazon Q Developer** | Code generation, IDE assistant (replaces CodeWhisperer) |
| **Amazon Q Business** | Enterprise assistant connected to your data |
| **AWS HealthScribe** | Clinical documentation from audio |
| **Amazon CodeCatalyst** | Dev platform (less AI-focused) |
| **PartyRock** | Free Bedrock playground / app builder |

> 🧠 **Exam trick:** "Build assistant that answers questions from internal Confluence + SharePoint + S3" → **Amazon Q Business** (or Bedrock Knowledge Bases if you want more control).

---

## 🔑 Domain 3 key takeaways

1. **Bedrock = serverless, multi-model, no infra, no training-data sharing.** SageMaker = full control, custom training.
2. **Bedrock features:** Knowledge Bases (RAG), Agents (tools), Guardrails (safety), Model Evaluation, Custom Models, Provisioned Throughput.
3. **RAG > fine-tuning** when the problem is "new/fresh knowledge".
4. **Vector stores on AWS:** OpenSearch Serverless, pgvector (RDS/Aurora), Kendra, MemoryDB.
5. **Model selection:** Claude for long context/reasoning, Titan Embeddings for vectors, Haiku/Lite for cheap, Titan Image / Stable Diffusion for images.
6. **Cost optimization:** right-size, compress prompts, cache, batch, Provisioned Throughput.
7. **Amazon Q** = managed GenAI assistant (Business for enterprise, Developer for code).

---

## ✅ Self-check questions (answers in `06-mock-questions.md`)

1. Company wants Claude 3 with **zero infrastructure management**. Which AWS service?
2. Need RAG over Confluence + S3 with the **least engineering effort**. Which feature?
3. App needs **embeddings for 1M product descriptions**. Which Bedrock model?
4. Need **guaranteed throughput** for high-volume Bedrock inference at predictable cost. Which feature?
5. You want to **block SSNs and hate speech** in a Bedrock app. Which feature?
6. Use case: fine-tune an **open-source LLM** with full control over training hyperparameters. Bedrock or SageMaker?
7. Cheapest model class for simple summarization at scale?
