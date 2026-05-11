import streamlit as st
import random

# Configuração da página - Nome corrigido para Luhvee Stores
st.set_page_config(page_title="Luhvee Stores - Mensagens de Felicidade", layout="wide")
st.title("💖 Luhvee Stores - Mensagens de Felicidade para seu Dia")

# ===== BANCO DE MENSAGENS (DEFINIDAS ANTES DE TUDO PARA EVITAR ERRO) =====

# AMOR PRÓPRIO
aberturas_amor_proprio = ["💖 Você merece todo o amor do mundo...", "✨ Hoje é dia de se amar mais...", "💝 Você é incrível do jeitinho que é...", "🌸 Se ame como se fosse sua melhor amiga...", "💎 Você vale muito mais do que pensa...", "👑 Você é a sua prioridade número 1...", "🌟 Seu corpo, mente e alma são lindos...", "💕 Aceite seus defeitos como beleza...", "✨ Você é digna de toda felicidade...", "💖 Amor próprio é o melhor investimento..."]
meios_amor_proprio = ["cuide de si como se fosse alguém especial", "porque você merece o melhor de tudo", "aquele tipo de cuidado que ninguém te obriga", "sua saúde mental agradece", "seu corpo é um templo sagrado", "você é forte demais pra desistir", "diga coisas bonitas pra si mesma", "se respeite acima de tudo", "você é a obra de arte mais linda", "sua vida é o espelho do que você planta"]
fechamentos_amor_proprio = ["💖 Você merece tudo isso e muito mais.", "✨ Cuide de si, sempre.", "💝 Seja gentil consigo mesma.", "🌸 Você é a razão de sua própria alegria.", "💎 Nunca deixe de brilhar.", "👑 Sua coroa fica bem em você.", "🌟 Continue se amando assim.", "💕 Você é o amor que procura.", "✨ Merecia saber disso antes.", "💖 Amor próprio é revolucionário."]

# GRATIDÃO
aberturas_gratidao = ["🙏 Hoje é dia de agradecer...", "💫 Quantas bênçãos você viu hoje?", "✨ Gratidão transforma tudo...", "🌺 Agradeça pelos pequenos momentos...", "💝 Você tem mais do que imagina...", "🌈 Cada dia é um presente...", "👼 Obrigada por tudo que tem...", "💖 Reconhecer bênçãos atrai mais...", "🙌 Seu coração precisava saber disso...", "✨ Gratidão é o caminho..."]
meios_gratidao = ["mesmo que a vida pareça difícil", "porque tem gente que valoriza o que você tem", "seu ar nos pulmões já é milagre", "sua família, seus amigos, sua vida", "as pessoas que te amam de verdade", "seu corpo que funciona, sua mente que pensa", "os momentos que fizeram você rir", "as lições que o tornaram mais forte", "aquele abraço que precisava", "estar aqui agora, neste momento"]
fechamentos_gratidao = ["🙏 Obrigada por estar viva.", "💫 Agradeça todos os dias.", "✨ Gratidão é oração.", "🌺 Conte suas bênçãos.", "💝 Você é abençoada.", "🌈 Reconheça o milagre que é viver.", "👼 O universo ouve seu obrigada.", "💖 Gratidão atrai mais gratidão.", "🙌 Seu coração sente a diferença.", "✨ Continue grata, sempre."]

# MOTIVAÇÃO
aberturas_motivacao = ["🚀 Você é mais capaz do que imagina...", "💪 Hoje é o dia da sua virada...", "⭐ Seus sonhos estão perto...", "🔥 Não desista agora...", "💯 Você consegue, eu acredito...", "🎯 O melhor ainda está por vir...", "✨ Sua hora está chegando...", "🌟 O universo torce por você...", "💝 Você é mais do que pensa...", "🚀 Dê um passo mesmo que pequeno..."]
meios_motivacao = ["porque você vem vencendo todos os dias", "aquela dificuldade que você superou ontem", "você sobreviveu a 100% dos seus piores dias", "fale sim para as oportunidades", "seu potencial é infinito", "o fracasso é aprendizado", "você está crescendo mesmo sem ver", "a jornada é o que importa", "você é a resposta que procurava", "continuar é vencer"]
fechamentos_motivacao = ["🚀 Você consegue, vai conseguir.", "💪 Não desista dos seus sonhos.", "⭐ Continue em frente, sempre.", "🔥 Você é mais forte do que pensa.", "💯 Acredite em você.", "🎯 Seus objetivos te esperam.", "✨ O universo está ao seu lado.", "🌟 Continue brilhando.", "💝 Você é digna de sucesso.", "🚀 Sua melhor versão está vindo."]

# POSITIVIDADE
aberturas_positividade = ["☀️ Escolha a alegria hoje...", "🌈 A vida é o que você faz dela...", "💫 Pense em coisas que te fazem sorrir...", "✨ O bem estar começa em você...", "🦋 Transforme sua energia...", "🌻 Veja o lado bom de tudo...", "💛 A vida merecia sua felicidade...", "🌟 Sua energia atrai seu destino...", "💖 Sorria, você está viva...", "🎨 Pinte seu dia de cores..."]
meios_positividade = ["porque sua mente merecia essa paz", "seus pensamentos criam realidade", "você tem poder sobre seus sentimentos", "escolha alegria a cada momento", "sua vibração atrai pessoas incríveis", "energia positiva é contagiante", "foque no que traz felicidade", "problemas vêm e vão", "sua alma merecia esse descanso", "a vida é agora"]
fechamentos_positividade = ["☀️ Escolha sorrir hoje.", "🌈 A vida é bela, aprecie.", "💫 Sua energia é tudo.", "✨ Mantenha a positividade.", "🦋 Transforme-se a cada dia.", "🌻 Veja a beleza ao seu redor.", "💛 A felicidade é sua escolha.", "🌟 Continue radiante.", "💖 Você merece se sentir bem.", "🎨 Sua vida é uma obra de arte."]

# AUTOCONFIANÇA
aberturas_autoconfianca = ["👑 Você é a estrela do seu filme...", "💎 Confie no seu valor...", "🔥 Você já provou sua força...", "✨ Sua opinião sobre você é o que importa...", "🌟 Você tem tudo dentro de si...", "💪 Você é capaz de tudo...", "👀 Olhe para você com amor...", "💖 Você é perfeita do seu jeito...", "🎯 Sua verdade é sua força...", "🚀 Não precisa de permissão pra brilhar..."]
meios_autoconfianca = ["porque você já enfrentou coisas piores", "suas cicatrizes são prova de força", "você sabe mais do que imagina", "confie em suas escolhas", "você é experiente pela vida que viveu", "ninguém conhece você melhor que você", "sua intuição é sábia", "você tem direito de ocupar espaço", "sua voz merecia ser ouvida", "você é a expert da sua vida"]
fechamentos_autoconfianca = ["👑 Você é a rainha do seu destino.", "💎 Confie em você, sempre.", "🔥 Você é mais forte do que aparenta.", "✨ Sua força vem de dentro.", "🌟 Você é inigualável.", "💪 Você consegue qualquer coisa.", "👀 Acredite no seu reflexo.", "💖 Você é perfeita.", "🎯 Sua verdade é sua vitória.", "🚀 Voe alto, sempre."]

# BEM-ESTAR
aberturas_bem_estar = ["🧘‍♀️ Respire, você está bem...", "💆‍♀️ Seu corpo merecia descanso...", "🛀 Cuide do seu bem-estar...", "🌿 Seu equilíbrio é sagrado...", "💤 Durma bem, você merecia...", "🌙 Repouso também é produtivo...", "☕ Aprecie os pequenos prazeres...", "🧘‍♀️ Medite, conecte-se...", "🌱 Cresça no seu próprio tempo...", "💚 Saúde mental é saúde..."]
meios_bem_estar = ["porque sua mente merecia parar", "seus nervos precisam desse repouso", "relaxar não é preguiça", "cuide da sua saúde mental", "seu corpo fala, está ouvindo?", "você não precisa fazer nada pra merecer", "desacelere, a vida espera", "seu coração bate melhor assim", "bem-estar é ato de amor", "sua paz é sua riqueza"]
fechamentos_bem_estar = ["🧘‍♀️ Respire fundo, você está segura.", "💆‍♀️ Cuide de si sempre.", "🛀 Repouso é necessário.", "🌿 Seu equilíbrio importa.", "💤 Durma tranquila.", "🌙 Repouso é vitória.", "☕ Aprecie a vida agora.", "🧘‍♀️ Sua paz é prioridade.", "🌱 No ritmo certo.", "💚 Cuide da sua saúde."]

# ESPERANÇA
aberturas_esperanca = ["🌅 O melhor ainda está por vir...", "🕊️ Tudo muda, tudo passa...", "🌟 Depois da chuva vem o sol...", "💫 Seus melhores dias estão chegando...", "🦋 Transformação em processo...", "🌈 A esperança nunca morre...", "🕯️ Sua luz não se apaga...", "🌱 Novo começo está aí...", "✨ Acredite que melhora...", "💝 O futuro tem seu nome..."]
meios_esperanca = ["porque nada dura para sempre", "o pior momento já passou", "você é resistente", "a maré vai virar", "seus melhores momentos te esperam", "o que parece fim é começo", "confia no processo", "você foi feita pra vencer", "o universo tem planos bons", "sua história não termina aqui"]
fechamentos_esperanca = ["🌅 Novos dias virão.", "🕊️ Tudo passa.", "🌟 Acredite, sempre.", "💫 Seus melhores dias vêm aí.", "🦋 Você está transformando.", "🌈 Esperança é o que precisa.", "🕯️ Sua luz guia o caminho.", "🌱 Está nascendo novamente.", "✨ Confie no novo.", "💝 O melhor está por vir."]

# CELEBRAÇÃO
aberturas_celebracao = ["🎉 É hora de celebrar...", "🥳 Cada vitória importa...", "⭐ Você merecia reconhecimento...", "🎊 Orgulho de ser você...", "💃 Sua jornada é uma festa...", "🍾 Brinde a você, guerreira...", "🎈 Aproveite a vida...", "🏆 Campeã do seu destino...", "👸 Celebre sua evolução...", "🎶 Sua vida é uma música linda..."]
meios_celebracao = ["porque cada dia vivido é vitória", "seus objetivos são a prova", "você cresceu e evoluiu", "reconheça seu esforço", "sua dedicação merecia este momento", "exemplo de persistência", "celebre os pequenos sucessos", "sua presença é uma festa", "você transforma vidas", "sua história merece ser contada"]
fechamentos_celebracao = ["🎉 Parabéns por ser você.", "🥳 Sua vitória é nossa alegria.", "⭐ Você é incrível.", "🎊 Celebre-se sempre.", "💃 Continue brilhando.", "🍾 Você merece este brinde.", "🎈 A vida sorri pra você.", "🏆 Sua coroa é merecida.", "👸 Continue evoluindo.", "🎶 Sua vida é uma sinfonia."]

# ===== CONFIGURAÇÃO DO HUB E DICIONÁRIO =====

LINK_HUB = "https://links-luhveestore.streamlit.app/"

BANCOS = {
    "Amor Próprio": {"abertura": aberturas_amor_proprio, "meio": meios_amor_proprio, "fechamento": fechamentos_amor_proprio},
    "Gratidão": {"abertura": aberturas_gratidao, "meio": meios_gratidao, "fechamento": fechamentos_gratidao},
    "Motivação": {"abertura": aberturas_motivacao, "meio": meios_motivacao, "fechamento": fechamentos_motivacao},
    "Positividade": {"abertura": aberturas_positividade, "meio": meios_positividade, "fechamento": fechamentos_positividade},
    "Autoconfiança": {"abertura": aberturas_autoconfianca, "meio": meios_autoconfianca, "fechamento": fechamentos_autoconfianca},
    "Bem-estar": {"abertura": aberturas_bem_estar, "meio": meios_bem_estar, "fechamento": fechamentos_bem_estar},
    "Esperança": {"abertura": aberturas_esperanca, "meio": meios_esperanca, "fechamento": fechamentos_esperanca},
    "Celebração": {"abertura": aberturas_celebracao, "meio": meios_celebracao, "fechamento": fechamentos_celebracao}
}

# ===== INTERFACE DO USUÁRIO =====

col1, col2, col3 = st.columns(3)

with col1:
    periodo = st.selectbox("Saudação:", ["Bom Dia", "Boa Tarde", "Boa Noite"])

with col2:
    tom = st.selectbox("Vibe:", list(BANCOS.keys()))

with col3:
    quantidade = st.slider("Quantidade:", 1, 100, 20)

# ===== LÓGICA DE GERAÇÃO (ANTI-REPETIÇÃO) =====

def gerar_mensagens():
    banco = BANCOS[tom]
    
    # Criamos cópias e embaralhamos para garantir que a ordem mude sempre
    abs_list = banco["abertura"].copy()
    meios_list = banco["meio"].copy()
    fecs_list = banco["fechamento"].copy()
    
    random.shuffle(abs_list)
    random.shuffle(meios_list)
    random.shuffle(fecs_list)
    
    saudacoes_extras = {
        "Bom Dia": ["☀️ Bom dia!", "✨ Bom dia, lindeza!", "🌅 Um dia maravilhoso!", "🌷 Bom dia com alegria!"],
        "Boa Tarde": ["🌤️ Boa tarde!", "✨ Tarde feliz!", "🌸 Boa tarde, estrela!", "🍃 Boa tarde pra você!"],
        "Boa Noite": ["🌙 Boa noite!", "✨ Durma bem!", "🌌 Noite de paz!", "🧸 Boa noite, querida!"]
    }

    final_msgs = []
    for i in range(quantidade):
        # Escolhe partes aleatórias
        s = random.choice(saudacoes_extras[periodo])
        a = abs_list[i % len(abs_list)]
        m = meios_list[i % len(meios_list)]
        f = fecs_list[i % len(fecs_list)]
        
        msg = (
            f"{s}\n\n"
            f"{a} {m}.\n"
            f"{f}\n\n"
            f"🛒 Vamos para as compras 🛍️🛍️\n"
            f"{LINK_HUB}\n\n"
            f"Bjs da Luh ❤️"
        )
        final_msgs.append(msg)
    
    return final_msgs

if st.button("✨ Gerar mensagens para a Luhvee Stores", use_container_width=True):
    msgs = gerar_mensagens()
    resultado = "\n\n" + "—" * 20 + "\n\n".join(msgs)
    st.success(f"✅ {quantidade} mensagens geradas!")
    st.text_area("📋 Copie aqui:", resultado, height=500)

st.divider()
st.caption("💖 Luhvee Stores - Transformando seu dia com amor e achadinhos")
