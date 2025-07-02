import pandas as pd
from datetime import datetime

def arrondi_dixieme_standard(prix):
    dixieme = round(prix * 10)
    reste = dixieme % 10

    # Si reste entre 1-4 → arrondi vers le bas
    # Si reste entre 5-9 → arrondi vers le haut
    if reste <= 4:
        dixieme -= reste
    else:
        dixieme += (10 - reste)

    return dixieme / 10

def appliquer_silent_surge(df):
    heure_actuelle = datetime.now().hour

    df = df.copy()
    df['prix_original'] = df['prix']
    
    if heure_actuelle >= 23:
        df['prix_modifie'] = df['prix'] * 1.20
        df['prix_modifie'] = df['prix_modifie'].apply(arrondi_dixieme_standard)
    else:
        df['prix_modifie'] = df['prix']  # Pas de changement si avant 23h

    return df[['id', 'nom', 'prix_original', 'prix_modifie']]
