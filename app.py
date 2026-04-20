import random
import streamlit as st

st.set_page_config(page_title="LuhVee Mensagens", page_icon="💖")

st.title("💖 LuhVee Stores - Mensagens com Links")

periodo = st.selectbox("Tipo:", ["Bom Dia", "Boa Tarde", "Boa Noite"])
quantidade = st.slider("Quantidade:", 1, 200, 10)

# 🔗 SEUS LINKS (COLOQUE OS REAIS AQUI)
LINK_PESQUISA = "https://SEU-LINK-PESQUISA"
LINK_HUB = "https://SEU-LINK-HUB"

aberturas = ["✨ Novo começo!", "🌸 Dica do dia:", "💖 Lembre-se:"]
meio = ["coisas boas estão chegando", "você merece coisas incríveis", "você é forte"]
final = ["💖 Confia!", "✨ Vai dar certo!", "🔥 Bora!"]

def gerar_base():
    return f"{random.choice(aberturas)} {random.choice(meio)}. {random.choice(final)}"

def inserir_links():
    tipo = random.choice(["pesquisa", "hub", "ambos", "nenhum"])

    if tipo == "pesquisa":
        return f"\n🔍 {LINK_PESQUISA}"
    elif tipo == "hub":
        return f"\n🌐 {LINK_HUB}"
    elif tipo == "ambos":
        return f"\n🔍 {LINK_PESQUISA}\n🌐 {LINK_HUB}"
    return ""

if st.button("✨ Gerar mensagens"):

    mensagens = []

    for _ in range(quantidade):

        if periodo == "Bom Dia":
            saudacao = "☀️ Bom dia!"
        elif periodo == "Boa Tarde":
            saudacao = "🌤️ Boa tarde!"
        else:
            saudacao = "🌙 Boa noite!"

        msg = f"{saudacao} {gerar_base()}{inserir_links()}"
        mensagens.append(msg)

    resultado = "\n\n".join(mensagens)

    st.success("Mensagens geradas com links!")

    st.text_area("📋 Copie aqui:", resultado, height=400)
