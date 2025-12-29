import streamlit as st
from utils import load_data, hot_cold_numbers, numero_info, numero_fuerte, calcular_ganancia

st.set_page_config(page_title="Pronósticos Lucky", layout="centered")

df = load_data()

st.title("🎲 Pronósticos Lucky")
st.caption("Análisis estadístico del TRIS")

st.header("⭐ Número fuerte por sorteo")
sorteo_sel = st.selectbox(
    "Selecciona sorteo",
    ["Medio Día", "De las 3", "Extra", "De las 7", "Clásico"]
)

num_fuerte, veces = numero_fuerte(df, sorteo_sel)
st.success(f"🎯 Número fuerte: {num_fuerte} (salió {veces} veces)")

st.header("🔥❄️ Números calientes y fríos")
calientes, frios = hot_cold_numbers(df, sorteo_sel)
st.write("🔥 Calientes:", calientes)
st.write("❄️ Fríos:", frios)

st.header("🔎 Consulta por número")
numero = st.text_input("Número (1 a 5 cifras)")

if numero:
    info = numero_info(df, numero)
    if not info:
        st.warning("No ha salido en la base de datos")
    else:
        st.write(info)

st.header("💰 Simulador de apuesta")
apuesta = st.number_input("Monto ($)", min_value=1)
multiplicador = st.checkbox("Multiplicador")

if st.button("Calcular") and numero:
    ganancia = calcular_ganancia(numero, apuesta, multiplicador)
    st.success(f"💵 Ganarías: ${ganancia:,.0f}")
    st.caption("🍀 Pronósticos Lucky te desea mucha suerte")
