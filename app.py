import streamlit as st
import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM

HF_TOKEN = None


if "HUGGINGFACE_HUB_TOKEN" in st.secrets:
    HF_TOKEN = st.secrets["HUGGINGFACE_HUB_TOKEN"]
else:
    
    HF_TOKEN = os.environ.get("HUGGINGFACE_HUB_TOKEN")

AGENT_NAME = "MindCare"
MODEL_NAME = "google/gemma-2b-it"

SYSTEM_PROMPT = (
    "You are a calm, empathetic mental health companion. "
    "You listen without judgment and respond gently. "
    "You do NOT diagnose, prescribe medicine, or give medical advice. "
    "If the user expresses severe distress, self-harm, or suicidal thoughts, "
    "encourage them to seek professional help or talk to a trusted person. "
    "Keep replies short (2–5 sentences), supportive, and reassuring."
)

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        token=HF_TOKEN
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        token=HF_TOKEN,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    return model, tokenizer, device


model, tokenizer, device = load_model()

st.set_page_config(page_title="MindCare")
st.title("🧠 MindCare")
st.caption("A gentle mental health companion (not a replacement for professional help).")

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
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    messages = [
        {"role": "user", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": ""},
        {"role": "user", "content": user_input},
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(device)

    prompt_len = prompt.shape[-1]

    with torch.no_grad():
        output = model.generate(
            prompt,
            max_new_tokens=150,
            do_sample=False
        )

    reply_ids = output[0][prompt_len:]
    reply = tokenizer.decode(reply_ids, skip_special_tokens=True).strip()

    if not reply:
        reply = "I’m here with you. Take your time."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
