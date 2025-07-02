import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_loader import load_data
from utils.model_predictor import predict_best_seller

st.set_page_config(page_title="Boucherie", layout="wide")
st.title("🥩 Analyse - Boucherie")

# Chargement des données
df = load_data("boucherie")

# Aperçu des données
st.subheader("📊 Aperçu des ventes")
st.dataframe(df.head())

# Top produits par saison
st.subheader("🔥 Top produits par saison")
saison_select = st.selectbox("Choisissez une saison :", df["saison"].unique())
df_saison = df[df["saison"] == saison_select]
top_products = df_saison["produit"].value_counts().head(5)

fig1, ax1 = plt.subplots()
sns.barplot(x=top_products.values, y=top_products.index, ax=ax1, palette="rocket")
ax1.set_xlabel("Quantité vendue")
ax1.set_title(f"Top 5 produits - Saison {saison_select}")
st.pyplot(fig1)

# Zones géographiques les plus rentables (temporaire → nombre de ventes)
st.subheader("📍 Zones géographiques - Volume de ventes")
zone_ca = df["zone"].value_counts()

fig2, ax2 = plt.subplots()
sns.barplot(x=zone_ca.values, y=zone_ca.index, ax=ax2, palette="Blues_d")
ax2.set_xlabel("Nombre de ventes")
ax2.set_title("Nombre de ventes par zone géographique")
st.pyplot(fig2)

# Prédiction best-seller
st.subheader("🔮 Prédiction du produit best-seller")
saison_pred = st.selectbox("Saison prédiction", df["saison"].unique(), key="saison_boucherie")
zone_pred = st.selectbox("Zone prédiction", df["zone"].unique(), key="zone_boucherie")

if st.button("Prédire le best-seller 🥩"):
    produit = predict_best_seller("boucherie", saison_pred, zone_pred)
    st.success(f"👉 Le produit best-seller prédictif est : **{produit}**")
