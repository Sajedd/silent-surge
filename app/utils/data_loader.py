from pathlib import Path
import pandas as pd
import streamlit as st

def load_data(domain: str) -> pd.DataFrame:
    """Charge les données de manière infaillible"""
    try:
        # Chemin absolu garanti
        data_path = Path(__file__).parent.parent.parent / "data" / f"ventes_{domain}.csv"
        
        if not data_path.exists():
            st.error(f"ERREUR CRITIQUE : Fichier {data_path} introuvable")
            st.stop()
            
        return pd.read_csv(data_path)
    
    except Exception as e:
        st.error(f"ERREUR FATALE : {str(e)}")
        st.stop()