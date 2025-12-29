import pandas as pd
from collections import Counter

PAGOS = {
    1: 5,
    2: 50,
    3: 500,
    4: 5000,
    5: 50000
}

def load_data():
    return pd.read_csv("data/tris.csv")

def hot_cold_numbers(df, sorteo=None, top=7):
    if sorteo:
        df = df[df["sorteo"] == sorteo]

    conteo = Counter(df["numero"])
    calientes = conteo.most_common(top)
    frios = conteo.most_common()[:-top-1:-1]
    return calientes, frios

def numero_info(df, numero):
    sub = df[df["numero"] == numero]
    total = len(sub)
    if total == 0:
        return None

    ultima = sub.iloc[-1]
    por_sorteo = sub["sorteo"].value_counts().to_dict()

    return {
        "total": total,
        "fecha": ultima["fecha"],
        "hora": ultima["hora"],
        "sorteo": ultima["sorteo"],
        "por_sorteo": por_sorteo
    }

def numero_fuerte(df, sorteo):
    sub = df[df["sorteo"] == sorteo]
    conteo = Counter(sub["numero"])
    return conteo.most_common(1)[0]

def calcular_ganancia(numero, apuesta, multiplicador=False):
    digitos = len(numero)
    base = PAGOS.get(digitos, 0)
    ganancia = apuesta * base
    if multiplicador:
        ganancia *= 3
    return ganancia
