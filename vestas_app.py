import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="centered", page_title="Analiză VESTAS", page_icon="📈")

st.title("📈 Analiză Investiție: VESTAS WIND SYSTEMS")
st.subheader("Cod bursier: `VWS.CO`")

# Obține datele de la yfinance
actiune = yf.Ticker("VWS.CO")
info = actiune.info
pret = info.get("currentPrice", "N/A")
recomandare = info.get("recommendationKey", "N/A")

col1, col2 = st.columns(2)
col1.metric("💰 Preț curent (DKK)", pret)
col2.metric("📌 Recomandare investitori", recomandare.upper())

with st.expander("🧩 Argumente strategice pentru investiție"):
    st.markdown("""
    - ✔️ Lider global în energie eoliană  
    - ✔️ Tehnologie verde – trend sustenabil și viitor sigur  
    - ✔️ Cerere în creștere pentru surse regenerabile  
    - ✔️ Parteneriate strategice cu guverne & corporații globale  
    - 📈 Piața energiei verzi este estimată să crească cu 80% până în 2030  
    """)

st.warning("⚠️ Investițiile pe piața bursieră implică riscuri. Informați-vă corect!")

# Graficul cu evoluția acțiunii
data = actiune.history(period="10d")

if not data.empty:
    zile = pd.to_datetime(data.index).strftime('%d %b')
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(zile, data["Close"], marker='o', linestyle='-', color='#007f5f', linewidth=2)
    ax.set_title("📊 Evoluția valorii acțiunii VESTAS (10 zile)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preț (DKK)")
    ax.grid(True, linestyle='--', alpha=0.5)

    for i, val in enumerate(data["Close"]):
        ax.annotate(f'{val:.1f}', (i, val), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

    st.pyplot(fig)
else:
    st.info("Datele nu sunt disponibile momentan.")
