import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\jaffrewe\Downloads\experimentations_5G.csv", sep=";", encoding="latin1")

def graphique_experimentations_par_acteur(df):
    compteur = {}
    
    for acteur in df["Expérimentateur"]:
        if pd.notna(acteur):
            if acteur in compteur:
                compteur[acteur] += 1
            else:
                compteur[acteur] = 1
    return compteur

def croissant(compteur):
    compteur = dict(sorted(compteur.items(), key=lambda item: item[1], reverse=True))
    acteurs = list(compteur.keys())
    valeurs = list(compteur.values())
    return acteurs, valeurs

    
def graphe(acteurs, valeurs):
    plt.figure(figsize=(8, 12))
    plt.barh(acteurs, valeurs, color='royalblue', edgecolor='black')
    plt.title("Nombre d’expérimentations par acteur (entreprises)", color='red')
    plt.xlabel("Expérimentateurs")
    plt.ylabel("Nombre d'expérimentations")
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()
    plt.show()
    
compteur = graphique_experimentations_par_acteur(df)
acteurs, valeurs = croissant(compteur)
graphe(acteurs, valeurs)

