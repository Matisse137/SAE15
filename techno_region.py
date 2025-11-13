import pandas as pd
import matplotlib.pyplot as plt

def diagramme_techno():
   
    fichier_csv = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")

    techno_cols = []
    region_col = []
    
    for col in fichier_csv.columns:
        if "Région" in col:  # On cherche la colonne "Région"
            region_col = col
        if "Techno" in col:  # On cherche les colonnes "Techno"
            techno_cols.append(col)  # On assigne la colonne "Département"
       
        
    data = fichier_csv[techno_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    nb_1 = data.sum()
    nb_0 = len(data) - nb_1

    plt.figure(figsize=(10, 5))
    plt.bar(techno_cols, nb_1, label="1 (Présence)", color="skyblue")
    plt.bar(techno_cols, nb_0, bottom=nb_1, label="0 (Absence)", color="lightcoral")

    plt.title("Réparation des technologies 5G par type de Techno")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Appel de la fonction
diagramme_techno()
