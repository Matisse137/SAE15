import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk  # pour insérer une image
import folium
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

df = None

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
    departement_counts = fichier_csv['Département'].value_counts()
    departement_counts.plot.barh()

    plt.ylabel("Département")
    plt.xlabel("Nombre d'expérimentations")
    plt.title("Répartition des expérimentations par département")
    plt.savefig("diagramme_dep.png")
    plt.close()
    
def diagramme_circulaire():
    fichier_csv = df

    bande_counts = fichier_csv['Bande de fréquences'].value_counts()

    plt.figure(figsize=(7,7))
    plt.pie(
        bande_counts.values,
        labels=bande_counts.index,
        autopct='%1.1f%%',
        startangle=105,
        counterclock=False
    )
    plt.title("Répartition des expérimentations par bande de fréquence (GHz)")
    plt.savefig("diagramme_circulaire.png")
    plt.close()
    
def diagramme_techno_par_dep():

    fichier_csv = df

    dep_col = []
    techno_cols = []
    
    for col in fichier_csv.columns:
        if "Département" == col:
            dep_col = col
        elif "Techno" in col:
            techno_cols.append(col)

    data = fichier_csv[[dep_col] + techno_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    techno_par_dep = data.groupby(dep_col)[techno_cols].sum()

    techno_par_dep.plot(kind="bar", stacked=True, figsize=(14, 6))

    plt.title("Technologies 5G utilisées par département")
    plt.ylabel("Nombre d'expérimentations")
    plt.xlabel("Département")
    
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Technologies", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("diagramme_techno_par_dep.png")
    plt.close()
    
def diagramme_techno_region():
   
    fichier_csv = df

    techno_cols = []
    region_col = []
    
    for col in fichier_csv.columns:
        if "Région" in col:
            region_col = col
        if "Techno" in col:
            techno_cols.append(col)
       
    data = fichier_csv[techno_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    nb_1 = data.sum()
    nb_0 = len(data) - nb_1

    plt.figure(figsize=(10, 5))
    plt.bar(techno_cols, nb_1, label="1 (Présence)", color="skyblue")
    plt.bar(techno_cols, nb_0, bottom=nb_1, label="0 (Absence)", color="lightcoral")

    plt.title("Réparation des technologies 5G par type de Techno (région)")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("diagramme_techno_par_region.png")
    plt.close()

    
def diagramme_usage_par_dep():

    fichier_csv = df
    
    dep_col = []
    usage_cols = []
    
    for col in fichier_csv.columns:
        if "Département" == col:
            dep_col = col
        elif "Usage" in col:
            usage_cols.append(col)

    data = fichier_csv[[dep_col] + usage_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    usage_par_dep = data.groupby(dep_col)[usage_cols].sum()

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

    fichier_csv = df
    
    reg_col = []
    usage_cols = []
    
    for col in fichier_csv.columns:
        if "Région" == col:
            reg_col = col
        elif "Usage" in col:
            usage_cols.append(col)


    data = fichier_csv[[reg_col] + usage_cols].replace({"Oui": 1, "Non": 0}).fillna(0)

    usage_par_reg = data.groupby(reg_col)[usage_cols].sum()

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
    plt.savefig("nombre_temporelle_experimentations.png") 
    plt.close()

    
def tracer_evolution(df):
    df["Début"] = pd.to_datetime(df["Début"], errors="coerce", dayfirst=True)
    df = df.dropna(subset=["Début"])
    evolution = df["Début"].dt.to_period("M").value_counts().sort_index()

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
    return evolution
    

def launch_pyplot():
    frequence_region() 
    usage()
    diagramme_techno()
    departement()
    diagramme_circulaire()
    diagramme_techno_par_dep()
    diagramme_techno_region()
    diagramme_usage_par_dep()
    diagramme_usage_par_reg()
    diagramme_techno_region()
    compteur = graphique_experimentations_par_acteur(df)
    acteurs, valeurs = croissant(compteur)
    graphe(acteurs, valeurs)
    tracer_evolution(df)
    plt.close('all')


def launch_folium(file_name):
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    carte.save("carte_interactive.html")
        
    carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    
    for i in range(len(df)):
        latitude, longitude, Bande_de_fréquences = df.loc[i, ["Latitude", "Longitude", "Bande de fréquences"]]
        latitude = float(latitude.replace(',', '.'))
        longitude = float(longitude.replace(',', '.'))
        regions = df.loc[i, "Région"]
        bande = df.loc[i, "Bande de fréquences"]
        description = df.loc[i, "Description"]
        numero_arcep = df.loc[i, "Numéro de la décision d'autorisation de l'Arcep"]
    
        popup_text = f"""
        <b>Région :</b> {regions}<br>
        <b>Numéro ARCEP :</b> {numero_arcep}<br>
        <b>Bande de fréquences :</b> {bande}<br>
        <b>Description :</b> {description}
        """
    
        folium.Marker(
            location=[latitude, longitude],
            tooltip="Cliquer pour plus d'infos",
            popup=popup_text
        ).add_to(carte)
    
    carte.save("carte_interactive.html")

def exist():
    file_list = [
    "diagramme_a_barre_region.png",
    "diagramme_dep.png",
    "diagramme_circulaire.png",
    "diagramme_techno.png",
    "diagramme_techno_par_dep.png",
    "diagramme_techno_par_region.png",
    "techno_region.png",
    "diagramme_usage.png",
    "diagramme_usage_par_departement.png",
    "diagramme_usage_par_region.png",
    "evolution_temporelle_experimentations.png",
    "nombre_temporelle_experimentations.png",
    "carte_interactive.html"
    ]

    for elt in file_list:
        if not os.path.isfile(elt):
            return False
    return True

global_window = None
global_top_frame = None
global_bottom_frame = None
global_file_entry = None

def init_window_frame(title, size):

    global global_window
    global global_top_frame
    global global_bottom_frame
    global global_file_entry
    
    window = tk.Tk() 
    window.title(title) 
    window.geometry(size)

    style = ttk.Style(window)
    style.configure("TButton", background="#d9d9d9")
    style.map("TButton", background=[("active", "#c0c0c0")])
    
    top_frame = ttk.Frame(window)
    top_frame.grid(row=0)

    bottom_frame = tk.Frame(window, bg="#3a3a3a")
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
    global global_window
    
    flush(global_bottom_frame)
    
    frame = tk.Frame(global_bottom_frame, bg="#3a3a3a")
    frame.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    img = Image.open(file_name)

    max_w, max_h = 900, 480
    img.thumbnail((max_w, max_h))

    tk_image = ImageTk.PhotoImage(img, master=global_window)

    canvas = tk.Canvas(frame, width=img.width, height=img.height,
                       bg="#3a3a3a", highlightthickness=0)
    canvas.pack()
    canvas.create_image(0, 0, image=tk_image, anchor=anchor_)
    
    canvas.image = tk_image
    return canvas

def btn_file():
    global global_top_frame
    global global_file_entry
    global df
    
    add_label(global_top_frame, "Veuillez patienter", 1, 2, 2, 2)
    global_window.update_idletasks()
    
    file_name = global_file_entry.get()
    
    df = pd.read_csv(rf"{file_name}", encoding="Windows-1252", sep=";", engine="python")
    df.head()
    
    if not os.path.isfile(file_name) or not file_name.lower().endswith(".csv"):
        error_case("Le fichier n'existe pas ou n'est pas un CSV valide.")
        return
    
    try:
        pd.read_csv(file_name, sep=";", encoding="Windows-1252", engine="python")
    except Exception as e:
        error_case(f"Erreur lors de la lecture du CSV : {str(e)}")
        return
    
    if not exist():
        launch_pyplot()
        launch_folium(df)
    flush(global_top_frame)
    
    add_button(global_top_frame, "Régions", btn_region, 0, 0, 2, 2)
    add_button(global_top_frame, "Départements", btn_dep, 0, 1, 2, 2)
    add_button(global_top_frame, "Bandes de fréquences", btn_bandes, 0, 2, 2, 2)
    add_button(global_top_frame, "Techno (global)", btn_techno_global, 0, 3, 2, 2)
    
    add_button(global_top_frame, "Techno par départements", btn_techno_dep, 1, 0, 2, 2)
    add_button(global_top_frame, "Techno par régions", btn_techno_reg, 1, 1, 2, 2)
    add_button(global_top_frame, "Usage (global)", btn_usage_global, 1, 2, 2, 2)
    add_button(global_top_frame, "Usage par départements", btn_usage_dep, 1, 3, 2, 2)
    
    add_button(global_top_frame, "Usage par régions", btn_usage_reg, 2, 0, 2, 2)
    add_button(global_top_frame, "Techno régions (simplifiée)", btn_techno_region_simple, 2, 1, 2, 2)
    add_button(global_top_frame, "Évolution temporelle", btn_evolution, 2, 2, 2, 2)
    add_button(global_top_frame, "Expérimentations par acteur", btn_acteurs, 2, 3, 2, 2)
    
    add_button(global_top_frame, "Carte interactive", btn_map, 3, 0, 2, 2)


def btn_region():
    add_img("diagramme_a_barre_region.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_dep():
    add_img("diagramme_dep.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_bandes():
    add_img("diagramme_circulaire.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_techno_global():
    add_img("diagramme_techno.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_techno_dep():
    add_img("diagramme_techno_par_dep.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_techno_reg():
    add_img("diagramme_techno_par_region.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_usage_global():
    add_img("diagramme_usage.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_usage_dep():
    add_img("diagramme_usage_par_departement.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_usage_reg():
    add_img("diagramme_usage_par_region.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_techno_region_simple():
    add_img("techno_region.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_evolution():
    add_img("evolution_temporelle_experimentations.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_acteurs():
    add_img("nombre_temporelle_experimentations.png", "nw", 800, 600, 0, 0, 0, 0)

def btn_map():
    webbrowser.open("carte_interactive.html")

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
    
    init_window_frame("Analyse CSV", "1024x600")
    
    global_window.mainloop()

launch_window()