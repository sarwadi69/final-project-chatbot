import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Chatbot Final Project", page_icon="🤖")
st.title("🤖 My AI Assistant")

api_key = st.sidebar.text_input("Masukkan Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Mencoba menggunakan gemini-1.5-flash sebagai pilihan utama
        # Ganti baris model yang lama dengan ini:
        model = genai.GenerativeModel('gemini-pro')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Apa yang ingin kamu tanyakan?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                try:
                    # Menambahkan pesan sistem sederhana
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Terjadi kesalahan saat generate konten: {e}")
                    
    except Exception as e:
        st.error(f"Konfigurasi API gagal: {e}")
else:
    st.info("Silakan masukkan API Key di sidebar.")
