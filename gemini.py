import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def gerar_ideia():

    prompt = "Crie uma ideia, resumida a 2 ou 3 palavras, (que não esteja entre essas: pular de paraquedas, ler 20 livros, viajar de avião, visitar 5 cidades do Brasil, ter filhos, amar de verdade, fazer uma aula de dança, realizar um sonho com alguém, viajar para o exterior, cozinhar uma comida só para você, partivipar de um campeonato, ir ao show de um cantor que você ama), de meta para uma lista de coisas para fazer antes de morrer."

    resposta = model.generate_content(prompt)

    return resposta.text

st.subheader("Gerar meta com IA!")
if st.button("Gerar ideia com IA"):

    ideia = gerar_ideia()

    st.success(ideia)
