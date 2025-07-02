# app/app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# === Fonctions de chargement ===
@st.cache_data
def load_data(client):
    path = os.path.join("data", f"ventes_{client.lower()}.csv")
    df = pd.read_csv(path, parse_dates=['date_vente'])
    return df

# === Fonction d'affichage ===
def show_dashboard(df, client):
    st.header(f"Dashboard - {client.title()}")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Ventes", f"{df['quantite'].sum():,}")
    with col2:
        st.metric("Marge Totale (€)", f"{df['marge_totale'].sum():.2f} €")

    st.subheader("Top Produits")
    top_produits = df.groupby("produit")["quantite"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_produits)

    st.subheader("Répartition des ventes par saison")
    fig = px.histogram(df, x="saison", y="quantite", color="saison", histfunc="sum")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Heatmap horaire des ventes")
    heat_df = df.groupby(["jour", "heure"])["quantite"].sum().unstack(fill_value=0)
    st.dataframe(heat_df.style.background_gradient(cmap='Blues'))

    st.subheader("Analyse géographique")
    fig = px.box(df, x="zone", y="marge_totale", points="all", title="Marge par zone")
    st.plotly_chart(fig, use_container_width=True)

# === Streamlit App ===
st.set_page_config(page_title="Silent Surge", layout="wide", page_icon="📊")
st.title("📊 Silent Surge - Optimisation des ventes")

client = st.sidebar.selectbox("Choisir un commerce", ["pizzeria", "boucherie", "epicerie"])
show_dashboard(load_data(client), client)

# === Bonus: bouton de majoration ===
if st.sidebar.button("Activer la majoration après 23h"):
    st.sidebar.success("Majoration activée : +20% après 23h (simulation)")
