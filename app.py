
import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Personal Assistant AI", page_icon="🤖")
st.title("🤖 My Simple Chatbot")
st.write("Projek Akhir - Data Science Training")

# Input API Key dari Sidebar
api_key = st.sidebar.text_input("Masukkan Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ada yang bisa saya bantu?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Tambahkan karakter unik di sini sesuai instruksi materi
            full_prompt = f"Berikan jawaban yang edukatif dan ramah: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)

        st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Silakan masukkan API Key di sidebar untuk memulai.")
