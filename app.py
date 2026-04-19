import streamlit as st
import random

st.set_page_config(page_title="LuhVee Mensagens", page_icon="💖")

st.title("💖 LuhVee Stores - Gerador de Mensagens")
st.write("Mensagens prontas para encantar, conectar e vender todos os dias ✨")

# Categorias
periodo = st.selectbox("Escolha o tipo de mensagem:", ["Bom Dia", "Boa Tarde", "Boa Noite"])

quantidade = st.slider("Quantas mensagens gerar?", 1, 200, 10)

# Bancos de frases
aberturas = [
    "✨ Hoje é um novo começo!",
    "💖 Ei, não esquece:",
    "🌸 Um lembrete importante:",
    "🔥 Acorda pra vida que você merece!",
    "💫 Você nasceu pra brilhar!"
]

meio = [
    "você merece coisas incríveis",
    "seu esforço vai valer a pena",
    "coisas boas estão chegando",
    "seu momento está mais perto do que você imagina",
    "você é mais forte do que pensa"
]

final = [
    "💖 Confia no processo.",
    "✨ Vai dar certo!",
    "🔥 Bora pra cima!",
    "🌸 Você consegue!",
    "💫 Nunca desista!"
]

cta = [
    "👉 Aproveita e confere os achadinhos da LuhVee!",
    "🛍️ Já viu as promoções de hoje?",
    "🔥 Corre no link antes que acabe!",
    "💖 Você merece se presentear hoje!",
    ""
]

def gerar_mensagem(periodo):
    if periodo == "Bom Dia":
        saudacao = "☀️ Bom dia!"
    elif periodo == "Boa Tarde":
        saudacao = "🌤️ Boa tarde!"
    else:
        saudacao = "🌙 Boa noite!"

    mensagem = f"{saudacao}\n\n{random.choice(aberturas)} {random.choice(meio)}.\n{random.choice(final)}\n\n{random.choice(cta)}"
    return mensagem

if st.button("✨ Gerar Mensagens"):
    for i in range(quantidade):
        st.text_area(f"Mensagem {i+1}", gerar_mensagem(periodo), height=150)
