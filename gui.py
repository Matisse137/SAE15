import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk  # pour insérer une image

def empty():
    return

global_file_name = ""

# Les fonctions qui suivent utilisent tkinter,
# elles servent à ajouter les éléments
def init_window(title, size):
    """
    Parameters
    ----------
    title : str
        texte affiché en tant que titre.
    size : str
        taille de la fenêtre au format nb1xnb2.

    Returns
    -------
    window : tk.Tk()
        renvoie l'objet fenêtre.
    """
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    return window


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
    window = init_window(title, size)
    frame = ttk.Frame(window)
    frame.grid()
    
    return window, frame


def add_label(window, txt, x, y, pad_x, pad_y):
    label = ttk.Label(window, text=txt)
    label.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    return label


def add_button(window, txt, func, x, y, pad_x, pad_y):
    button = ttk.Button(window, text=txt, command=func)
    button.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    return button


def add_entry(window, x, y, pad_x, pad_y):
    entry = ttk.Entry(window)
    entry.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    
    return entry


def add_img(window, file_name, anchor_, size_x, size_y, x, y, pad_x, pad_y):
    img = Image.open(file_name)
    img = img.resize((size_x, size_y))
    tk_image = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(window, width=size_x, height=size_y)
    canvas.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    canvas.create_image(0, 0, image=tk_image, anchor=anchor_)
    
    canvas.image = tk_image
    return canvas

# Les fonctions qui suivent seront les actions de chaques boutons
def btn_file(file_name):
    global_file_name = file_name

def btn_1():
    
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
    webbrowser.open_new_tab("carte_interactive.html")
    return

# fonctions de comportement de la fenêtre

def ask_file(frame):
    
    add_button(frame, "valider", lambda: btn_file(), x, y, pad_x, pad_y)

# Fonction de lancement de la fenêtre
def launch_window():
    window, frame = init_window_frame("Analyse CSV", "960x540")
    add_button(frame, "Expérimentations par départements", btn_1, 0, 0, 2, 2)
    add_button(frame, "Expérimentations par bandes de fréquences", btn_2, 0, 1, 2, 2)
    add_button(frame, "Technologie par départements", btn_3, 0, 2, 2, 2)
    add_button(frame, "Technologie par régions", btn_4, 0, 3, 2, 2)
    add_button(frame, "Usage par départements", btn_5, 1, 0, 2, 2)
    add_button(frame, "Usage par régions", btn_6, 1, 1, 2, 2)
    add_button(frame, "Présence de technologies par régions", btn_7, 1, 2, 2, 2)
    add_button(frame, "Ouvrir la carte interactive", btn_8, 1, 3, 2, 2)
    
    
    
    window.mainloop()

launch_window()
