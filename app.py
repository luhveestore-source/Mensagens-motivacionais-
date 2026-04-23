import streamlit as st
import random
from itertools import cycle

st.set_page_config(page_title="LuhVee - Gerador de Mensagens", layout="wide")
st.title("💖 LuhVee - Gerador de Mensagens Infinitas")

# 🔗 SEUS LINKS
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_HUB = "https://hublinks-app.streamlit.app"

# ===== CONFIGURAÇÕES =====
col1, col2, col3 = st.columns(3)

with col1:
    periodo = st.selectbox(
        "Tipo de Saudação:",
        ["Bom Dia", "Boa Tarde", "Boa Noite"],
        help="Escolha o período do dia"
    )

with col2:
    tom = st.selectbox(
        "Tom da mensagem:",
        ["Inspirador", "Urgente", "Amigável", "Exclusive", "Economia", "FOMO", "Social Proof", "Curiosidade"],
        help="Escolha o tom/vibe das mensagens"
    )

with col3:
    quantidade = st.slider("Quantidade de mensagens:", 1, 500, 20)

# 🎨 BANCO DE MENSAGENS EXPANDIDO (POR TOM)

# ===== TOM 1: INSPIRADOR =====
aberturas_inspirador = [
    "✨ Hoje pode ser o dia da sua virada...",
    "💖 Tem coisa boa chegando pra você...",
    "🌸 Não ignora isso aqui...",
    "🔥 Você merece muito mais do que imagina...",
    "💫 Isso aqui pode mudar seu dia...",
    "🌟 Algo especial está te esperando...",
    "✨ A vida recompensa quem toma ação...",
    "💎 Você é mais capaz do que pensa...",
    "🚀 É hora de crescer...",
    "💝 Merecia ter descoberto isso antes...",
]

meios_inspirador = [
    "imagine encontrar algo que combina com você",
    "coisas assim transformam vidas",
    "isso pode abrir portas incríveis",
    "você vai se surpreender com os resultados",
    "muita gente já experimentou e adorou",
    "isso é o tipo de coisa que faz diferença",
    "esse tipo de oportunidade não é todo dia",
    "seu potencial é maior que você imagina",
    "isso é o acelerador que você precisa",
    "grandes histórias começam com decisões pequenas",
]

fechamentos_inspirador = [
    "💖 Confia no processo.",
    "✨ Não deixa pra depois.",
    "🔥 Pode ser sua chance hoje.",
    "💫 Aproveita enquanto dá tempo.",
    "🌟 Sua vida agradece no futuro.",
    "💝 Você merece dar esse passo.",
    "🚀 Começar é vencer metade.",
    "💎 Isso é investimento em você.",
    "✨ Sua melhor versão chama por isso.",
    "🔥 Toma essa decisão corajosa.",
]

# ===== TOM 2: URGENTE =====
aberturas_urgente = [
    "⏰ Isso não vai durar...",
    "🔥 Segundos contam...",
    "⚡ Muita gente está pegando agora...",
    "⏳ Isso está saindo de estoque...",
    "💨 Não dura até amanhã...",
    "🚨 Último aviso para você...",
    "⚡ Isso está viralizando...",
    "🔔 Acordaaaa para essa oportunidade...",
    "⏰ O tempo está acabando...",
    "💔 Quem não pega agora se arrepende...",
]

meios_urgente = [
    "coisas assim somem em minutos",
    "muita gente já está aproveitando",
    "isso chama atenção de verdade",
    "fila andando rápido demais",
    "não fica mais que 2 horas disponível",
    "a concorrência já descobriu",
    "estoque se esgotando agora",
    "próxima rodada começa em poucas horas",
    "essa é a janela: agora ou nunca",
    "quem quer pega rápido",
]

fechamentos_urgente = [
    "🔥 Aproveita AGORA.",
    "⚡ Sem esperar mais.",
    "⏰ Vai? Vai? Vai!",
    "💨 Rápido antes de sair.",
    "🚀 Pega já a sua cota.",
    "⏳ Segundos importam aqui.",
    "🎯 Toma a ação agora.",
    "💥 Não deixa morrer na praia.",
    "🔔 Tá na hora mesmo.",
    "⚡ Clica rápido demais.",
]

# ===== TOM 3: AMIGÁVEL =====
aberturas_amigavel = [
    "Oi, tudo bem? 👋",
    "E aí, você sabia disso? 😊",
    "Ó, olha só que legal! 💕",
    "Vem cá, achei que você ia gostar...",
    "Psiu, vem ver uma coisa... 💖",
    "Eita, encontrei algo especial! ✨",
    "Sabe aquele feeling? 🌸",
    "Olha, achei perfeito pra você...",
    "Vem conhecer uma novidade! 💫",
    "Viu isso já? Te aposto que você adora...",
]

meios_amigavel = [
    "você vai gostar disso",
    "é coisa de verdade mesmo",
    "combinava com você desde o começo",
    "sabe aquele tipo que te faz feliz?",
    "isso é meu recomendado pessoal",
    "conheço gente que adorou",
    "testei e confirmei: vale muito",
    "é tipo aquele achado que muda tudo",
    "sinceramente? Perfeito demais",
    "promete, você não vai se arrepender",
]

fechamentos_amigavel = [
    "💕 Garanto que você vai amar.",
    "😊 Confia em mim nessa.",
    "💖 Você vai me agradecer depois.",
    "✨ Sério mesmo, é bom demais.",
    "🌸 Essa é minha recomendação forte.",
    "💫 Você não vai se arrepender.",
    "😄 Sinta só como é top.",
    "💝 Isso é coisa de amiga mesmo.",
    "🎉 Você vai amar descobrir.",
    "✨ É tipo aquela que você buscava.",
]

# ===== TOM 4: EXCLUSIVE =====
aberturas_exclusive = [
    "🎭 Isso é só pra você... 👑",
    "💎 Acesso exclusivo, selecionado...",
    "🔐 Nem todo mundo sabe disso...",
    "👑 VIP alert incoming...",
    "✨ Você ganhou acesso especial...",
    "🌟 Privilegiado demais pro comum...",
    "💰 Ouro em barra aqui...",
    "🏆 Elite detect aqui...",
    "🎯 Escolhido a dedo pra você...",
    "👑 Seu status merecia saber...",
]

meios_exclusive = [
    "apenas selecionados têm acesso",
    "nem todo mundo consegue ver isso",
    "você está em um grupo especial",
    "isso é importado, raro por aqui",
    "acesso restrito às pessoas certas",
    "cota limitada pro tipo de pessoa certa",
    "circula só entre quem sabe",
    "segredo de quem conhece qualidade",
    "privilegiado demais pro comum",
    "você tem bom gosto detectado",
]

fechamentos_exclusive = [
    "👑 Seu lugar é aqui.",
    "💎 Acesso confirmado pro VIP.",
    "🌟 Status elevado detectado.",
    "✨ Bem-vindo ao grupo select.",
    "🏆 Você tinha direito a isso.",
    "💰 Qualidade reconhece qualidade.",
    "🎭 Esse é seu nível.",
    "👑 Privilégio merecido.",
    "💎 Isso faz parte de quem é bom.",
    "🔐 Raridade só pra você.",
]

# ===== TOM 5: ECONOMIA =====
aberturas_economia = [
    "💰 Isso vai economizar sua grana...",
    "🤑 Achei a melhor barganha do mês...",
    "💳 Seu dinheiro renderá mais aqui...",
    "🎁 Descontos que você não vê por aí...",
    "💵 Gastando menos, ganhando mais...",
    "🏷️ Preço que faz a gente chorar de alegria...",
    "💎 Qualidade sem esvaziar o bolso...",
    "🔔 Promoção que não pode perder...",
    "💸 Seu orçamento agradece...",
    "🎯 Achado que economiza meses de poupança...",
]

meios_economia = [
    "o preço está tão bom que parece brincadeira",
    "você paga menos e leva mais",
    "economia que só vira notícia boa",
    "aquele tipo de desconto que dura pouco",
    "investimento que se paga rapidinho",
    "qualidade por fração do preço normal",
    "promoção que faz até economista chorar",
    "você vai gastar menos e ficar rico",
    "aquele deal que você contar pro povo",
    "economia que deixa seu cartão feliz",
]

fechamentos_economia = [
    "💰 Sério, economiza demais.",
    "🤑 Seu bolso agradece agora.",
    "💳 Aproveita esse preço.",
    "🎁 Não deixa passar esse desconto.",
    "💵 Parou a promoção de tão boa.",
    "🏷️ Enche o carrinho antes que acabe.",
    "💎 Qualidade + preço = sucesso.",
    "🔔 Esse deal não vem todo dia.",
    "💸 Economia que você merecia.",
    "🎯 Investe nessa sacanagem.",
]

# ===== TOM 6: FOMO =====
aberturas_fomo = [
    "😱 Enquanto você lê, alguém mais já pegou...",
    "🔥 Mais gente descobrindo a cada segundo...",
    "⚡ Seu amigo já viu isso antes de você...",
    "😭 Aqueles que perderam vão se arrepender...",
    "🚀 A galera toda está nessa onda agora...",
    "💔 Você vai ser o último a saber...",
    "📢 Virou febre nas redes já...",
    "⏰ O FOMO é real, super real...",
    "👀 Viu quanto de gente fazendo?",
    "😩 Ficou de fora dessa vez?",
]

meios_fomo = [
    "enquanto você lê isso já saiu",
    "todos estão pegando menos você",
    "sua timeline inteira já descobriu",
    "o trending topic é isso agora",
    "quando virar notícia você sabia antes",
    "seus amigos já estão curtindo",
    "só você não entrou nessa ainda",
    "todo mundo menos você",
    "não seja o último a descobrir",
    "o pessoal de dentro já sabe",
]

fechamentos_fomo = [
    "😱 Entra na onda urgente.",
    "🔥 Antes que fique late.",
    "⚡ Sério, corre agora.",
    "😭 Não fica de fora.",
    "🚀 Toda galera está indo.",
    "💔 Aproveita enquanto está quente.",
    "📢 O trend é agora.",
    "⏰ Time to jump in.",
    "👀 Sou você, ia fazer agora.",
    "😩 Não deixa passar mais nada.",
]

# ===== TOM 7: SOCIAL PROOF =====
aberturas_social_proof = [
    "⭐ A galera toda está amando...",
    "👥 Já tem 10 mil pessoas usando...",
    "💯 100% recomendado por quem usou...",
    "🏆 Campeão de satisfação aqui...",
    "👍 As reviews não mentem...",
    "🌟 Virou referência pra galera...",
    "💬 O que falam sobre isso?",
    "📊 Os números não enganam...",
    "🎤 Quem usa canta louvor...",
    "✅ Selo de qualidade conferido...",
]

meios_social_proof = [
    "a galera toda está falando disso",
    "reviews que não deixam dúvida",
    "números que falam por si",
    "testemunhos que emocionam",
    "quem usou virou fã automático",
    "reputação que só cresce",
    "feedback que é tudo positivo",
    "pessoas que voltariam a fazer",
    "histórias de sucesso de verdade",
    "quem conhece recomenda pro mundo",
]

fechamentos_social_proof = [
    "⭐ Confere as reviews.",
    "👥 Entra no grupo crescente.",
    "💯 Vai ser satisfeito demais.",
    "🏆 Qualidade comprovada.",
    "👍 Recomendação que vale.",
    "🌟 Vai entender por que.",
    "💬 Pergunte pra quem usa.",
    "📊 Os dados estão aí.",
    "🎤 As vozes falam alto.",
    "✅ Confiança que compra.",
]

# ===== TOM 8: CURIOSIDADE =====
aberturas_curiosidade = [
    "🤔 Sabe aquela coisa que você procura?",
    "❓ Isso vai explodir sua mente...",
    "🎁 O que mais ganha visualização...",
    "👀 Coisas que poucos conhecem...",
    "🔍 Descoberta do mês está aqui...",
    "💡 Você NÃO sabe disso ainda...",
    "🚪 Abre essa porta comigo...",
    "🎯 Achei algo que você vai amar...",
    "✨ Tá procurando por isso?",
    "🔐 Segredo guardado está aqui...",
]

meios_curiosidade = [
    "você nunca viu algo assim",
    "é tipo aquele mystery box",
    "desvendando uma descoberta incrível",
    "coisas que deixam a boca aberta",
    "você vai querer contar pra alguém",
    "tipo aquele achado que surpreende",
    "é bem diferente do comum",
    "desperta aquela curiosidade louca",
    "você não aguenta de vontade",
    "o tipo de coisa que vicia",
]

fechamentos_curiosidade = [
    "🤔 Vem descobrir que é.",
    "❓ Cria uma necessidade em você.",
    "🎁 Abre pra ficar impressionado.",
    "👀 Você vai amar saber.",
    "🔍 Tá esperando o quê?",
    "💡 Conhecimento é poder.",
    "🚪 Entra e descobre.",
    "🎯 Satisfaz sua curiosidade.",
    "✨ Tá aí a surpresa.",
    "🔐 Desbloqueie essa novidade.",
]

# Dicionário de mapeamento completo
BANCOS = {
    "Inspirador": {
        "abertura": aberturas_inspirador,
        "meio": meios_inspirador,
        "fechamento": fechamentos_inspirador
    },
    "Urgente": {
        "abertura": aberturas_urgente,
        "meio": meios_urgente,
        "fechamento": fechamentos_urgente
    },
    "Amigável": {
        "abertura": aberturas_amigavel,
        "meio": meios_amigavel,
        "fechamento": fechamentos_amigavel
    },
    "Exclusive": {
        "abertura": aberturas_exclusive,
        "meio": meios_exclusive,
        "fechamento": fechamentos_exclusive
    },
    "Economia": {
        "abertura": aberturas_economia,
        "meio": meios_economia,
        "fechamento": fechamentos_economia
    },
    "FOMO": {
        "abertura": aberturas_fomo,
        "meio": meios_fomo,
        "fechamento": fechamentos_fomo
    },
    "Social Proof": {
        "abertura": aberturas_social_proof,
        "meio": meios_social_proof,
        "fechamento": fechamentos_social_proof
    },
    "Curiosidade": {
        "abertura": aberturas_curiosidade,
        "meio": meios_curiosidade,
        "fechamento": fechamentos_curiosidade
    }
}

# ===== FUNÇÕES =====

def gerar_saudacao(periodo):
    """Gera a saudação inicial"""
    saudacoes = {
        "Bom Dia": "☀️ Bom dia!",
        "Boa Tarde": "🌤️ Boa tarde!",
        "Boa Noite": "🌙 Boa noite!"
    }
    return saudacoes[periodo]

def gerar_mensagens(periodo, tom, quantidade):
    """Gera mensagens sem repetição dentro de um ciclo"""
    banco = BANCOS[tom]
    
    # Embaralha os bancos para variedade
    aberturas = banco["abertura"].copy()
    meios = banco["meio"].copy()
    fechamentos = banco["fechamento"].copy()
    
    random.shuffle(aberturas)
    random.shuffle(meios)
    random.shuffle(fechamentos)
    
    # Cria ciclos para repetição sem padrão
    ciclo_abertura = cycle(aberturas)
    ciclo_meio = cycle(meios)
    ciclo_fechamento = cycle(fechamentos)
    
    saudacao = gerar_saudacao(periodo)
    
    mensagens = []
    for _ in range(quantidade):
        msg = f"{saudacao}\n\n{next(ciclo_abertura)} {next(ciclo_meio)}.\n{next(ciclo_fechamento)}"
        mensagens.append(msg)
    
    return mensagens

def adicionar_links(mensagem):
    """Adiciona os links ao final da mensagem"""
    return f"{mensagem}\n\n🔍 Pesquisa: {LINK_PESQUISA}\n🌐 Hub: {LINK_HUB}"

# ===== INTERFACE =====

col_button, col_info = st.columns([1, 2])

with col_button:
    gerar_button = st.button("✨ Gerar mensagens infinitas", use_container_width=True, key="gerar")

with col_info:
    tons_disponiveis = ", ".join(list(BANCOS.keys())[:4])
    st.caption(f"💡 Tons: {tons_disponiveis}...")

if gerar_button:
    with st.spinner("Gerando suas mensagens... 💫"):
        mensagens = gerar_mensagens(periodo, tom, quantidade)
        mensagens_com_links = [adicionar_links(msg) for msg in mensagens]
        resultado = "\n\n---\n\n".join(mensagens_com_links)
    
    # Exibe as mensagens
    st.success(f"✅ {quantidade} mensagens geradas com sucesso!")
    
    st.text_area(
        "📋 Copie e poste:", 
        resultado, 
        height=500,
        key="resultado"
    )
    
    # Info adicional
    st.divider()
    
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    with col_stats1:
        st.metric("Total gerado", f"{quantidade} msgs")
    with col_stats2:
        st.metric("Tom usado", tom)
    with col_stats3:
        st.metric("Variações", "10 cada")
    
    st.info("💡 Todas as mensagens são **únicas em estrutura** com emojis e chamadas diferentes!")

# ===== FOOTER =====
st.divider()
st.caption("🚀 LuhVee - Agregador de deals inteligente | Feito com ❤️ para o seu sucesso")
