import streamlit as st
import random
from itertools import cycle

st.set_page_config(page_title="LuhVee - Mensagens de Felicidade", layout="wide")
st.title("💖 LuhVee - Mensagens de Felicidade para seu Dia")

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
        "Vibe do dia:",
        ["Amor Próprio", "Gratidão", "Motivação", "Positividade", "Autoconfiança", "Bem-estar", "Esperança", "Celebração"],
        help="Escolha a energia para o dia"
    )

with col3:
    quantidade = st.slider("Quantidade de mensagens:", 1, 500, 20)

# 🎨 BANCO DE MENSAGENS POSITIVAS (POR TOM)

# ===== TOM 1: AMOR PRÓPRIO =====
aberturas_amor_proprio = [
    "💖 Você merece todo o amor do mundo...",
    "✨ Hoje é dia de se amar mais...",
    "💝 Você é incrível do jeitinho que é...",
    "🌸 Se ame como se fosse sua melhor amiga...",
    "💎 Você vale muito mais do que pensa...",
    "👑 Você é a sua prioridade número 1...",
    "🌟 Seu corpo, sua mente, sua alma... tudo é lindo...",
    "💕 Aceite seus defeitos como parte da sua beleza...",
    "✨ Você é digna de toda a felicidade...",
    "💖 Amor próprio é o melhor investimento...",
]

meios_amor_proprio = [
    "cuide de si como se fosse alguém especial",
    "porque você merece o melhor de tudo",
    "aquele tipo de cuidado que ninguém te obriga",
    "sua saúde mental agradece",
    "seu corpo é um templo sagrado",
    "você é forte demais pra desistir",
    "diga coisas bonitas pra si mesma",
    "se respeite acima de tudo",
    "você é a obra de arte mais linda",
    "sua vida é o espelho do que você planta"
]

fechamentos_amor_proprio = [
    "💖 Você merece tudo isso e muito mais.",
    "✨ Cuide de si, sempre.",
    "💝 Seja gentil consigo mesma.",
    "🌸 Você é a razão de sua própria alegria.",
    "💎 Nunca deixe de brilhar.",
    "👑 Sua coroa fica bem em você.",
    "🌟 Continue se amando assim.",
    "💕 Você é o amor que procura.",
    "✨ Merecia saber disso antes.",
    "💖 Amor próprio é revolucionário.",
]

# ===== TOM 2: GRATIDÃO =====
aberturas_gratidao = [
    "🙏 Hoje é dia de agradecer por estar viva...",
    "💫 Quantas bênçãos você deixa passar?",
    "✨ Gratidão transforma tudo...",
    "🌺 Agradeça pelos pequenos momentos...",
    "💝 Você tem mais do que imagina...",
    "🌈 Cada dia é um presente...",
    "👼 Obrigada por tudo que tem...",
    "💖 Reconhecer bênçãos atrai mais...",
    "🙌 Seu coração merecia saber disso...",
    "✨ Gratidão é o caminho para a felicidade...",
]

meios_gratidao = [
    "mesmo que a vida pareça difícil agora",
    "porque tem gente que não tem o que você tem",
    "seu ar nos pulmões já é milagre",
    "sua família, seus amigos, sua vida",
    "as pessoas que te amam de verdade",
    "seu corpo que funciona, sua mente que pensa",
    "os momentos que fizeram você rir",
    "as lições que o tornaram mais forte",
    "aquele abraço que precisava",
    "estar aqui agora, neste exato momento"
]

fechamentos_gratidao = [
    "🙏 Obrigada por estar viva.",
    "💫 Agradeça todos os dias.",
    "✨ Gratidão é oração.",
    "🌺 Conte suas bênçãos.",
    "💝 Você é abençoada.",
    "🌈 Reconheça o milagre que é viver.",
    "👼 Deus/Universo ouve seu obrigada.",
    "💖 Gratidão atrai mais gratidão.",
    "🙌 Seu coração sente a diferença.",
    "✨ Continue grata, sempre.",
]

# ===== TOM 3: MOTIVAÇÃO =====
aberturas_motivacao = [
    "🚀 Você é mais capaz do que imagina...",
    "💪 Hoje é o dia da sua virada...",
    "⭐ Seus sonhos estão mais perto do que pensa...",
    "🔥 Não desista agora...",
    "💯 Você consegue, eu acredito...",
    "🎯 O melhor ainda está por vir...",
    "✨ Sua hora está chegando...",
    "🌟 O universo tá torcendo pra você...",
    "💝 Você é mais do que pensa que é...",
    "🚀 Dê um passo mesmo que pequeno...",
]

meios_motivacao = [
    "porque você vem vencendo todos os dias",
    "aquela dificuldade que você superou ontem",
    "você sobreviveu a 100% dos seus piores dias",
    "fale sim para as oportunidades",
    "seu potencial é infinito",
    "o fracasso é só um nome feio pro aprendizado",
    "você está crescendo mesmo que não veja",
    "a jornada é mais importante que o destino",
    "você é a resposta que procurava",
    "continuar é vencer"
]

fechamentos_motivacao = [
    "🚀 Você consegue, vai conseguir.",
    "💪 Não desista dos seus sonhos.",
    "⭐ Continue em frente, sempre.",
    "🔥 Você é mais forte do que pensa.",
    "💯 Acredite em você como acreditamos.",
    "🎯 Seus objetivos estão te esperando.",
    "✨ O universo está ao seu lado.",
    "🌟 Continue brilhando assim.",
    "💝 Você é digna de sucesso.",
    "🚀 Sua melhor versão está vindo.",
]

# ===== TOM 4: POSITIVIDADE =====
aberturas_positividade = [
    "☀️ Escolha a alegria hoje...",
    "🌈 A vida é o que você faz dela...",
    "💫 Pense em coisas que te fazem sorrir...",
    "✨ O bem estar começa em você...",
    "🦋 Transforme sua energia em positividade...",
    "🌻 Veja o lado bom de tudo...",
    "💛 A vida merecia sua felicidade...",
    "🌟 Sua energia atrai seu destino...",
    "💖 Sorria, você está viva...",
    "🎨 Pinte seu dia de cores...",
]

meios_positividade = [
    "porque sua mente merecia essa paz",
    "seus pensamentos criam sua realidade",
    "você tem poder sobre seus sentimentos",
    "escolha alegria a cada momento",
    "sua vibração atrai pessoas incríveis",
    "energia positiva é contagiante",
    "foque no que traz felicidade",
    "problemas vêm e vão",
    "sua alma merecia esse descanso",
    "a vida é agora, não lá na frente"
]

fechamentos_positividade = [
    "☀️ Escolha sorrir hoje.",
    "🌈 A vida é bela, aprecie.",
    "💫 Sua energia é tudo.",
    "✨ Mantenha a positividade.",
    "🦋 Transforme-se a cada dia.",
    "🌻 Veja a beleza ao seu redor.",
    "💛 A felicidade é sua escolha.",
    "🌟 Continue radiante assim.",
    "💖 Você merece se sentir bem.",
    "🎨 Sua vida é uma obra de arte.",
]

# ===== TOM 5: AUTOCONFIANÇA =====
aberturas_autoconfianca = [
    "👑 Você é a estrela do seu próprio filme...",
    "💎 Confie no seu valor...",
    "🔥 Você já provou sua força...",
    "✨ Sua opinião sobre você é o que importa...",
    "🌟 Você tem tudo que precisa dentro de si...",
    "💪 Você é capaz de tudo...",
    "👀 Olhe para você como outros te olham...",
    "💖 Você é exatamente do jeito que deveria ser...",
    "🎯 Sua verdade é sua força...",
    "🚀 Você não precisa de permissão pra brilhar...",
]

meios_autoconfianca = [
    "porque você já enfrentou coisas piores",
    "suas cicatrizes são prova de força",
    "você sabe mais do que imagina",
    "confie em suas escolhas",
    "você é experiente pela vida que viveu",
    "ninguém conhece você melhor que você",
    "sua intuição é sábia",
    "você tem direito de ocupar espaço",
    "sua voz merecia ser ouvida",
    "você é a expert da sua vida"
]

fechamentos_autoconfianca = [
    "👑 Você é a rainha do seu destino.",
    "💎 Confie em você, sempre.",
    "🔥 Você é mais forte do que aparenta.",
    "✨ Sua força vem de dentro.",
    "🌟 Você é inigualável.",
    "💪 Você consegue qualquer coisa.",
    "👀 Acredite no seu reflexo.",
    "💖 Você é exatamente perfeita.",
    "🎯 Sua verdade é sua vitória.",
    "🚀 Voe alto, sempre.",
]

# ===== TOM 6: BEM-ESTAR =====
aberturas_bem_estar = [
    "🧘‍♀️ Respire, você está bem...",
    "💆‍♀️ Seu corpo merecia descanso...",
    "🛀 Cuide do seu bem-estar...",
    "🌿 Seu equilíbrio é sagrado...",
    "💤 Durma bem, você merecia...",
    "🌙 Repouso também é produtivo...",
    "☕ Aprecie os pequenos prazeres...",
    "🧘‍♀️ Medite, conecte-se...",
    "🌱 Cresça no seu próprio tempo...",
    "💚 Saúde mental é saúde...",
]

meios_bem_estar = [
    "porque sua mente merecia parar",
    "seus nervos precisam desse repouso",
    "relaxar não é preguiça",
    "cuide da sua saúde mental como cuida de tudo",
    "seu corpo fala, está ouvindo?",
    "você não precisa fazer nada pra merecer",
    "desacelere, a vida espera",
    "seu coração bate melhor assim",
    "bem-estar é ato de amor",
    "sua paz é sua riqueza"
]

fechamentos_bem_estar = [
    "🧘‍♀️ Respire fundo, você está segura.",
    "💆‍♀️ Cuide de si sempre.",
    "🛀 Repouso é necessário.",
    "🌿 Seu equilíbrio importa.",
    "💤 Durma tranquila.",
    "🌙 Repouso é vitória.",
    "☕ Aprecie a vida agora.",
    "🧘‍♀️ Sua paz é prioridade.",
    "🌱 Você está exatamente no ritmo certo.",
    "💚 Cuide da sua saúde.",
]

# ===== TOM 7: ESPERANÇA =====
aberturas_esperanca = [
    "🌅 O melhor ainda está por vir...",
    "🕊️ Tudo muda, tudo passa...",
    "🌟 Depois da chuva vem o sol...",
    "💫 Seus melhores dias estão chegando...",
    "🦋 Transformação está em processo...",
    "🌈 A esperança nunca morre...",
    "🕯️ Sua luz não se apaga...",
    "🌱 Novo começo está aí...",
    "✨ Acredite que melhora...",
    "💝 O futuro tem seu nome...",
]

meios_esperanca = [
    "porque nada dura para sempre",
    "o pior momento já passou",
    "você é mais resistente do que imagina",
    "a maré vai virar",
    "seus melhores momentos te esperam",
    "o que parece fim é começo",
    "confia no processo",
    "você foi feita pra vencer",
    "o universo tem planos bons pra você",
    "sua história não termina aqui"
]

fechamentos_esperanca = [
    "🌅 Novos dias virão.",
    "🕊️ Tudo passa, tudo passa.",
    "🌟 Acredite, sempre.",
    "💫 Seus melhores dias vêm aí.",
    "🦋 Você está transformando.",
    "🌈 Esperança é tudo que precisa.",
    "🕯️ Sua luz guia seu caminho.",
    "🌱 Está nascendo novamente.",
    "✨ Confie no novo.",
    "💝 O melhor está por vir.",
]

# ===== TOM 8: CELEBRAÇÃO =====
aberturas_celebracao = [
    "🎉 Você conseguiu, é hora de celebrar...",
    "🥳 Cada vitória, por menor que seja...",
    "⭐ Você merecia esse reconhecimento...",
    "🎊 Orgulho de ser você...",
    "💃 Sua jornada é digna de festa...",
    "🍾 Brinde a você, guerreira...",
    "🎈 A vida é pra aproveitar...",
    "🏆 Você é campeã do seu destino...",
    "👸 Celebre o quanto você evoluiu...",
    "🎶 Sua vida é uma música linda...",
]

meios_celebracao = [
    "porque cada dia que vive é vitória",
    "seus objetivos alcançados são prova",
    "você cresceu, mudou, evoluiu",
    "reconheça seu esforço",
    "sua dedicação merecia este momento",
    "você é um exemplo de persistência",
    "celebre mesmo os pequenos sucessos",
    "sua presença já é celebração",
    "você transformou vidas só existindo",
    "sua história merecia ser contada"
]

fechamentos_celebracao = [
    "🎉 Parabéns por ser você.",
    "🥳 Sua vitória é nossa alegria.",
    "⭐ Você é incrível, de verdade.",
    "🎊 Celebre-se sempre.",
    "💃 Continue brilhando assim.",
    "🍾 Você merecia esse brinde.",
    "🎈 A vida sorri pra você.",
    "🏆 Sua coroa é merecida.",
    "👸 Continue evoluindo.",
    "🎶 Sua vida é uma sinfonia.",
]

# Dicionário de mapeamento completo
BANCOS = {
    "Amor Próprio": {
        "abertura": aberturas_amor_proprio,
        "meio": meios_amor_proprio,
        "fechamento": fechamentos_amor_proprio
    },
    "Gratidão": {
        "abertura": aberturas_gratidao,
        "meio": meios_gratidao,
        "fechamento": fechamentos_gratidao
    },
    "Motivação": {
        "abertura": aberturas_motivacao,
        "meio": meios_motivacao,
        "fechamento": fechamentos_motivacao
    },
    "Positividade": {
        "abertura": aberturas_positividade,
        "meio": meios_positividade,
        "fechamento": fechamentos_positividade
    },
    "Autoconfiança": {
        "abertura": aberturas_autoconfianca,
        "meio": meios_autoconfianca,
        "fechamento": fechamentos_autoconfianca
    },
    "Bem-estar": {
        "abertura": aberturas_bem_estar,
        "meio": meios_bem_estar,
        "fechamento": fechamentos_bem_estar
    },
    "Esperança": {
        "abertura": aberturas_esperanca,
        "meio": meios_esperanca,
        "fechamento": fechamentos_esperanca
    },
    "Celebração": {
        "abertura": aberturas_celebracao,
        "meio": meios_celebracao,
        "fechamento": fechamentos_celebracao
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
    
    # Link do Hub
    LINK_HUB = "https://hublinks-app.streamlit.app"
    
    mensagens = []
    for _ in range(quantidade):
        msg = f"{saudacao}\n\n{next(ciclo_abertura)} {next(ciclo_meio)}.\n{next(ciclo_fechamento)}\n\n🛒 Vamos para as compras 🛍️🛍️\n{LINK_HUB}\n\nBjs da Luh da LuhVee ❤️"
        mensagens.append(msg)
    
    return mensagens

# ===== INTERFACE =====

col_button, col_info = st.columns([1, 2])

with col_button:
    gerar_button = st.button("✨ Gerar mensagens de felicidade", use_container_width=True, key="gerar")

with col_info:
    st.caption("💝 Mensagens para deixar seu dia mais feliz!")

if gerar_button:
    with st.spinner("Gerando mensagens carinhosas... 💖"):
        mensagens = gerar_mensagens(periodo, tom, quantidade)
        resultado = "\n\n---\n\n".join(mensagens)
    
    # Exibe as mensagens
    st.success(f"✅ {quantidade} mensagens de felicidade geradas com sucesso!")
    
    st.text_area(
        "📋 Copie e compartilhe com amor:", 
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
        st.metric("Vibe", tom)
    with col_stats3:
        st.metric("Assinado com", "Bjs da Luh ❤️")
    
    st.info("💖 Cada mensagem foi feita com amor para trazer felicidade ao dia de alguém!")

# ===== FOOTER =====
st.divider()
st.caption("💖 LuhVee - Mensagens de amor e felicidade | Feito com ❤️ para deixar o dia mais bonito")
