import streamlit as st
import requests
import os

HF_TOKEN = st.secrets.get(
    "HUGGINGFACE_HUB_TOKEN",
    os.environ.get("HUGGINGFACE_HUB_TOKEN")
)

API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

SYSTEM_PROMPT = (
    "You are a calm, empathetic mental health companion. "
    "You listen without judgment and respond gently. "
    "You do NOT diagnose, prescribe medicine, or give medical advice. "
    "If the user expresses severe distress, self-harm, or suicidal thoughts, "
    "encourage them to seek professional help or talk to a trusted person. "
    "Keep replies short (2–5 sentences), supportive, and reassuring."
)

def generate_reply(user_input: str) -> str:
    payload = {
        "inputs": f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:",
        "parameters": {
            "max_new_tokens": 120,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()

    except Exception:
        return (
            "I’m here with you. If something feels heavy right now, "
            "you don’t have to face it alone."
        )

    return "I’m here with you. Please tell me more."

st.set_page_config(page_title="MindCare", page_icon="🧠")

st.title("🧠 MindCare")
st.caption("A gentle mental health companion (not a replacement for professional help).")

st.warning(
    "⚠️ This app is not a substitute for professional mental health care. "
    "If you are in immediate distress or thinking about self-harm, "
    "please contact a trusted person or a mental health professional."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi, I’m here to listen. 🌱\n\n"
                "You can start by answering this (only if you want):\n"
                "- Have you been feeling emotionally overwhelmed lately?\n"
                "- Is there any past experience or trauma that still affects you?\n\n"
                "Or simply tell me how you’re feeling right now."
            )
        }
    ]


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type how you're feeling...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    reply = generate_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.write(reply)

