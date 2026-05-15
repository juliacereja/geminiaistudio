import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def responder_pergunta():

    prompt = st.text_input("Digite sua pergunta:")

    resposta = model.generate_content(prompt)

    return resposta.text

st.subheader("Faça uma pergunta a IA")
if st.button("Perguntar"):

    if prompt:

        resposta = model.generate_content(prompt)

        st.success(resposta.text)

    else:
        st.warning("Digite uma pergunta.")
