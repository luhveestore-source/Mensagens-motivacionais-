import streamlit as st
import random

st.title("💖 LuhVee - Gerador de Mensagens Infinitas")

# 🔗 SEUS LINKS
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_HUB = "https://hublinks-app.streamlit.app"

periodo = st.selectbox("Tipo:", ["Bom Dia", "Boa Tarde", "Boa Noite"])
quantidade = st.slider("Quantidade:", 1, 500, 20)

# 🧠 EMOÇÃO + DESEJO + CONEXÃO
aberturas = [
    "✨ Hoje pode ser o dia da sua virada...",
    "💖 Tem coisa boa chegando pra você...",
    "🌸 Não ignora isso aqui...",
    "🔥 Você merece muito mais do que imagina...",
    "💫 Isso aqui pode mudar seu dia..."
]

meio = [
    "imagine encontrar algo que combina com você",
    "coisas assim somem rápido",
    "muita gente já está aproveitando",
    "isso chama atenção de verdade",
    "você vai gostar disso"
]

fechamento = [
    "💖 Confia no processo.",
    "✨ Não deixa pra depois.",
    "🔥 Pode ser sua chance hoje.",
    "💫 Aproveita enquanto dá tempo."
]

def gerar():
    if periodo == "Bom Dia":
        s = "☀️ Bom dia!"
    elif periodo == "Boa Tarde":
        s = "🌤️ Boa tarde!"
    else:
        s = "🌙 Boa noite!"

    return f"{s}\n\n{random.choice(aberturas)} {random.choice(meio)}.\n{random.choice(fechamento)}"

def links():
    return f"\n\n🔍 Pesquisa: {LINK_PESQUISA}\n🌐 Hub: {LINK_HUB}"

if st.button("✨ Gerar mensagens infinitas"):

    mensagens = []

    for _ in range(quantidade):
        msg = gerar() + links()
        mensagens.append(msg)

    resultado = "\n\n---\n\n".join(mensagens)

    st.text_area("📋 Copie e poste:", resultado, height=500)
