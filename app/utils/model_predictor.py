from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import joblib
import os

MODEL_CACHE_DIR = Path(__file__).parent.parent / "model_cache"
os.makedirs(MODEL_CACHE_DIR, exist_ok=True)

@st.cache_resource
def load_data(commerce: str) -> pd.DataFrame:
    """Charge les données avec chemin absolu et cache"""
    data_path = Path(__file__).parent.parent.parent / "data" / f"ventes_{commerce}.csv"
    
    if not data_path.exists():
        st.error(f"ERREUR : Fichier {data_path.name} introuvable")
        st.stop()
    
    return pd.read_csv(data_path)

@st.cache_resource
def get_model(commerce: str, X, y):
    """Cache les modèles entraînés pour éviter le re-entraînement"""
    cache_path = MODEL_CACHE_DIR / f"{commerce}_model.joblib"
    
    if cache_path.exists():
        return joblib.load(cache_path)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, cache_path)
    return model

def predict_best_seller(commerce: str, saison: str, zone: str) -> str:
    """Version blindée avec gestion d'erreurs et cache"""
    try:
        df = load_data(commerce)
        df["type_commerce"] = commerce

        # Encodage
        encoders = {
            col: LabelEncoder().fit(df[col]) 
            for col in ["saison", "zone", "type_commerce"]
        }
        enc_target = LabelEncoder().fit(df["produit"])

        X = df[["saison", "zone", "type_commerce"]].copy()
        for col in X.columns:
            X[col] = encoders[col].transform(X[col])
        y = enc_target.transform(df["produit"])

        # Modèle (cache automatique)
        model = get_model(commerce, X, y)

        # Prédiction
        new_data = pd.DataFrame([[saison, zone, commerce]], 
                              columns=["saison", "zone", "type_commerce"])
        
        for col in new_data.columns:
            if new_data[col].iloc[0] not in encoders[col].classes_:
                new_data[col] = encoders[col].classes_[0]  # Valeur par défaut
            new_data[col] = encoders[col].transform([new_data[col].iloc[0]])[0]

        pred = model.predict([new_data.iloc[0]])
        return enc_target.inverse_transform(pred)[0]

    except Exception as e:
        st.error(f"ERREUR : {str(e)}")
        st.stop()