import pandas as pd
import matplotlib.pyplot as plt

def diagramme_techno_par_dep():

    # Charger le fichier CSV
    fichier_csv = pd.read_csv(r"experimentations_5G.csv",encoding="Windows-1252", sep=";", engine="python")

    # Trouver les colonnes "Département" et "Techno"
    dep_col = []
    techno_cols = []
    
    for col in fichier_csv.columns:
        if "Département" == col:
            dep_col = col  # On assigne la colonne "Département"
        elif "Techno" in col:
            techno_cols.append(col)  # Ajouter les colonnes "Techno"

    # Convertir Oui/Non → 1/0
    data = fichier_csv[[dep_col] + techno_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    # Regrouper par département et sommer les 1
    techno_par_dep = data.groupby(dep_col)[techno_cols].sum()

    # Créer un diagramme en barres empilées
    techno_par_dep.plot(kind="bar", stacked=True, figsize=(14, 6))

    plt.title("Technologies 5G utilisées par département")
    plt.ylabel("Nombre d'expérimentations")
    plt.xlabel("Département")
    
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Technologies", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("diagramme_techno_par_dep.png")
    plt.show()

# Appel de la fonction
diagramme_techno_par_dep()



    



