import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="J.A.R.V.I.S. - Enzo Enzo Aura", page_icon="🤖")

# Título do Jarvis
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>O assistente virtual do Tony Stark</p>", unsafe_allow_html=True)

# Sua assinatura oficial e imutável na tela
st.markdown("<div style='text-align: center; border: 1px solid #ff4b4b; padding: 10px; border-radius: 5px; margin-bottom: 20px;'><b style='color: #ff4b4b;'>⚙️ Criador & Proprietário:</b> <span style='color: #fff;'>Enzo Enzo Aura</span></div>", unsafe_allow_html=True)

# SISTEMA DE SEGURANÇA ANTIXERETA: Puxa a chave do cofre oculto do site
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
elif "gemini" in st.secrets:
    API_KEY = st.secrets["gemini"]["api_key"]
else:
    API_KEY = None

if not API_KEY:
    st.error("🔒 Erro de Autenticação: Sistema de segurança ativado. Chave não encontrada no cofre.")
else:
    genai.configure(api_key=API_KEY)
    instrucoes = "Você é o J.A.R.V.I.S., o assistente do Tony Stark. Seja educado, britânico, use termos cibernéticos e chame o usuário de Senhor."
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instrucoes)

    comando = st.text_input("Diga algo para o Jarvis:")

    if comando:
        with st.spinner("Processando criptografia..."):
            response = model.generate_content(comando)
            st.write(f"🤖 J.A.R.V.I.S.: {response.text}")
