# 💖 LuhVee - Gerador de Mensagens Infinitas

Um gerador de mensagens de marketing inteligente e dinâmico feito com Streamlit. Crie mensagens únicas e variadas para suas campanhas com 8 tons diferentes!

## ✨ Características

✅ **8 Tons Diferentes:**
- 💖 **Inspirador** - Motivacional e transformador
- 🔥 **Urgente** - Cria senso de pressa
- 😊 **Amigável** - Conversinha de amiga
- 👑 **Exclusive** - VIP e premium
- 💰 **Economia** - Foca em descontos e economia
- 😱 **FOMO** - Fear of Missing Out
- 👥 **Social Proof** - Prova social
- 🤔 **Curiosidade** - Desperta interesse

✅ **10 Variações em Cada Categoria**
- Aberturas únicas
- Meios argumentativos
- Fechamentos persuasivos

✅ **Sistema Anti-Repetição**
- Embaralhamento aleatório
- Ciclos inteligentes
- Geração de até 500 mensagens sem padrão óbvio

✅ **3 Períodos do Dia**
- ☀️ Bom Dia
- 🌤️ Boa Tarde
- 🌙 Boa Noite

✅ **Fácil de Usar**
- Interface intuitiva
- 1 clique para gerar
- Copia pronta para postar

## 🚀 Como Usar

### 1. Instalação Local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/luhvee-message-generator.git
cd luhvee-message-generator

# Instale as dependências
pip install streamlit

# Execute o app
streamlit run luhvee_generator_completo.py
```

### 2. Deploy no Streamlit Cloud

1. Faça push do código para o GitHub
2. Vá para [streamlit.cloud](https://streamlit.io/cloud)
3. Clique em "New app"
4. Conecte seu repositório GitHub
5. Selecione o arquivo `luhvee_generator_completo.py`
6. Clique em "Deploy"

## 📋 Como Usar o App

1. **Selecione o Período**: Bom Dia, Boa Tarde ou Boa Noite
2. **Escolha o Tom**: Inspirador, Urgente, Amigável, etc.
3. **Define a Quantidade**: De 1 a 500 mensagens
4. **Clique em "Gerar mensagens infinitas"**
5. **Copie e Cole** nos seus textos/redes sociais

## 🎨 Personalizando

### Adicionar Novo Tom

1. Abra `luhvee_generator_completo.py`
2. Crie três listas para seu novo tom:

```python
aberturas_novo_tom = [
    "✨ Primeira mensagem...",
    "💖 Segunda mensagem...",
    # ... 8 mais opções
]

meios_novo_tom = [
    "seu argumento aqui",
    # ... 9 mais opções
]

fechamentos_novo_tom = [
    "💖 Chamada final.",
    # ... 9 mais opções
]
```

3. Adicione ao dicionário `BANCOS`:

```python
BANCOS = {
    # ... tons existentes
    "Seu Novo Tom": {
        "abertura": aberturas_novo_tom,
        "meio": meios_novo_tom,
        "fechamento": fechamentos_novo_tom
    }
}
```

### Alterar Links

Procure pelas linhas:
```python
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_HUB = "https://hublinks-app.streamlit.app"
```

E substitua pelos seus links.

## 📊 Estrutura do Código

```
luhvee_generator_completo.py
├── Imports e Config
├── Links (customizáveis)
├── Seleção de Período e Tom
├── 8 Bancos de Mensagens (10 variações cada)
├── Dicionário BANCOS
├── Funções:
│   ├── gerar_saudacao()
│   ├── gerar_mensagens()
│   └── adicionar_links()
└── Interface Streamlit
```

## 💡 Dicas de Marketing

### Melhor Prática de Uso

- **Bom Dia**: Use tons Inspirador ou Curiosidade
- **Boa Tarde**: Use Urgente ou FOMO
- **Boa Noite**: Use Amigável ou Social Proof

### A/B Testing

Gere mensagens com tons diferentes e teste qual tem melhor engajamento:
- Acompanhe clicks de cada tom
- Otimize baseado em dados
- Repita o tom vencedor

## 🔧 Requisitos

- Python 3.8+
- Streamlit 1.0+

## 📦 Instalação de Dependências

```bash
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install streamlit
```

## 🎯 Roadmap

- [ ] Adicionar tom de "Educação"
- [ ] Adicionar tom de "Humor"
- [ ] Integração com Excel para export
- [ ] Análise de performance
- [ ] Histórico de gerações
- [ ] Customização de emojis por tom

## 📝 Licença

MIT License - Sinta-se livre para usar, modificar e distribuir!

## 🤝 Contribuindo

1. Faça um Fork
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 💬 Suporte

Precisa de ajuda? Abra uma issue no GitHub!

---

**Feito com ❤️ para o LuhVee** 

Transformando estratégia em mensagens que vendem! 🚀

![Status](https://img.shields.io/badge/status-ativo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
