import random

LINK_PESQUISA = "https://SEU-LINK-PESQUISA-AQUI"
LINK_HUB = "https://SEU-LINK-HUB-AQUI"

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

def inserir_links():
    tipo = random.choice(["pesquisa", "hub", "ambos", "nenhum"])

    if tipo == "pesquisa":
        return f"\n🔍 {LINK_PESQUISA}"
    elif tipo == "hub":
        return f"\n🌐 {LINK_HUB}"
    elif tipo == "ambos":
        return f"\n🔍 {LINK_PESQUISA}\n🌐 {LINK_HUB}"
    return ""

def gerar(periodo):
    saudacoes = {
        "dia": "☀️ Bom dia!",
        "tarde": "🌤️ Boa tarde!",
        "noite": "🌙 Boa noite!"
    }

    base = f"{saudacoes[periodo]}\n\n{random.choice(aberturas)} {random.choice(meio)}.\n{random.choice(final)}"
    return base + inserir_links()
