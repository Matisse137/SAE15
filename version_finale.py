import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 
os.getcwd()

df = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()



def frequence_region():
    region_counts = df["Région"].value_counts()  
    
    plt.figure(figsize=(10,6))
    region_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Nombre d'expérimentations 5G par région")
    plt.xlabel("Région")
    plt.ylabel("Fréquence")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("diagramme_a_barre_region.png")

    

def usage():
    
    counts = []
    usages = []
    
    usages = df.filter(regex='^Usage').columns.tolist()
    
    for col in usages:
        if col in df.columns:
            quantite = df[col].value_counts().get(1)
            counts.append(int((quantite*100)/len(df)))
        else:
            pass
    
    x = np.array(usages)
    y = np.array(counts)
    
    plt.figure(figsize=(10, 5))
    plt.bar(x,100, color="#ff8066", edgecolor="black")
    plt.bar(x,y, color="skyblue", edgecolor="black")
    plt.title("Nombre d'expérimentations par type d'usage")
    plt.xlabel("Nombre de test réaliser")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("diagramme_usage.png")

                
def diagramme_techno():
   
    fichier_csv = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")

    techno_cols = []
    for col in fichier_csv.columns:
        if "Techno" in col:
            techno_cols.append(col)

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
    plt.savefig("diagramme_techno.png")
    
    
def departement():
    
    fichier_csv = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
    # Comptage des occurrences par département
    departement_counts = fichier_csv['Département'].value_counts()

    # Création du graphique en barres horizontales
    departement_counts.plot.barh()

    # Personnalisation du graphique
    plt.ylabel("Département")
    plt.xlabel("Nombre d'expérimentations")
    plt.title("Répartition des expérimentations par département")
    plt.savefig("diagramme_dep.png")

    
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
    
def diagramme_techno_par_region():

    # Charger le fichier CSV
    fichier_csv = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")

    # Trouver les colonnes "Région" et "Techno"
    region_col = []
    techno_cols = []
    
    for col in fichier_csv.columns:
        if "Région" == col:
            region_col = col  # On assigne la colonne "Département"
        elif "Techno" in col:
            techno_cols.append(col)  # Ajouter les colonnes "Techno"

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
    plt.savefig("diagramme_techno_par_region.png")
    
    
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
    plt.savefig("diagramme_usage_par_departement.png")
    
    
def diagramme_usage_par_reg():

    # Charger le fichier CSV
    fichier_csv = pd.read_csv(r"experimentations_5G.csv",encoding="Windows-1252", sep=";", engine="python")
    fichier_csv.head()
    
    # Trouver les colonnes "Région" et "Techno"
    reg_col = []
    usage_cols = []
    
    for col in fichier_csv.columns:
        if "Région" == col:
            reg_col = col  # On assigne la colonne "Département"
        elif "Usage" in col:
            usage_cols.append(col)  # Ajouter les colonnes "Techno"


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
    plt.savefig("diagramme_usage_par_region.png")
    
df = pd.read_csv(r"experimentations_5G.csv", sep=";", encoding="latin1")

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
    plt.savefig("nombre_temporelle_experimentations")
    

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
    plt.savefig("techno_region.png")
    
    
def tracer_evolution(df):
    # Conversion de la colonne 'Début' en format date
    df["Début"] = pd.to_datetime(df["Début"], errors="coerce", dayfirst=True)

    # Supprimer les lignes sans date valide
    df = df.dropna(subset=["Début"])

    # Compter le nombre d’expérimentations par mois
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
    plt.savefig("evolution_temporelle_experimentations.png")

    return evolution  # facultatif

    
# Appel de toute les fonctions

frequence_region() 
usage()
diagramme_techno()
departement()
diagramme_circulaire()
diagramme_techno_par_dep()
diagramme_techno_par_region()
diagramme_usage_par_dep()
diagramme_usage_par_reg()
diagramme_techno()
compteur = graphique_experimentations_par_acteur(df)
acteurs, valeurs = croissant(compteur)
graphe(acteurs, valeurs)



    

