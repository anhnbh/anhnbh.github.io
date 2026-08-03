# Domain 1 — Fundamentals of AI and ML (20%)

> **What AWS tests:** Can you define core AI/ML terms, identify the right type of ML for a problem, and map stages of the ML development lifecycle to business objectives?

---

## 1.1 AI vs. ML vs. Deep Learning — the hierarchy

```
Artificial Intelligence (AI)          ← broadest: machines doing "smart" things
   └── Machine Learning (ML)          ← learn patterns from data (no explicit programming)
        └── Deep Learning (DL)        ← ML with multi-layer neural networks
            └── Generative AI (GenAI) ← DL that creates NEW content (text, image, audio)
```

| Term | One-liner | Example |
|---|---|---|
| **AI** | Software that mimics human intelligence | Chess bot, recommendation system |
| **ML** | Algorithms that learn from data | Spam classifier |
| **DL** | ML using neural networks with many layers | Face recognition |
| **GenAI** | AI that *generates* new content | ChatGPT, Claude, Stable Diffusion |

> 🧠 **Exam trick:** "Predicting churn from historical data" = ML. "Writing a new marketing email" = GenAI. Don't confuse the two.

---

## 1.2 Types of Machine Learning

### **Supervised Learning** — labeled data
- Data comes in **(input, label)** pairs.
- Goal: learn a function `f(input) → label`.
- **Examples:** spam detection (spam/not-spam), house price prediction, image classification.
- **Algorithms:** Linear/Logistic Regression, Decision Trees, Random Forest, XGBoost, Neural Networks.

### **Unsupervised Learning** — unlabeled data
- No labels; algorithm finds structure.
- **Examples:** customer segmentation, anomaly detection, topic discovery.
- **Algorithms:** K-Means clustering, PCA, DBSCAN.

### **Reinforcement Learning (RL)** — learn by reward
- Agent takes actions in an environment; gets rewards/penalties.
- **Examples:** game-playing AIs, robotics, recommendation tuning.
- **Algorithms:** Q-Learning, Deep Q-Network (DQN).

| Type | Data | Use case trigger words |
|---|---|---|
| Supervised | Labeled | "predict", "classify", "labeled dataset" |
| Unsupervised | Unlabeled | "group", "segment", "cluster", "find patterns" |
| Reinforcement | Reward signal | "agent", "reward", "policy", "game", "robot" |

> 🧠 **Exam trick:** If the question mentions "**labeled**" + "**predict a category/value**" → supervised. "**Group similar customers**" → unsupervised (clustering).

---

## 1.3 ML development lifecycle (6 stages)

```
1. Business problem framing   → "What are we predicting? Why?"
2. Data collection            → gather raw data
3. Data preparation / EDA     → clean, transform, feature engineering
4. Model training             → algorithm learns from data
5. Model evaluation           → measure performance (accuracy, F1, etc.)
6. Deployment & monitoring    → serve predictions, watch for drift
```

### Key sub-concepts
- **Feature:** an individual measurable property (column). E.g., "age", "purchase_count".
- **Feature engineering:** transforming raw data into useful features.
- **Training set vs. validation set vs. test set:** split data so the model doesn't memorize.
- **Inference:** using the trained model to make predictions on new data.
  - **Real-time (online) inference** — low-latency, single request.
  - **Batch inference** — process large datasets offline.
- **Model drift:** performance degrades over time because real-world data changed → retrain.

> 🧠 **Exam trick:** "Model accuracy dropped 3 months after deployment" → **model drift** → retrain with fresh data.

### Performance metrics cheat list
| Problem type | Common metric |
|---|---|
| Classification | Accuracy, Precision, Recall, F1, AUC-ROC |
| Regression | MSE, RMSE, MAE |
| Imbalanced classes | Use F1/AUC, not raw accuracy |

---

## 1.4 Inferencing: choosing inference type

| Need | Pick |
|---|---|
| Sub-second latency, single user request | **Real-time / online inference** |
| Process millions of rows overnight | **Batch inference** |
| Sporadic traffic, cost-sensitive | **Serverless / asynchronous inference** |
| Need GPU, low latency, autoscaling | **Real-time endpoint** (SageMaker) |

---

## 1.5 AWS services for traditional ML (NOT GenAI)

These services are for "classic" ML/feature tasks — exam loves to test the distinction:

| Service | What it does | Trigger words in question |
|---|---|---|
| **Amazon SageMaker** | End-to-end ML platform (build, train, deploy) | "train custom model", "MLOps", "Jupyter" |
| **SageMaker JumpStart** | Pre-trained models + 1-click deploy | "quickly deploy pretrained model" |
| **SageMaker Canvas** | No-code ML for business analysts | "no code", "business user", "drag-and-drop" |
| **SageMaker Ground Truth** | Data labeling (human labelers) | "label dataset", "annotators" |
| **SageMaker Feature Store** | Central repository for features | "share features across teams" |
| **Amazon Comprehend** | NLP: sentiment, key phrases, entities, PII | "extract sentiment from text" |
| **Amazon Rekognition** | Image/video analysis (faces, objects, moderation) | "detect objects in image", "moderate content" |
| **Amazon Transcribe** | Speech-to-text | "convert audio to text" |
| **Amazon Polly** | Text-to-speech | "convert text to lifelike speech" |
| **Amazon Lex** | Conversational chatbots (same tech as Alexa) | "build chatbot", "voice bot" |
| **Amazon Translate** | Language translation | "translate documents" |
| **Amazon Textract** | OCR — extract text from scanned docs | "extract text from PDF/forms" |
| **Amazon Personalize** | Real-time recommendations | "movie/product recommendations" |
| **Amazon Forecast** | Time-series forecasting | "predict demand/sales over time" |
| **Amazon Fraud Detector** | Online fraud detection | "detect fraudulent transactions" |
| **Amazon Kendra** | Enterprise search (natural language) | "enterprise search across documents" |
| **AWS HealthScribe** | Generate clinical notes from doctor-patient audio | "clinical documentation", "medical transcription" |

> 🧠 **Exam trick — service shortcut table.** Almost every Domain 1 question is "match use case → service". Memorize the **trigger words** column above; that's 80% of the battle.

---

## 1.6 Business problem → ML problem (framing)

The exam often gives a business sentence and asks how to frame it as ML:

| Business problem | ML framing |
|---|---|
| "Reduce customer churn" | Binary classification: will customer X leave in 30 days? |
| "Recommend products" | Recommendation system (collaborative filtering) |
| "Detect defective parts on assembly line" | Image classification (defect/no-defect) |
| "Forecast next quarter sales" | Time-series regression |
| "Sort support tickets by urgency" | Multiclass classification or NLP (Comprehend) |

**Steps to frame:**
1. Define the **target variable** (what to predict).
2. Define the **prediction horizon** (when).
3. Define **success metric** (business value + ML metric).
4. Confirm data availability.

---

## 🔑 Domain 1 key takeaways

1. AI ⊃ ML ⊃ DL ⊃ GenAI — know the hierarchy.
2. **Supervised (labeled) / Unsupervised (cluster) / RL (reward)** — pick by trigger words.
3. **ML lifecycle = 6 stages.** "Drift" = retrain signal.
4. **Inference type**: real-time (low-latency) vs. batch (offline bulk).
5. **Know AWS classic-AI services cold** — Comprehend, Rekognition, Transcribe, Polly, Lex, Textract, Personalize, Forecast, Kendra, HealthScribe. Match by **trigger words**.
6. GenAI services (Bedrock, Q, Titan) are tested in **Domains 2 & 3** — don't confuse them with the classic ML services above.

---

## ✅ Self-check questions (answers in `06-mock-questions.md`)

1. A company wants to group customers by purchasing behavior without predefined categories. Which ML type?
2. "Detect PII in scanned contracts." Which single AWS service?
3. A model's accuracy dropped from 92% to 78% six months post-deployment. What happened, and what's the fix?
4. Real-time fraud detection on card swipes — which inference type?
5. "Convert a 1-hour patient-doctor conversation into structured clinical notes." Which AWS service?
