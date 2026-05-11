import streamlit as st
import random

# Configuração da página
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
    quantidade = st.slider("Quantidade de mensagens:", 1, 100, 20)

# Link do Hub Atualizado
LINK_HUB = "https://links-luhveestore.streamlit.app/"

# 🎨 BANCO DE MENSAGENS (As frases permanecem as mesmas, mas a lógica de sorteio mudou)
# [Omitindo as listas longas aqui para o código ficar limpo, mas elas devem estar no seu script]

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

# ===== FUNÇÕES MELHORADAS PARA EVITAR REPETIÇÃO =====

def gerar_saudacao_variada(periodo):
    """Gera variações para a saudação não ser sempre idêntica"""
    saudacoes = {
        "Bom Dia": ["☀️ Bom dia!", "✨ Bom dia, lindeza!", "🌅 Um dia maravilhoso para você!", "🌷 Bom dia com muita alegria!"],
        "Boa Tarde": ["🌤️ Boa tarde!", "✨ Uma tarde produtiva e feliz!", "🌸 Boa tarde, estrela!", "🍃 Passando para desejar uma boa tarde!"],
        "Boa Noite": ["🌙 Boa noite!", "✨ Durma bem, boa noite!", "🌌 Uma noite de paz e luz!", "🧸 Boa noite com muito carinho!"]
    }
    return random.choice(saudacoes[periodo])

def gerar_mensagens(periodo, tom, qtd):
    banco = BANCOS[tom]
    mensagens = []
    
    for _ in range(qtd):
        saudacao = gerar_saudacao_variada(periodo)
        
        # Sorteia elementos diferentes a cada loop para criar combinações únicas
        ab = random.choice(banco["abertura"])
        me = random.choice(banco["meio"])
        fe = random.choice(banco["fechamento"])
        
        msg = (
            f"{saudacao}\n\n"
            f"{ab} {me}.\n"
            f"{fe}\n\n"
            f"🛒 Vamos para as compras 🛍️🛍️\n"
            f"{LINK_HUB}\n\n"
            f"Bjs da Luh da LuhVee ❤️"
        )
        mensagens.append(msg)
    
    return mensagens

# ===== INTERFACE =====

gerar_button = st.button("✨ Gerar mensagens de felicidade", use_container_width=True)

if gerar_button:
    with st.spinner("Gerando mensagens exclusivas... 💖"):
        lista_msgs = gerar_mensagens(periodo, tom, quantidade)
        # Separador visual entre as mensagens no campo de texto
        resultado = "\n\n" + "—" * 30 + "\n\n".join(lista_msgs)
    
    st.success(f"✅ {quantidade} mensagens geradas com sucesso!")
    st.text_area("📋 Copie e compartilhe com amor:", resultado, height=500)

# ===== FOOTER =====
st.divider()
st.caption("💖 LuhVee - Mensagens de amor e felicidade | Link do Hub atualizado")
