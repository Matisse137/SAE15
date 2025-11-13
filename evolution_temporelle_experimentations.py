import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\jaffrewe\Downloads\experimentations_5G.csv", sep=";", encoding="latin1")

# Conversion de la colonne 'Début' en format date
df["Début"] = pd.to_datetime(df["Début"], errors="coerce", dayfirst=True)

# Supprimer les lignes sans date valide
df = df.dropna(subset=["Début"])

# Compter le nombre d’expérimentations par mois (ou par année selon ton choix)
evolution = df["Début"].dt.to_period("M").value_counts().sort_index()

# Tracer le graphique
plt.figure(figsize=(10,5))
plt.plot(evolution.index.astype(str), evolution.values, marker='o', linestyle='-', color='royalblue')
plt.title("Évolution temporelle des expérimentations 5G en France")
plt.xlabel("Date de début (mois)")
plt.ylabel("Nombre d’expérimentations lancées")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
