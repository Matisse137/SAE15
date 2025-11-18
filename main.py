import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk  # pour insérer une image
import folium
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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
    plt.close()
    

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
    plt.close()

                
def diagramme_techno():
   
    fichier_csv = df

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

    plt.title("Répartion des technologies 5G par type de Techno")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("diagramme_techno.png")
    plt.close()
    
def departement():
    
    fichier_csv = df
    # Comptage des occurrences par département
    departement_counts = fichier_csv['Département'].value_counts()

    # Création du graphique en barres horizontales
    departement_counts.plot.barh()

    # Personnalisation du graphique
    plt.ylabel("Département")
    plt.xlabel("Nombre d'expérimentations")
    plt.title("Répartition des expérimentations par département")
    plt.savefig("diagramme_dep.png")
    plt.close()
    
def diagramme_circulaire():
    fichier_csv = df
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
    plt.close()
    
def diagramme_techno_par_dep():

    # Charger le fichier CSV
    fichier_csv = df

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
    plt.close()
    
def diagramme_techno_par_region():

    # Charger le fichier CSV
    fichier_csv = df

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
    plt.close()
    
def diagramme_usage_par_dep():

    # Charger le fichier CSV
    fichier_csv = df
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
    plt.close()
    
def diagramme_usage_par_reg():

    # Charger le fichier CSV
    fichier_csv = df
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
    plt.close()
    
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
    plt.close()

def diagramme_techno():
   
    fichier_csv = df

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
    plt.close()
    
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
    plt.close()
    return evolution  # facultatif

    
# Appel de toute les fonctions
def launch_pyplot():
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
    plt.close()

def launch_folium(file_name):
    # Créer une carte
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    
    # Enregistrer dans un fichier HTML
    fichier = "carte_interactive.html"
    carte.save(fichier)
    
    # Charger le fichier CSV
    df = pd.read_csv(rf"{file_name}", encoding="Windows-1252", sep=";", engine="python")
    df.head()
    
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    
    for i in range(len(df)):
        latitude, longitude, Bande_de_fréquences = df.loc[i, ["Latitude", "Longitude", "Bande de fréquences"]]
        latitude = float(latitude.replace(',', '.'))
        longitude = float(longitude.replace(',', '.'))
        regions = df.loc[i, "Région"]
        bande = df.loc[i, "Bande de fréquences"]
        description = df.loc[i, "Description"]
        numero_arcep = df.loc[i, "Numéro de la décision d'autorisation de l'Arcep"]
    
        # Créer le texte du popup en HTML
        popup_text = f"""
        <b>Région :</b> {regions}<br>
        <b>Numéro ARCEP :</b> {numero_arcep}<br>
        <b>Bande de fréquences :</b> {bande}<br>
        <b>Description :</b> {description}
        """
    
        # Ajouter le marqueur
        folium.Marker(
            location=[latitude, longitude],
            tooltip="Cliquer pour plus d'infos",  
            popup=popup_text  # affiché au clic
        ).add_to(carte)
    
    carte.save("carte_interactive.html")

def empty():
    return

# variable globales qui peuvent êtres accedées partout dans le code
global_window = None
global_top_frame = None
global_bottom_frame = None
global_file_entry = None

# Les fonctions qui suivent utilisent tkinter,
# elles servent à ajouter les éléments

def init_window_frame(title, size):
    """
    Crée une fenêtre principale avec un frame interne.

    Returns
    -------
    window : tk.Tk()
        renvoie l'objet fenêtre.
    frame : ttk.Frame()
        renvoie le frame associé à la fenêtre.
    """
    global global_window
    global global_top_frame
    global global_bottom_frame
    global global_file_entry
    
    window = tk.Tk() 
    window.title(title) 
    window.geometry(size)
    
    top_frame = ttk.Frame(window)
    top_frame.grid(row=0)
    bottom_frame = ttk.Frame(window)
    bottom_frame.grid(row=1)
    
    global_window = window
    global_top_frame = top_frame
    global_bottom_frame = bottom_frame
    
    add_label(top_frame, "Veuillez entrer le nom du fichier CSV : ", 0, 0, 1, 0)
    global_file_entry = add_entry(top_frame, 0, 1, 1, 0)
    add_button(top_frame, "valider", btn_file, 1, 1, 2, 2)

def flush(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def add_label(frame, txt, x, y, pad_x, pad_y):
    label = ttk.Label(frame, text=txt)
    label.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    return label

def add_button(frame, txt, func, x, y, pad_x, pad_y):
    button = ttk.Button(frame, text=txt, command=func)
    button.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    return button


def add_entry(frame, x, y, pad_x, pad_y):
    entry = ttk.Entry(frame)
    entry.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    return entry


def add_img(file_name, anchor_, size_x, size_y, x, y, pad_x, pad_y):
    global global_bottom_frame
    
    flush(global_bottom_frame)
    
    img = Image.open(file_name)
    img = img.resize((size_x, size_y))
    tk_image = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(global_bottom_frame, width=size_x, height=size_y)
    canvas.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    canvas.create_image(0, 0, image=tk_image, anchor=anchor_)
    
    canvas.image = tk_image
    return canvas

# Les fonctions qui suivent seront les actions de chaques boutons
def btn_file():
    global global_top_frame
    global global_file_entry
    
    file_name = global_file_entry.get()
    
    if not os.path.isfile(file_name) or not file_name.lower().endswith(".csv"):
        error_case("Le fichier n'existe pas ou n'est pas un CSV valide.")
        return
    
    try:
        # Vérifie que pandas peut le lire
        pd.read_csv(file_name, sep=";", encoding="Windows-1252", engine="python")
    except Exception as e:
        error_case(f"Erreur lors de la lecture du CSV : {str(e)}")
        return
    
    launch_pyplot()    
    
    add_button(global_top_frame, "Expérimentations par départements", btn_1, 0, 0, 2, 2)
    add_button(global_top_frame, "Expérimentations par bandes de fréquences", btn_2, 0, 1, 2, 2)
    add_button(global_top_frame, "Technologie par départements", btn_3, 0, 2, 2, 2)
    add_button(global_top_frame, "Technologie par régions", btn_4, 0, 3, 2, 2)
    add_button(global_top_frame, "Usage par départements", btn_5, 1, 0, 2, 2)
    add_button(global_top_frame, "Usage par régions", btn_6, 1, 1, 2, 2)
    add_button(global_top_frame, "Présence de technologies par régions", btn_7, 1, 2, 2, 2)
    add_button(global_top_frame, "Ouvrir la carte interactive", btn_8, 1, 3, 2, 2)
        
    
def btn_1():
    add_img( "diagramme_techno.png", "nw", 800, 600, 0, 0, 0, 0)
    return

def btn_2():
    
    return 

def btn_3():
    
    return 

def btn_4():
    add_img( "diagramme_a_barre_region.png", "nw", 800, 600, 0, 0, 0, 0)
    return 

def btn_5():
    
    return

def btn_6():
    add_img( "diagramme_usage.png", "nw", 800, 600, 0, 0, 0, 0)
    return 

def btn_7():
    
    return

def btn_8():
    webbrowser.open("carte_interactive.html")
    return

# Fonction de lancement de la fenêtre
def error_case(txt):
    global global_bottom_frame
    global global_top_frame
    global global_window
    
    flush(global_bottom_frame)
    flush(global_top_frame)
    
    
    
    add_label(global_window, txt, 0, 0, 0, 0)
    add_label(global_window, "Veuillez relancer l'application, en corrigeant les erreurs.", 0, 1, 0, 0)

def launch_window():
    global global_window
    
    init_window_frame("Analyse CSV", "960x540")
    
    global_window.mainloop()

launch_window()
