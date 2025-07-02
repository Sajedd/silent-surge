import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go


st.set_page_config(page_title="Silent Surge", layout="wide")

st.title("🌙 Silent Surge PRO — Optimiseur de marge IC-SOLUTIONS")
st.image("app/logo.png") 

st.markdown("Bienvenue sur Silent Surge – un outil de **data storytelling prédictif** pour les commerces alimentaires locaux.")
st.markdown("""
💡 Cette application permet de :
- Visualiser vos ventes selon les saisons et la zone géographique
- Prédire les best-sellers à venir
- Adapter les stocks en fonction des tendances

Utilisez le menu à gauche pour explorer chaque commerce.
""")


# Upload CSV
uploaded_file = st.file_uploader("📂 Importez votre catalogue produit (.csv)", type="csv")

# Simulation d’heure personnalisée
simulate = st.checkbox("🕒 Simuler une heure personnalisée ?")
if simulate:
    heure_simulee = st.time_input("Choisissez une heure simulée", value=datetime.time(2, 0))
    heure_actuelle = heure_simulee
else:
    heure_actuelle = datetime.datetime.now().time()

# Fonction pour vérifier si Silent Surge doit s'activer
def silent_surge_active(heure):
    return heure >= datetime.time(23, 0) or heure <= datetime.time(4, 59)

# Fonction d’application de la majoration
def appliquer_silent_surge(df, heure):
    if silent_surge_active(heure):
        df['Prix après Silent Surge (€)'] = df['Prix (€)'] * 1.2
        df['Prix après Silent Surge (€)'] = df['Prix après Silent Surge (€)'].apply(lambda x: round(x * 10) / 10)
    else:
        df['Prix après Silent Surge (€)'] = df['Prix (€)']
    return df

# Si fichier uploadé
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📊 Données originales")
    st.dataframe(df, use_container_width=True)

    # Application Silent Surge
    df_modifie = appliquer_silent_surge(df.copy(), heure_actuelle)

    st.subheader("🔍 Visualisation après Silent Surge")
    st.dataframe(df_modifie, use_container_width=True)

    # Affichage graphique avant/après
    fig = go.Figure(data=[
        go.Bar(name='Avant', x=df['Produit'], y=df['Prix (€)'], marker_color='indianred'),
        go.Bar(name='Après', x=df_modifie['Produit'], y=df_modifie['Prix après Silent Surge (€)'], marker_color='lightgreen')
    ])
    fig.update_layout(
        title="Comparaison des prix (Avant vs Après Silent Surge)",
        xaxis_title="Produit",
        yaxis_title="Prix (€)",
        barmode='group',
        template='plotly_white'
    )
    st.plotly_chart(fig)

    # Téléchargement CSV
    csv = df_modifie.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Télécharger le nouveau fichier CSV", csv, "produits_silent_surge.csv", "text/csv")
else:
    st.info("Veuillez importer un fichier .csv contenant les colonnes 'Produit' et 'Prix (€)'.")
