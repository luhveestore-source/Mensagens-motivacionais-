import pandas as pd

def exportar(dados):
    df = pd.DataFrame(dados)
    df.to_csv("mensagens_luhvee_completo.csv", index=False, encoding="utf-8-sig")
