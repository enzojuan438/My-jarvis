import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="J.A.R.V.I.S.", page_icon="🤖")

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>O assistente do Tony Stark</p>", unsafe_allow_html=True)

# Troque o texto entre as aspas pela sua chave que começa com AIza
API_KEY = "AQ.Ab8RN6LwshWXwhpTSLni4l-KJgZvlwERSJLFAHh-oy_EfnkUtw"

if API_KEY == "COLE_SUA_CHAVE_AQUI":
    st.warning("Coloque sua chave de API no código!")
else:
    genai.configure(api_key=API_KEY)
    instrucoes = "Você é o J.A.R.V.I.S., o assistente do Tony Stark. Seja educado, britânico e chame o usuário de Senhor."
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instrucoes)

    comando = st.text_input("Diga algo para o Jarvis:")

    if comando:
        with st.spinner("Processando..."):
            response = model.generate_content(comando)
            st.write(f"🤖 J.A.R.V.I.S.: {response.text}")
            
