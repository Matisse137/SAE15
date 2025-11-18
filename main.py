import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk  # pour insérer une image
import folium
import pandas as pd
import os

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
        
    add_button(global_top_frame, "Expérimentations par départements", btn_1, 0, 0, 2, 2)
    add_button(global_top_frame, "Expérimentations par bandes de fréquences", btn_2, 0, 1, 2, 2)
    add_button(global_top_frame, "Technologie par départements", btn_3, 0, 2, 2, 2)
    add_button(global_top_frame, "Technologie par régions", btn_4, 0, 3, 2, 2)
    add_button(global_top_frame, "Usage par départements", btn_5, 1, 0, 2, 2)
    add_button(global_top_frame, "Usage par régions", btn_6, 1, 1, 2, 2)
    add_button(global_top_frame, "Présence de technologies par régions", btn_7, 1, 2, 2, 2)
    add_button(global_top_frame, "Ouvrir la carte interactive", btn_8, 1, 3, 2, 2)
        
    
def btn_1():
    # add_img(frame, file_name, anchor_, size_x, size_y, x, y, pad_x, pad_y)
    return

def btn_2():
    
    return 

def btn_3():
    
    return 

def btn_4():
    
    return 

def btn_5():
    
    return

def btn_6():
    
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
