import streamlit as st
import random

st.set_page_config(page_title="LuhVee Mensagens", page_icon="💖")

st.title("💖 LuhVee Stores - Mensagens para Postar")

periodo = st.selectbox("Tipo de mensagem:", ["Bom Dia", "Boa Tarde", "Boa Noite"])
quantidade = st.slider("Quantidade:", 1, 200, 10)

aberturas = ["✨ Novo começo!", "💖 Lembre-se:", "🌸 Dica do dia:"]
meio = ["você merece coisas incríveis", "coisas boas estão chegando", "você é forte"]
final = ["💖 Confia!", "✨ Vai dar certo!", "🔥 Bora!"]

def gerar():
    return f"{random.choice(aberturas)} {random.choice(meio)}. {random.choice(final)}"

if st.button("✨ Gerar mensagens"):

    mensagens = []

    for _ in range(quantidade):
        if periodo == "Bom Dia":
            msg = "☀️ Bom dia! " + gerar()
        elif periodo == "Boa Tarde":
            msg = "🌤️ Boa tarde! " + gerar()
        else:
            msg = "🌙 Boa noite! " + gerar()

        mensagens.append(msg)

    texto_final = "\n\n".join(mensagens)

    st.success("Mensagens geradas!")

    # 👇 MOSTRA TUDO PRONTO PRA COPIAR
    st.text_area("📋 Copie suas mensagens aqui:", texto_final, height=400)
