# 📈 Silent Surge — IC-Pricing Optimizer

> **Optimisation intelligente des prix en fonction de l’heure pour les commerces de nuit**  
> Projet personnel présenté dans le cadre du cours **Application Data**  
> **Data Storytelling Project — Paris Ynov Campus (Master 1 IA & Data)**

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

📸 **[Insérer capture d’écran du notebook ici]**

---

### 🏠 Page d’accueil de Silent Surge

_Aperçu de l’interface principale de l’application Streamlit :_

📸 **[Insérer capture d’écran de la page d’accueil de l’app ici]**

---

### ⚙️ Fonctionnalités clés

_Aperçu des différentes sections de l’application :_

- Visualisation marge avant / après majoration  
  📸 **[Insérer capture section "Avant vs Après"]**
- Affichage des produits impactés  
  📸 **[Insérer capture d’un produit avec majoration active]**
- Bouton retour aux prix d’origine  
  📸 **[Insérer capture bouton ou section]**

---

## 🛠️ Fonctionnalités principales

- ✅ **Majoration automatique des prix après une heure définie** (ex : +20% après 23h)
- ✅ **Arrondi intelligent** au dixième (ex : 2.64 → 2.6)
- ✅ **Visualisation des marges et profits avant/après**
- ✅ **Mode clair / sombre**
- ✅ **Bouton pour réinitialiser les prix**
- ✅ **Hébergement gratuit possible avec Streamlit Cloud**

---

## 📁 Arborescence

```
silent-surge/
│
├── data/
│ └── silent_surge_dataset.csv # Données simulées
│
├── notebooks/
│ ├── 01_exploration.ipynb # Exploration des données
│ └── 02_majoration_logique.ipynb # Définition de la logique métier
│
├── app/
│ └── app.py # App Streamlit principale
│
├── README.md # Ce fichier
└── requirements.txt # Librairies nécessaires
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

```bash
git clone https://github.com/ton-utilisateur/silent-surge.git
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

_Aperçu de la présentation réalisée devant le jury / professeur (support PowerPoint)_

📸 **[Insérer ici une capture d’écran de la présentation orale]**

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
