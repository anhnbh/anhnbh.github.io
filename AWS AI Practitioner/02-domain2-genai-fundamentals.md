# Domain 2 — Fundamentals of Generative AI (24%)

> **What AWS tests:** GenAI vocabulary, LLM mechanics (tokens, parameters, temperature), prompt engineering basics, and the difference between prompt eng / RAG / fine-tuning. **High-yield domain.**

---

## 2.1 What is Generative AI?

**GenAI** = a class of AI that creates **new content** (text, image, audio, code, video) by learning the distribution of its training data.

| Compared to classic ML | Classic ML | GenAI |
|---|---|---|
| Output | A label or number (spam = yes/no) | New content (an essay, an image) |
| Training data | Task-specific labeled data | Massive unlabelled corpora |
| Typical size | Thousands to millions of parameters | **Billions** of parameters |

**Foundation model (FM):** a very large model pretrained on broad data that can be **adapted** to many downstream tasks. Examples: GPT, Claude, Titan, Llama, Stable Diffusion.

**LLM (Large Language Model):** a foundation model specialized on **text**.

---

## 2.2 How LLMs work — concepts you MUST know

### Tokens
- LLMs don't read words — they read **tokens** (chunks of text).
- 1 token ≈ 4 characters of English ≈ ¾ of a word.
- Tokenization affects **cost** (you pay per token) and **context window**.

### Context window
- The **max tokens** the model can ingest (prompt + response).
- Small window (4K) → cheap but forgets long docs. Large window (200K+ like Claude) → can ingest whole books.
- If your prompt + doc exceeds the window → **truncation** or error.

### Parameters
- Internal weights learned during training.
- More parameters → generally more capable, but slower & costlier.
- **Inference parameters** (you control at runtime):
  - **Temperature** (0.0 – 1.0+): controls randomness.
    - `0` = deterministic, repeatable, "safe".
    - `~0.7` = balanced (typical chat).
    - `1.0+` = creative, unpredictable.
  - **Top-P** (nucleus sampling): another randomness control; usually pick one of Top-P or Temperature, not both.
  - **Top-K**: restrict to top K probable next tokens.
  - **Max tokens**: hard cap on response length.
  - **Stop sequences**: tokens that end generation.

> 🧠 **Exam trick:** "Want consistent, reproducible answers for a customer service bot" → **temperature = 0**.
> "Creative ad copy variations" → higher temperature.

### How LLMs generate text
- **Next-token prediction** — repeatedly pick the most likely next token until a stop condition.
- They **don't "know" facts** — they predict plausible-sounding text. This is why hallucinations happen.

---

## 2.3 Capabilities & limitations of GenAI

### ✅ Strengths
- Text generation, summarization, translation, Q&A.
- Code generation & explanation.
- Image/audio/video generation.
- Democratized access — no ML expertise needed to use a model.

### ⚠️ Limitations / risks
| Risk | Meaning | Mitigation |
|---|---|---|
| **Hallucination** | Confidently states false info | RAG, citations, lower temperature |
| **Knowledge cutoff** | Doesn't know events after training date | RAG with fresh sources |
| **Bias & toxicity** | Inherits bias from training data | Guardrails, content filtering |
| **Non-determinism** | Same prompt → different answers | Set temperature = 0 |
| **No real reasoning** | Bad at math / strict logic | Tools, function calling |
| **Cost & latency** | Big models are slow & pricey | Right-size model, caching |
| **Prompt injection** | Malicious input hijacks model | Input sanitization, Guardrails |

> 🧠 **Exam trick:** "Customer service bot occasionally gives wrong product specs from outdated docs" → **hallucination + knowledge cutoff** → fix with **RAG over current docs**.

---

## 2.4 Prompt engineering

### Anatomy of a good prompt
```
[ROLE]       You are a senior AWS Solutions Architect.
[CONTEXT]    The customer is a healthcare startup with HIPAA requirements.
[TASK]       Draft a 3-step migration plan to AWS.
[FORMAT]     Output as a numbered list, max 150 words.
[CONSTRAINTS] Avoid mentioning specific vendor names other than AWS.
```

### Techniques
| Technique | What it does | When |
|---|---|---|
| **Zero-shot** | Ask directly, no examples | Simple tasks |
| **Few-shot** | Give 2–5 examples in prompt | Need consistent style/format |
| **Chain-of-Thought (CoT)** | "Let's think step by step" | Math, reasoning |
| **Role / persona prompting** | Assign a role | Better-quality expert answers |
| **Template / instruction tuning** | Standardize prompts | Production apps |

### Prompt engineering vs. fine-tuning vs. RAG — DECISION TABLE

| Need | Best approach |
|---|---|
| Quick wins, no training data | **Prompt engineering** (cheapest) |
| Ground answers in your private docs (FAQ, manuals) | **RAG** |
| Need specific tone/style/format consistently | **Fine-tuning** |
| Need brand-new capability not in model | **Train from scratch** (rare, expensive) |

> 🧠 **Most common exam question:** "Company has 10,000 internal PDFs and wants an accurate Q&A bot." → Answer is **RAG**, NOT fine-tuning.

---

## 2.5 RAG (Retrieval Augmented Generation) — must master

### Why RAG?
- Solves **hallucination** + **knowledge cutoff** + **private data access**.
- Cheaper than fine-tuning; updates are trivial (just update the knowledge base).

### How RAG works (4 steps)
```
1. User asks: "What's our refund policy?"
2. Retrieve:  vector search finds relevant chunks in your knowledge base
3. Augment:   those chunks are appended to the LLM prompt
4. Generate:  LLM answers grounded in the retrieved context
```

### Key components
- **Embeddings model** — converts text → vectors (numbers). Examples: Titan Embeddings, Cohere Embed.
- **Vector database** — stores vectors for similarity search.
  - On AWS: **OpenSearch Serverless**, **RDS with pgvector**, **Amazon Kendra**, **MemoryDB for Redis**, **DocumentDB**, **Neptune Analytics**.
- **Chunking strategy** — split long docs into retrievable pieces.
- **Knowledge base** — the indexed store RAG pulls from.

> 🧠 **Exam trick:** "Need semantic search over 50K internal wiki pages." → **embeddings + vector store** (or **Amazon Kendra** if you want it managed).

---

## 2.6 Fine-tuning & customization options

| Method | What changes | Cost | When |
|---|---|---|---|
| **Prompt engineering** | Just the prompt | $0 | Default starting point |
| **RAG** | External knowledge | Low | Private/real-time data |
| **Instruction fine-tuning** | Model weights via labeled (prompt, response) pairs | Medium | Specific tone/style/format |
| **Domain-adaptation fine-tuning** | Continue pretraining on domain text | Medium-high | Medical/legal jargon |
| **Continued pre-training** | More unlabeled domain data | High | Highly specialized vocab |
| **Train from scratch** | Everything | Very high | Almost never (use a FM instead) |

### Fine-tuning vs. RAG — quick decision
- Need **new knowledge**? → **RAG**
- Need **new behavior/style**? → **Fine-tune**
- Need both? → **Fine-tune for style + RAG for facts** (common combo)

---

## 2.7 Model performance evaluation

| Metric | For |
|---|---|
| **ROUGE** | Text summarization (recall-oriented) |
| **BLEU** | Translation / generation precision |
| **BERTScore** | Semantic similarity |
| **Perplexity** | How well model predicts text (lower = better) |
| **Human eval** | Tone, helpfulness, safety |
| **BARTScore, METEOR** | Other generation quality |

> 🧠 **Exam trick:** "Evaluate summarization quality automatically" → **ROUGE**. "Evaluate translation quality" → **BLEU**.

---

## 2.8 Agents & tool use (lighter coverage)

- **Agent** = LLM + ability to call **tools/APIs** to take actions.
- Use cases: book a flight, query a database, run a search, call a Lambda function.
- On AWS: **Agents for Amazon Bedrock**.

### Advanced GenAI application patterns
| Pattern | What |
|---|---|
| **RAG** | Retrieve-then-generate |
| **Agentic workflow** | LLM orchestrates multi-step tool calls |
| **Multi-modal** | Text + image + audio (e.g., Titan Image Generator, Claude with vision) |
| **Human-in-the-loop** | LLM drafts, human approves |

---

## 2.9 GenAI vs. traditional ML — final decision aid

| Question | If YES → |
|---|---|
| Need to create new content (text, image, audio, code)? | **GenAI** |
| Need to predict a label / number from structured features? | **Traditional ML** (SageMaker) |
| Need explainability & determinism? | **Traditional ML** |
| Need flexible, conversational, generalized task handling? | **GenAI** |

---

## 🔑 Domain 2 key takeaways

1. **Tokens, context window, temperature** — know cold.
2. **Hallucination + knowledge cutoff** → fix with **RAG**.
3. **Prompt eng → RAG → fine-tune → train from scratch**: increasing cost & effort.
4. **RAG = embeddings + vector DB + LLM**. Vector stores on AWS: OpenSearch Serverless, pgvector, Kendra, MemoryDB.
5. **Evaluation:** ROUGE=summary, BLEU=translation, Perplexity=general.
6. **Agents** = LLM + tools (Bedrock Agents).
7. **GenAI vs. classic ML** by output type (create vs. classify).

---

## ✅ Self-check questions (answers in `06-mock-questions.md`)

1. Customer service bot must give identical answers to identical questions. Which parameter?
2. Internal HR bot over 5,000 PDFs — best customization approach?
3. Evaluate quality of an automated summarization feature. Which metric?
4. Foundation model "doesn't know" events from last month. What limitation is this?
5. Need to build a workflow where an LLM queries a database and books meetings. Which AWS feature?
