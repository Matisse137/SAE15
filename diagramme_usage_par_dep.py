import pandas as pd
import matplotlib.pyplot as plt

def diagramme_usage_par_dep():

    # Charger le fichier CSV
    fichier_csv = pd.read_csv(r"experimentations_5G.csv",encoding="Windows-1252", sep=";", engine="python")
    fichier_csv.head()
    
    # Trouver les colonnes "Région" et "Techno"
    dep_col = []
    usage_cols = []
    
    for col in fichier_csv.columns:
        if "Département" == col:
            dep_col = col  # On assigne la colonne "Département"
        elif "Usage" in col:
            usage_cols.append(col)  # Ajouter les colonnes "Techno"

    # Convertir Oui/Non → 1/0
    data = fichier_csv[[dep_col] + usage_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    # Regrouper par région et sommer les 1
    usage_par_dep = data.groupby(dep_col)[usage_cols].sum()

    # Créer un diagramme en barres empilées
    usage_par_dep.plot(kind="bar", stacked=True, figsize=(14, 8))

    plt.title("Usage 5G utilisées par département")
    plt.ylabel("Nombre d'expérimentations")
    plt.xlabel("Département")
    
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Technologies", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# Appel de la fonction
diagramme_usage_par_dep()

