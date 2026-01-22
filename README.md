# 🧠 MindCare – A Gentle Mental Health Companion

MindCare is a web-based AI mental health companion designed to provide **empathetic, supportive conversations** for users who want someone to talk to.
It is **not a replacement for professional help**, but a gentle first step toward emotional expression and self-reflection.

🔗 **Live App:**
[https://mindcare-ai-anzacddipscws7hkh8drlg.streamlit.app/](https://mindcare-ai-anzacddipscws7hkh8drlg.streamlit.app/)

---

## 🚩 Problem Statement

Many people experience emotional stress, tiredness, or loneliness but hesitate to seek professional help due to stigma, lack of accessibility, or fear of judgment. There is a need for a safe, non-judgmental, and easily accessible mental health companion.

---

## 💡 Solution

MindCare acts as a calm, empathetic listener that:

* Responds gently and supportively
* Maintains conversational context
* Avoids diagnosis or medical advice
* Encourages seeking professional help when necessary

The system is designed to feel **human-like**, simple, and emotionally safe.

---

## 🛠 Tech Stack

* **Frontend & UI:** Streamlit
* **AI Model:** Google Gemma (via Hugging Face Inference API)
* **Backend Logic:** Python
* **Deployment:** Streamlit Cloud

---

## ⚙️ System Architecture

1. User enters a message via the Streamlit chat interface
2. Recent conversation history is combined with a predefined empathetic system prompt
3. The prompt is sent to Hugging Face Inference API
4. The AI generates a context-aware response
5. The response is displayed and stored in session memory

This approach avoids heavy local model loading and ensures cloud reliability.

---

## 🚀 Features

* Conversational memory to avoid repetitive replies
* Empathetic, non-judgmental responses
* Clean and calming UI
* Cloud-safe deployment
* Lightweight and fast response time

---

## ⚠️ Disclaimer

> MindCare is **not a substitute for professional mental health care**.
> If you are experiencing severe distress, self-harm thoughts, or a mental health emergency, please seek help from a qualified professional or a trusted person immediately.

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/Golixco/mindcare-ai.git
cd mindcare-ai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Setup

Create a Hugging Face token and add it as a secret:

### Streamlit Cloud Secrets

```toml
HUGGINGFACE_HUB_TOKEN="hf_your_token_here"
```

---

## 📈 Results

* Successfully delivers emotionally supportive and context-aware responses
* Runs reliably on cloud infrastructure
* Provides a safe and accessible mental health companion experience

---

## 🔮 Future Scope

* Crisis detection with region-based helplines
* Daily mood tracking and emotional journaling
* Conversation export (PDF / TXT)
* Multilingual support
* Enhanced personalization

---

## 📚 References

* Streamlit Documentation
* Hugging Face Inference API Documentation
* Google Gemma Model
* WHO Digital Mental Health Guidelines

---

## 👤 Author

**Rohan Sonu Bablani** (Golixco)

--- 

Thanks 
This was a Capstone Project to Edunet Foundation

