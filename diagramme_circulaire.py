import pandas as pd
import matplotlib.pyplot as plt

def diagramme_circulaire():
    fichier_csv=pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
    fichier_csv.head()

    bande_counts = fichier_csv['Bande de fréquences'].value_counts()

    # Diagramme circulaire automatique
    plt.figure(figsize=(7,7))
    plt.pie(
        bande_counts.values,                # valeurs à tracer
        labels=bande_counts.index,          # noms des bandes
        autopct='%1.1f%%',                  # pourcentage formaté
        startangle=105,
        counterclock=False
    )
    plt.title("Répartition des expérimentations par bande de fréquence (GHz)")
    plt.savefig("diagramme_circulaire.png")
    plt.show()

diagramme_circulaire()





