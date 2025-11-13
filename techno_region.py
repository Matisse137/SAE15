import pandas as pd
import matplotlib.pyplot as plt

def diagramme_techno_par_region():

    # Charger le fichier CSV
    fichier_csv = pd.read_csv(r"C:/Users/roubaabd/Downloads/experimentations_5G.csv",
                              encoding="Windows-1252", sep=";", engine="python")

    # Trouver les colonnes "Région" et "Techno"
    region_col = [col for col in fichier_csv.columns if "Eégion" in col][0]
    techno_cols = [col for col in fichier_csv.columns if "Techno" in col]

    # Convertir Oui/Non → 1/0
    data = fichier_csv[[region_col] + techno_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    # Regrouper par région et sommer les 1
    techno_par_region = data.groupby(region_col)[techno_cols].sum()

    # Créer un diagramme en barres empilées
    techno_par_region.plot(kind="bar", stacked=True, figsize=(12, 6))

    plt.title("Technologies 5G utilisées par région")
    plt.ylabel("Nombre d'expérimentations")
    plt.xlabel("Régions")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Technologies", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# Appel de la fonction
diagramme_techno_par_region()

    