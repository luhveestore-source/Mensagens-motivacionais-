# 💖 LuhVee - Mensagens de Felicidade

Um gerador de mensagens positivas, motivacionais e amorosas para deixar o dia de seus clientes mais feliz! 

Mensagens que vêm direto do coração, assinadas com carinho: **Bjs da Luh da LuhVee ❤️**

## ✨ Características

✅ **8 Vibes Diferentes:**
- 💖 **Amor Próprio** - Valorizar-se e se amar
- 🙏 **Gratidão** - Agradecer pelas bênçãos
- 🚀 **Motivação** - Inspirar a continuar
- ☀️ **Positividade** - Energia positiva
- 👑 **Autoconfiança** - Acreditar em si
- 💆‍♀️ **Bem-estar** - Cuida da saúde mental
- 🌅 **Esperança** - Acreditar que melhora
- 🎉 **Celebração** - Comemorar vitórias

✅ **Mensagens 100% Positivas**
- Nenhuma mensagem sobre vendas
- Foco total em bem-estar emocional
- Inspiração genuína

✅ **Assinatura Pessoal**
- Todas as mensagens terminam com: **Bjs da Luh da LuhVee ❤️**
- Cria conexão pessoal com seus clientes

✅ **3 Períodos do Dia**
- ☀️ Bom Dia
- 🌤️ Boa Tarde
- 🌙 Boa Noite

## 🚀 Como Usar

### 1. Instalação Local

```bash
git clone https://github.com/seu-usuario/luhvee-message-generator.git
cd luhvee-message-generator
pip install -r requirements.txt
streamlit run luhvee_felicidade.py
```

### 2. No App

1. Escolha o **período do dia**
2. Selecione uma **vibe/energia**
3. Defina a **quantidade** (1-500)
4. Clique em **"Gerar mensagens de felicidade"**
5. Copie e compartilhe com seus clientes! 💖

## 💡 Exemplos de Mensagens

### Vibe: Amor Próprio

```
☀️ Bom dia!

💖 Você merece todo o amor do mundo... 
cuide de si como se fosse alguém especial.
💖 Você merece tudo isso e muito mais.

Bjs da Luh da LuhVee ❤️
```

### Vibe: Motivação

```
☀️ Bom dia!

🚀 Você é mais capaz do que imagina... 
porque você vem vencendo todos os dias.
🚀 Você consegue, vai conseguir.

Bjs da Luh da LuhVee ❤️
```

### Vibe: Bem-estar

```
🌙 Boa noite!

🧘‍♀️ Respire, você está bem... 
porque sua mente merecia parar.
🧘‍♀️ Respire fundo, você está segura.

Bjs da Luh da LuhVee ❤️
```

## 🎯 Casos de Uso

✅ **Instagram Stories** - Poste diariamente para seus seguidores
✅ **WhatsApp Broadcast** - Envie para sua lista de clientes
✅ **Email Marketing** - Mensagens motivacionais periódicas
✅ **Lives e Transmissões** - Comece suas transmissões com positividade
✅ **Comunidades** - Compartilhe no grupo da comunidade
✅ **Redes Sociais** - TikTok, Pinterest, Threads

## 📊 8 Vibes Explicadas

| Vibe | Quando usar | Exemplo |
|------|-----------|---------|
| Amor Próprio | Quando quer inspirar autoestima | Segunda de manhã |
| Gratidão | Para reconhecer bênçãos | Domingo |
| Motivação | Para impulsionar ação | Segunda ou quarta |
| Positividade | Para elevar energia | Qualquer dia |
| Autoconfiança | Para fortalecer segurança | Antes de eventos |
| Bem-estar | Para tranquilidade | Noite ou dia estressante |
| Esperança | Para momentos difíceis | Qualquer hora |
| Celebração | Para comemorar | Quando tiver motivo |

## 🎨 Personalizando

### Mudar a Assinatura

Abra `luhvee_felicidade.py` e procure por:

```python
msg = f"{saudacao}\n\n{next(ciclo_abertura)} {next(ciclo_meio)}.\n{next(ciclo_fechamento)}\n\nBjs da Luh da LuhVee ❤️"
```

Troque `"Bjs da Luh da LuhVee ❤️"` por sua assinatura personalizada!

### Adicionar Nova Vibe

1. Crie 3 listas com 10 frases cada:

```python
aberturas_sua_vibe = [
    "✨ Sua mensagem aqui...",
    # ... 9 mais
]

meios_sua_vibe = [
    "seu argumento aqui",
    # ... 9 mais
]

fechamentos_sua_vibe = [
    "✨ Seu fechamento aqui.",
    # ... 9 mais
]
```

2. Adicione ao dicionário `BANCOS`:

```python
BANCOS = {
    # ... outras vibes
    "Sua Nova Vibe": {
        "abertura": aberturas_sua_vibe,
        "meio": meios_sua_vibe,
        "fechamento": fechamentos_sua_vibe
    }
}
```

## 💝 Por que Mensagens Positivas?

✨ **Conexão Genuína** - Cria laço emocional com seus clientes
✨ **Diferencial** - Ninguém mais faz isso do jeito que você faz
✨ **Lealdade** - Clientes amam ser cuidados emocionalmente
✨ **Engajamento** - Positividade gera compartilhamentos
✨ **Marca Pessoal** - Você fica conhecido por trazer felicidade
✨ **Impacto Real** - Muda o dia de alguém de verdade

## 📱 Dicas de Uso

1. **Consistência** - Poste no mesmo horário
2. **Diversidade** - Varie os tons/vibes
3. **Autenticidade** - Acredite no que está compartilhando
4. **Engajamento** - Responda quem comentar
5. **Regularidade** - Faça isto um hábito

## 🚀 Deploy

```bash
# Criar repositório no GitHub
git init
git add .
git commit -m "LuhVee Felicidade - Mensagens de amor"
git branch -M main
git remote add origin https://github.com/seu-usuario/luhvee-felicidade.git
git push -u origin main

# Deploy no Streamlit Cloud
# 1. Vá para streamlit.io/cloud
# 2. Conecte seu GitHub
# 3. Selecione seu repositório
# 4. Arquivo: luhvee_felicidade.py
# 5. Deploy!
```

## 💖 Impacto que Você Vai Fazer

Cada mensagem que você gera pode:
- ✨ Salvar alguém de um dia ruim
- 💖 Fortalecer a autoestima de uma mulher
- 🌟 Inspirar alguém a continuar
- 💪 Dar força para enfrentar dificuldades
- 🎯 Mostrar que alguém se importa
- 🌈 Trazer um sorriso sincero

## 🎁 Bônus: Cronograma Sugerido

**Segunda:** Motivação 🚀
**Terça:** Autoconfiança 👑
**Quarta:** Positividade ☀️
**Quinta:** Amor Próprio 💖
**Sexta:** Celebração 🎉
**Sábado:** Bem-estar 💆‍♀️
**Domingo:** Gratidão 🙏

---

**Pronto para espalhar felicidade?** 💖

Cada mensagem é uma semente de alegria plantada no coração de alguém.

**Bjs da Luh da LuhVee ❤️**
