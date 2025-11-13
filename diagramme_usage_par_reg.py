import pandas as pd
import matplotlib.pyplot as plt

def diagramme_usage_par_reg():

    # Charger le fichier CSV
    fichier_csv = pd.read_csv(r"experimentations_5G.csv",encoding="Windows-1252", sep=";", engine="python")
    fichier_csv.head()
    
    # Trouver les colonnes "Région" et "Techno"
    reg_col = [col for col in fichier_csv.columns if "Région" in col][0]
    usage_cols = [col for col in fichier_csv.columns if "Usage" in col]

    # Convertir Oui/Non → 1/0
    data = fichier_csv[[reg_col] + usage_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    # Regrouper par région et sommer les 1
    usage_par_reg = data.groupby(reg_col)[usage_cols].sum()

    # Créer un diagramme en barres empilées
    usage_par_reg.plot(kind="bar", stacked=True, figsize=(14, 8))

    plt.title("Usage 5G utilisées par région")
    plt.ylabel("Nombre d'expérimentations")
    plt.xlabel("Région")
    
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Technologies", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# Appel de la fonction
diagramme_usage_par_reg()


