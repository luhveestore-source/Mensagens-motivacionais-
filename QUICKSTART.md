# 🚀 Quick Start - LuhVee Message Generator

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/seu-usuario/luhvee-message-generator.git
cd luhvee-message-generator
```

### 2️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Execute Localmente
```bash
streamlit run luhvee_generator_completo.py
```

O app abrirá em: `http://localhost:8501`

## ☁️ Deploy no Streamlit Cloud (Grátis!)

1. **Faça login** em [streamlit.cloud](https://streamlit.io/cloud)
2. **Conecte seu GitHub**
3. **Clique em "New app"**
4. Selecione:
   - Repository: `seu-usuario/luhvee-message-generator`
   - Branch: `main`
   - File: `luhvee_generator_completo.py`
5. **Deploy!** 🎉

Sua URL será algo como: `https://luhvee-message-generator.streamlit.app`

## 📱 Usar o App

1. Escolha o **período do dia**
2. Selecione um **tom de mensagem**
3. Defina a **quantidade** (1-500)
4. Clique em **"Gerar mensagens infinitas"**
5. **Copie** e **cole** nos seus textos

## ⚙️ Customizar Links

Abra `luhvee_generator_completo.py` e encontre:

```python
# 🔗 SEUS LINKS
LINK_PESQUISA = "https://pesquisa-luhvee.streamlit.app"
LINK_HUB = "https://hublinks-app.streamlit.app"
```

Substitua pelos seus links!

## 🎨 8 Tons Disponíveis

| Ton | Melhor Para | Emoji |
|-----|-----------|-------|
| Inspirador | Motivação | 💖 |
| Urgente | Criar pressa | 🔥 |
| Amigável | Conexão pessoal | 😊 |
| Exclusive | VIP/Premium | 👑 |
| Economia | Descontos | 💰 |
| FOMO | Medo de perder | 😱 |
| Social Proof | Prova social | 👥 |
| Curiosidade | Despertador interesse | 🤔 |

## 📊 Exemplo de Uso

**Entrada:**
- Período: Bom Dia
- Tom: Urgente
- Quantidade: 3

**Saída:**
```
☀️ Bom dia!

⏰ Isso não vai durar... não fica mais que 2 horas disponível.
🔥 Aproveita AGORA.

🔍 Pesquisa: https://pesquisa-luhvee.streamlit.app
🌐 Hub: https://hublinks-app.streamlit.app

---

☀️ Bom dia!

🔥 Segundos contam... estoque se esgotando agora.
⚡ Sem esperar mais.

🔍 Pesquisa: https://pesquisa-luhvee.streamlit.app
🌐 Hub: https://hublinks-app.streamlit.app

---

☀️ Bom dia!

⚡ Muita gente está pegando agora... fila andando rápido demais.
🎯 Toma a ação agora.

🔍 Pesquisa: https://pesquisa-luhvee.streamlit.app
🌐 Hub: https://hublinks-app.streamlit.app
```

## 🆘 Troubleshooting

**App não abre?**
```bash
pip install --upgrade streamlit
streamlit run luhvee_generator_completo.py
```

**Erro de importação?**
```bash
pip install -r requirements.txt --force-reinstall
```

**Quer fazer deploy local (sem Streamlit Cloud)?**
```bash
streamlit run luhvee_generator_completo.py --server.port 3000
```

## 📚 Mais Informações

- 📖 Veja o [README.md](README.md) para documentação completa
- 💬 Abra uma [Issue](https://github.com/seu-usuario/luhvee-message-generator/issues) para dúvidas
- 🤝 Contribuições são bem-vindas!

---

**Pronto para gerar mensagens incríveis?** 🚀

Divirta-se e bom marketing! 💖
