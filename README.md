<div align="center">

# 🤖 CodeAlpha — Artificial Intelligence Internship

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-FF6B35?style=for-the-badge)
![NLTK](https://img.shields.io/badge/NLTK-NLP-4CAF50?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Desktop%20GUI-FF9800?style=for-the-badge)
![Status](https://img.shields.io/badge/Internship-Completed-brightgreen?style=for-the-badge)

**Completed by Pranav · BBACA Graduate · Modern College of Arts, Science & Commerce, Pune**

*"The best way to learn AI is to build something with it."*

</div>

---

## 📋 Table of Contents

- [About This Internship](#-about-this-internship)
- [Task Summary](#-task-summary)
- [Task 1 — Language Translation Tool](#-task-1--language-translation-tool)
- [Task 2 — FAQ Chatbot · ARIA](#-task-2--faq-chatbot--aria)
- [Task 4 — Object Detection & Tracking · TITAN](#-task-4--object-detection--tracking--titan)
- [Setup & Installation](#-setup--installation)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [What I Learned](#-what-i-learned)
- [Acknowledgements](#-acknowledgements)
- [Contact](#-contact)

---

## 🏢 About This Internship

This repository contains my completed AI projects for the **CodeAlpha Artificial Intelligence Internship** — a program focused on building real-world AI applications using Python.

Each project covers a distinct domain of AI:

| Domain | Project |
|--------|---------|
| Natural Language Processing | FAQ Chatbot — ARIA |
| Translation Systems | Language Translation Tool |
| Computer Vision & Deep Learning | Object Detection — TITAN |
| Desktop Application Development | All three projects use Tkinter |

---

## ✅ Task Summary

| Task | Project | Status |
|------|---------|--------|
| Task 1 | Language Translation Tool | ✅ Completed |
| Task 2 | FAQ Chatbot — **ARIA** | ✅ Completed |
| Task 3 | Music Generation with AI | ⏭ Skipped |
| Task 4 | Object Detection & Tracking — **TITAN** | ✅ Completed |

> **Certificate requirement:** Minimum 2 tasks completed. ✅

---

## 🌐 Task 1 — Language Translation Tool

### What is it?

A desktop translation application built entirely in Python — a self-contained mini Google Translate with no paid API key required.

### How It Works

```
┌─────────────────────────────────────────────────────┐
│                   User enters text                  │
└─────────────────────────┬───────────────────────────┘
                          │
              ┌───────────▼────────────┐
              │  Select source lang    │  ← Auto-detect supported
              │  Select target lang    │  ← 20+ languages
              └───────────┬────────────┘
                          │
              ┌───────────▼────────────┐
              │   deep-translator      │
              │  (Google Translate     │
              │   engine — free)       │
              └───────────┬────────────┘
                          │
              ┌───────────▼────────────┐
              │  Translated text       │
              │  displayed instantly   │
              └────────────────────────┘
```

### Features

| Feature | Description |
|---------|-------------|
| 🌍 20+ Languages | Hindi, French, Spanish, Japanese, Arabic, German & more |
| 🔍 Auto-detect | Detects source language automatically |
| ⇄ Swap | One-click swap between source and target |
| 📋 Copy | Copy translated output to clipboard |
| 🗑 Clear | Clear both panels in one click |
| 📊 Status bar | Shows translation result live |
| 🌙 Dark UI | Modern dark-themed Tkinter interface |

### UI Layout

```
┌──────────────────────────────────────────────────────┐
│  🌐  Language Translation Tool    CodeAlpha Task 1   │
│  ────────────────────────────────────────────────── │
│                                                      │
│   From  [ Auto Detect      ▼ ]  ⇄  To  [ Hindi ▼ ] │
│                                                      │
│   ┌───────────────────┐   ┌───────────────────┐      │
│   │  Enter text...    │   │  Translation...   │      │
│   │                   │   │                   │      │
│   │                   │   │                   │      │
│   └───────────────────┘   └───────────────────┘      │
│                                                      │
│      [ Translate ➜ ]   [ 📋 Copy ]   [ 🗑 Clear ]    │
│   ✅  Translated: English → Hindi                    │
└──────────────────────────────────────────────────────┘
```

### Technologies

| Library | Purpose |
|---------|---------|
| Python | Core language |
| Tkinter | Desktop GUI |
| deep-translator | Google Translate engine (free, no API key) |

---

## 🤖 Task 2 — FAQ Chatbot · ARIA

> **ARIA** = **A**I **R**esearch & **I**nformation **A**ssistant

### What is it?

A desktop chatbot that answers technical questions across 10+ domains using NLP-powered semantic matching — not keyword matching. ARIA understands the *meaning* of your question, then routes it through a dual-layer intelligence system.

### Dual-Layer Architecture

```
                        User Question
                             │
             ┌───────────────▼────────────────┐
             │         LAYER 1 — FAQ Bank      │
             │   200 Q&A pairs across 10 domains│
             │   TF-IDF Vectorization (bigrams) │
             │   + Cosine Similarity matching   │
             └───────────────┬────────────────┘
                             │
                  ┌──────────▼──────────┐
                  │   Score ≥ 0.20 ?    │
                  └────┬────────────────┘
                       │
           ┌───────────┴───────────────┐
           │ YES                       │ NO (low confidence)
           ▼                           ▼
   ┌──────────────┐          ┌──────────────────────┐
   │   FAQ Bank   │          │   LAYER 2 — Claude   │
   │   Answer     │          │   AI API (dynamic)   │
   │   [FAQ ✓]    │          │   [Claude AI ✨]     │
   │   (instant)  │          │   (any tech question)│
   └──────────────┘          └──────────────────────┘
```

### NLP Pipeline — Step by Step

```
User Input: "how does ML work?"
     │
     ▼
Step 1 — Preprocessing (NLTK)
     lowercase → remove punctuation → remove stopwords → stem
     "how does ML work?" ──► "ml work"
     │
     ▼
Step 2 — TF-IDF Vectorization (Scikit-learn, bigrams)
     Converts text into a weighted numerical vector
     TF  = how often a word appears in this question
     IDF = how rare the word is across all 200 FAQs
     │
     ▼
Step 3 — Cosine Similarity
     Compare user vector against all 200 FAQ vectors
     Score 1.0 = identical meaning
     Score 0.0 = completely unrelated
     │
     ▼
Step 4 — Routing Decision
     Score ≥ 0.20 → FAQ answer    [FAQ ✓]  green badge
     Score < 0.20 → Claude API    [AI ✨]   teal  badge
```

### Knowledge Base — 200 FAQs · 10 Domains

| Domain | Example Questions |
|--------|-------------------|
| 🤖 AI & ML | What is deep learning? What is overfitting? |
| 🐍 Python | What is list comprehension? What is a decorator? |
| 🗄️ SQL & Databases | What is a JOIN? What is ACID? What is normalization? |
| ☕ Java | What is the JVM? What is multithreading in Java? |
| 🌐 Web Dev | What is REST API? What is the DOM? What is React? |
| 💡 LLMs & Gen AI | What is ChatGPT? What is RAG? How do LLMs work? |
| ☁️ Cloud & DevOps | What is Docker? What is Kubernetes? What is CI/CD? |
| 🔗 Networking | TCP vs UDP? What is DNS? What is HTTP? |
| 🔒 Cybersecurity | What is SQL injection? What is encryption? |
| 💻 DSA | What is Big O notation? What is a hash table? |

### UI Layout

```
┌──────────────────────────────────────────────┐
│  🤖  ARIA — FAQ Chatbot    CodeAlpha Task 2  │
│  ──────────────────────────────────────────  │
│                                              │
│  ARIA                                        │
│  👋 Hi! I'm ARIA — AI Research &             │
│  Information Assistant.                      │
│  Ask me anything about AI, ML, Python,       │
│  SQL, Java, Web Dev, Cloud & more!           │
│                                              │
│  You                                         │
│  what is machine learning                    │
│                                              │
│  ARIA  [FAQ ✓]  🤖 AI / ML                  │
│  Machine Learning is a subset of AI          │
│  where systems learn from data without       │
│  being explicitly programmed...              │
│                                              │
│  You                                         │
│  explain binary search trees                 │
│                                              │
│  ARIA  [Claude AI ✨]  💬 General Tech       │
│  A Binary Search Tree stores nodes where     │
│  left child < parent < right child...        │
│                                              │
│  ──────────────────────────────────────────  │
│  [ Type your question here... ] [Send ➜][🗑] │
│  FAQ Bank: 200 Q&As  |  Claude AI fallback   │
└──────────────────────────────────────────────┘
```

### Technologies

| Library | Purpose |
|---------|---------|
| Python | Core language |
| NLTK | Tokenization, stopword removal, stemming |
| Scikit-learn | TF-IDF vectorizer + cosine similarity |
| Anthropic API | Claude AI fallback for unknown questions |
| Tkinter | Dark-themed chat interface |

---

## 🎯 Task 4 — Object Detection & Tracking · TITAN

> **TITAN** = **T**racking & **I**dentification **T**echnology for **A**utonomous **N**etworks

### What is it?

A real-time AI object detection and tracking system. Point your webcam at anything — TITAN detects and tracks every object it sees using YOLOv8 and assigns persistent IDs that follow objects across frames.

### How It Works

```
┌──────────────────────────────────────────────────────┐
│              Webcam  /  Video File                   │
└────────────────────────┬─────────────────────────────┘
                         │  frame-by-frame
                         ▼
┌──────────────────────────────────────────────────────┐
│                    YOLOv8 Model                      │
│                                                      │
│  Divides frame into a grid                           │
│  Each cell predicts: object class + bounding box     │
│                     + confidence score               │
│                                                      │
│  Detects 80 COCO object classes:                     │
│  person, phone, laptop, car, bottle, chair...        │
└────────────────────────┬─────────────────────────────┘
                         │  detected boxes + scores
                         ▼
┌──────────────────────────────────────────────────────┐
│                   ByteTrack                          │
│                                                      │
│  Matches detections across frames using IoU          │
│  Assigns a persistent tracking ID to each object     │
│  Same object keeps same ID even if briefly hidden    │
└────────────────────────┬─────────────────────────────┘
                         │  labeled + tracked frame
                         ▼
┌──────────────────────────────────────────────────────┐
│               OpenCV Display Window                  │
│                                                      │
│  Bounding box with corner accents per object         │
│  Badge: #ID  ClassName  Confidence%                  │
│  HUD overlay: FPS · Object count · Model · Controls  │
└──────────────────────────────────────────────────────┘
```

### What Gets Detected — 80 COCO Classes

```
People      →  person
Vehicles    →  car, motorcycle, bus, truck, bicycle
Electronics →  laptop, phone, TV, keyboard, mouse
Furniture   →  chair, sofa, bed, dining table
Kitchen     →  bottle, cup, fork, knife, bowl
Animals     →  cat, dog, bird, horse
Outdoors    →  traffic light, stop sign, umbrella
Sports      →  ball, skateboard, tennis racket
             +  many more...
```

### Model Options

| Model | File | Speed | Accuracy |
|-------|------|-------|----------|
| YOLOv8 Nano | yolov8n.pt | ⚡ Fastest | Good |
| YOLOv8 Small | yolov8s.pt | ⚡⚡ Fast | Better |
| YOLOv8 Medium | yolov8m.pt | ⚡⚡⚡ Moderate | Best |

> All model weights (~6–50 MB) auto-download from Ultralytics on first run.

### Detection Window — On-Screen Elements

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│    ┌─────────────────────────────────┐                   │
│    │ #1  person 94%                  │ ← label badge     │
│    ├  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ┤ ← corner accents  │
│    │                                 │                   │
│    │        [person detected]        │ ← bounding box    │
│    │                                 │                   │
│    ├  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ┤                   │
│    └─────────────────────────────────┘                   │
│                                                          │
│   ┌──────────────────────────┐   ← HUD (top-right)       │
│   │ FPS    :  29.8           │                           │
│   │ Objects:    3            │                           │
│   │ Model  : YOLOV8N        │                           │
│   │ [ P ] Pause  [ Q ] Quit │                           │
│   └──────────────────────────┘                           │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Keyboard Controls

| Key | Action |
|-----|--------|
| `P` | Pause / Resume detection |
| `Q` | Quit detection window |

### Control Panel Layout

```
┌──────────────────────────────────────────────┐
│  🎯  TITAN          CodeAlpha AI Task 4      │
│  ──────────────────────────────────────────  │
│                                              │
│  📹  Video Source                            │
│    ◉  Webcam  (index 0)                      │
│    ○  Video File                [Browse…]    │
│                                              │
│  🧠  YOLO Model                              │
│    [ YOLOv8 Nano (fastest)              ▼ ] │
│                                              │
│  🎚️  Confidence Threshold                   │
│    [━━━━━━━━━━━━━━━━━━━━━━━━━━━━━]  0.45    │
│                                              │
│  📊  Live Stats                              │
│  ┌──────────┬──────────┬───────────┐         │
│  │   FPS    │ Objects  │  Status   │         │
│  │   29.4   │    4     │  Running  │         │
│  └──────────┴──────────┴───────────┘         │
│                                              │
│   [▶  Start Detection]   [■  Stop]           │
│  ──────────────────────────────────────────  │
│   [ P ] Pause / Resume   [ Q ] Quit          │
└──────────────────────────────────────────────┘
```

### Technologies

| Library | Purpose |
|---------|---------|
| Python | Core language |
| YOLOv8 (Ultralytics) | Real-time object detection |
| ByteTrack | Persistent object ID tracking across frames |
| OpenCV | Video capture, frame processing, display |
| NumPy | Array math for drawing operations |
| Tkinter | Desktop control panel UI |

---

## ⚙️ Setup & Installation

### Prerequisites

- Python **3.9** or higher
- `pip`
- Internet connection *(model weights + NLTK data auto-download on first run)*

### Install All Dependencies

```bash
pip install deep-translator nltk scikit-learn ultralytics opencv-python numpy anthropic
```

### API Key (Task 2 only — for Claude AI fallback)

```bash
# Windows
set ANTHROPIC_API_KEY=sk-ant-...

# Mac / Linux
export ANTHROPIC_API_KEY=sk-ant-...
```

> Get a free key at: [console.anthropic.com](https://console.anthropic.com)  
> Without a key, ARIA still works — it uses the FAQ bank for all answers.

---

## ▶️ How to Run

**Task 1 — Language Translation Tool**
```bash
cd CodeAlpha_LanguageTranslation
python translator.py
```

**Task 2 — FAQ Chatbot (ARIA)**
```bash
cd CodeAlpha_FAQChatbot
python chatbot.py
```
> NLTK data downloads automatically on first launch (~2 sec).

**Task 4 — Object Detection & Tracking (TITAN)**
```bash
cd CodeAlpha_ObjectDetection
python detector.py
```
> YOLOv8 weights auto-download on first launch. Select model in UI, click **Start Detection**.

---

## 📁 Project Structure

```
CodeAlpha-AI-Internship/
│
├── CodeAlpha_LanguageTranslation/
│   ├── translator.py          ← run this
│   └── requirements.txt
│
├── CodeAlpha_FAQChatbot/
│   ├── chatbot.py             ← run this
│   ├── faqs.py                ← 200 Q&A knowledge base
│   └── requirements.txt
│
├── CodeAlpha_ObjectDetection/
│   ├── detector.py            ← run this
│   └── requirements.txt
│
└── README.md
```

---

## 📚 What I Learned

### 🧠 NLP — Task 2

```
Raw text  ──►  Preprocessing  ──►  TF-IDF vector  ──►  Cosine score  ──►  Answer
"how ML?"      lowercase            200-dim               ≥ 0.20?          FAQ
               stopwords            bigrams               < 0.20?          Claude AI
               stemming
```

- Text preprocessing pipeline: tokenization → stopwords → stemming
- Why TF-IDF captures importance, not just frequency
- How cosine similarity measures semantic closeness regardless of text length
- When to use retrieval (FAQ) vs generation (Claude AI) — and how to combine both

### 👁️ Computer Vision — Task 4

```
Frame  ──►  YOLO grid  ──►  Box predictions  ──►  ByteTrack  ──►  Display
image       NxN cells       class + conf          IoU match       annotated
            each predicts   bounding box          persistent ID   frame
```

- How YOLO divides a frame into a grid and predicts multiple boxes per cell
- What confidence threshold does and how tuning it affects detection sensitivity
- How ByteTrack uses Intersection over Union (IoU) to match detections across frames
- Trade-offs between Nano (speed) vs Medium (accuracy) model sizes
- Threading — keeping the Tkinter UI responsive while OpenCV runs on a background thread

### 🐍 Python & Software Engineering

- OOP — separating `DetectionSession` from `ControlPanel` with clean callbacks
- Threading with `daemon=True` and `root.after()` for safe UI updates
- `try/except ImportError` pattern for graceful dependency handling
- Structuring a multi-file project for clean GitHub submission

---

## 🙏 Acknowledgements

- **[CodeAlpha](https://codealpha.tech)** — for the internship opportunity and well-structured task list
- **[Ultralytics](https://ultralytics.com)** — for YOLOv8, the cleanest object detection API available
- **[Anthropic](https://anthropic.com)** — for Claude AI powering ARIA's dynamic fallback
- **[NLTK Team](https://nltk.org)** — for the NLP toolkit behind ARIA's preprocessing
- **[Scikit-learn](https://scikit-learn.org)** — for TF-IDF and cosine similarity

---

## 📬 Contact

**Pranav**
BBACA Graduate
Modern College of Arts, Science and Commerce, Pune-16

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

---

<div align="center">

Built with 🧠 + ☕ during the **CodeAlpha AI Internship**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Open to Opportunities](https://img.shields.io/badge/Status-Open%20to%20Opportunities-brightgreen?style=flat-square)

</div>
