import streamlit as st
import google.generativeai as genai

# Configuração visual do site (Tema Escuro do Homem de Ferro)
st.set_page_config(page_title="J.A.R.V.I.S.", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>O assistente virtual do Tony Stark, direto no seu celular.</p>", unsafe_allow_html=True)

# Aqui você vai colocar a sua chave secreta que salvou no bloco de notas
API_KEY = "AQ.Ab8RN6LwshWXwhpTSLni4l-KJgZvlwERSJLFAHh-oy_EfnkUtw"

if API_KEY == "COLE_SUA_CHAVE_AQUI":
    st.warning("⚠️ Atenção: Você precisa colocar a sua Chave de API do Gemini no código para o Jarvis funcionar!")
else:
    # Liga o cérebro do Jarvis
    genai.configure(api_key=API_KEY)
    # Dá a personalidade do Jarvis para a IA
    instrucoes = "Você é o J.A.R.V.I.S., o assistente virtual do Tony Stark. Seja extremamente educado, britânico, chame o usuário de 'Senhor' (ou 'Sra.') e use termos técnicos de forma inteligente. Suas respostas devem ser curtas e diretas."
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instrucoes)

    # Caixa para o usuário digitar ou usar o microfone do teclado do celular
    comando = st.text_input("Diga algo para o Jarvis (você pode usar o microfone do seu teclado):", placeholder="Ex: Jarvis, qual o plano para hoje?")

    if comando:
        with st.spinner("Processando dados, Senhor..."):
            try:
                response = model.generate_content(comando)
                st.markdown(f"<h3>🤖 J.A.R.V.I.S.:</h3> <p style='font-size:18px;'>{response.text}</p>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro nos sistemas, 
