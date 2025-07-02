# 📈 Silent Surge — IC-Pricing Optimizer

> **Optimisation intelligente des prix en fonction de l’heure pour les commerces de nuit**  
> Projet personnel présenté dans le cadre du cours **Application Data**  
> **Data Storytelling Project — Paris Ynov Campus (Bachelor 3 IA & Data)**

---

## 🧠 Concept du projet

**Silent Surge** est un module stratégique d’optimisation tarifaire conçu pour répondre à un besoin réel observé sur le terrain : permettre aux commerces de proximité (snacks, épiceries de nuit…) d’**augmenter automatiquement leurs prix à certaines heures** afin de **maximiser leurs marges**, sans impacter négativement la fidélité client.

Ce projet a été imaginé comme une **mise à jour intelligente** de l’offre d’**IC-ETAG-SOLUTIONS** (étiquetage électronique), mais il pourrait également exister comme une **solution SaaS indépendante à l’échelle internationale**.

---

## 🎯 Objectifs

- 🎯 Construire un **projet concret** à fort potentiel économique et social
- 🧠 Appliquer des compétences en **data storytelling, visualisation, IA et stratégie métier**
- 🚀 Proposer une **Web App complète et présentable** en entreprise

---

## 🧑‍💻 Réalisé par

- **Sajed Ben Youssef** — Conception, Data, Streamlit, UX
- **Abdoulaye Camara** — Participation à la phase de réflexion, storytelling, design

---

## 📊 Aperçu visuel

### 📌 Présentation du notebook (Exploration + logique métier)

_Aperçu du notebook utilisé pour l’analyse initiale et l’application de la logique de majoration :_

![Image](https://github.com/user-attachments/assets/533dfe3d-33c1-4dd8-abb2-ec9427172051)

---

### 🏠 Page d’accueil de Silent Surge

_Aperçu de l’interface principale de l’application Streamlit :_

![Image](https://github.com/user-attachments/assets/14cc7537-2421-4385-b278-cb548c81b913)

---

### ⚙️ Fonctionnalités clés

_Aperçu des différentes sections de l’application :_
![Image](https://github.com/user-attachments/assets/dc3dd9c0-19cb-4dd8-b324-a91c14504edf)
![Image](https://github.com/user-attachments/assets/1f84758c-79f6-47d5-85fc-72a37758479f)
![Image](https://github.com/user-attachments/assets/dc1d1c46-643c-4250-87b7-f51c6e86168e)
![Image](https://github.com/user-attachments/assets/bd14a651-1aa8-4371-a464-41e3130b6c8f)

---

## 🛠️ Fonctionnalités principales

- ✅ **Majoration automatique des prix après une heure définie** (ex : +20% après 23h)
- ✅ **Arrondi intelligent** au dixième (ex : 2.64 → 2.6)
- ✅ **Visualisation des marges et profits avant/après**
- ✅ **Mode clair / sombre**
- ✅ **Bouton pour réinitialiser les prix**
- ✅ **Hébergement gratuit possible avec Streamlit Cloud**
![Image](https://github.com/user-attachments/assets/4b360a7f-784f-4806-9cfa-41e1c3176a4f)

---

## 📁 Arborescence

```
silent-surge/
│
├── app/
│ ├── app.py # Point d’entrée principal de l'app Streamlit
│ ├── Home.py # Page d’accueil personnalisée
│ ├── logo.png # Logo du projet
│ ├── style.css # Feuille de style Streamlit personnalisée
│ ├── pages/ # Pages par type de commerce
│ │ ├── 1_Pizzeria.py
│ │ ├── 2_Boucherie.py
│ │ └── 3_Epicerie.py
│ ├── model_cache/ # Modèles ML joblib
│ │ ├── boucherie_model.joblib
│ │ ├── epicerie_model.joblib
│ │ └── pizzeria_model.joblib
│ └── utils/
│ ├── data_loader.py # Chargement des données
│ └── model_predictor.py # Prédictions sur les ventes
│
├── app/v1/
│ ├── surge.py # Logique de majoration horaire
│ └── data/
│ ├── produits.csv
│ └── ventes_silent_surge.csv
│
├── data/
│ ├── ventes_boucherie.csv
│ ├── ventes_epicerie.csv
│ └── ventes_pizzeria.csv
│
├── models/ # (Réservé aux modèles supplémentaires)
│
├── notebooks/
│ ├── eda_silent_surge.ipynb # Analyse exploratoire (EDA)
│ ├── model_silent_surge.ipynb # Entraînement des modèles
│ └── analyse_strategique.xlsx # Support stratégique / scoring
│
├── screenshots/ # Captures d’écran pour présentation
│
├── venv/ # Environnement virtuel local (à ignorer dans Git)
├── README.md # Fichier de présentation du projet
└── requirements.txt # Liste des dépendances Python
```

## 📂 Jeu de données simulé

| produit  | heure | prix_unitaire | cout_unitaire | marge_totale | zone | saison | mois | jour |
| -------- | ----- | ------------- | ------------- | ------------ | ---- | ------ | ---- | ---- |
| RedBull  | 23    | 2.50          | 1.10          | 1.40         | Sud  | Été    | 7    | Ven  |
| Sandwich | 00    | 4.20          | 2.30          | 1.90         | Nord | Hiver  | 12   | Sam  |
| ...      | ...   | ...           | ...           | ...          | ...  | ...    | ...  | ...  |

---

## 🚀 Lancer le projet localement

### 1. Cloner le dépôt

```
git clone https://github.com/Sajedd/silent-surge.git
cd silent-surge
```

### 2. Installer les dépendances

```
pip install -r requirements.txt
```

### 3. Lancer l’application

```
streamlit run app/app.py
```
---

## 🧠 Technologies utilisées

- Python 3.11  
- Streamlit  
- Pandas / Numpy  
- Matplotlib / Seaborn  
- Darklight Theme Streamlit  
- Hébergement : Streamlit Cloud (optionnel)

---

## 📸 Présentation 

_Aperçu de la présentation (support PowerPoint)_

![Image](https://github.com/user-attachments/assets/646235a3-7109-4273-b713-b881d7995e41)
![Image](https://github.com/user-attachments/assets/a2f6514e-8274-4bbf-938e-c829db9515ed)

---

## 📈 Impact potentiel

- ✅ Augmentation des marges de **12 à 25 %** sur produits clés
- ✅ Amélioration des revenus nocturnes **sans changer les habitudes de gestion**
- ✅ Possibilité d’**industrialisation** ou d’**intégration directe** dans IC-ETAG-SOLUTIONS

---

## 🔚 Conclusion

**Silent Surge** démontre comment une idée simple, basée sur des données et une observation terrain, peut devenir une solution à fort **impact économique et stratégique**.

Ce projet illustre parfaitement l’approche **Data Storytelling** appliquée à un cas métier réel, avec une **mise en œuvre technique complète et visuellement professionnelle**.

---

📍 *Projet présenté en Juillet 2025 — Paris Ynov Campus*  
📧 *Contact : sajed.benyoussef@ynov.com*
