import streamlit as st
from generator import gerar
from formatter import *
from exporter import exportar
from image_creator import criar_imagem
import random

st.title("💖 LuhVee Automação Completa")

qtd = st.slider("Quantidade", 10, 5000, 100)

if st.button("🚀 Gerar Tudo"):
    dados = []

    for i in range(qtd):
        periodo = random.choice(["dia", "tarde", "noite"])
        base = gerar(periodo)

        insta = formatar_instagram(base)
        zap = formatar_whatsapp(base)
        tele = formatar_telegram(base)

        dados.append({
            "instagram": insta,
            "whatsapp": zap,
            "telegram": tele
        })

        if i < 50:
            criar_imagem(insta, i)

    exportar(dados)

    st.success("✅ Tudo gerado: mensagens + CSV + imagens!")
