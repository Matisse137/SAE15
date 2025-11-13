import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
fichier_csv = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")

# Fonction pour afficher le graphique en barres horizontales
def departement():
    # Comptage des occurrences par département
    departement_counts = fichier_csv['Département'].value_counts()

    # Création du graphique en barres horizontales
    departement_counts.plot.barh()

    # Personnalisation du graphique
    plt.ylabel("Département")
    plt.xlabel("Nombre d'expérimentations")
    plt.title("Répartition des expérimentations par département")

    # Affichage du graphique
    plt.show()

departement()

