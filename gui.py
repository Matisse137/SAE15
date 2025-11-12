import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # poue inserer une image

def init_window(title, size):
    """
    Parameters
    ----------
    title : str
        texte affiché en temps que titre.
    size : str
        taille de la fenetre de format nb1xnb2.

    Returns
    -------
    window : tl.Tk()
        renvoie l'objet fenetre.
    """
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    return window
    
def init_window_frame(title, size):
    """
    Parameters
    ----------
    title : str
        texte affiché en temps que titre.
    size : str
        taille de la fenetre de format nb1xnb2.

    Returns
    -------
    window : tl.Tk()
        renvoie l'objet fenetre.
    """
    window = init_window(title, size)
    frame = ttk.Frame()
    frame.grid()
    return window
    
def add_label(window, txt, x, y, pad_x, pad_y):
    """
    Parameters
    ----------
    window : tk.Tk()
        fenetre, objet principale du programme lié à tkinter.
    txt : str
        texte associé.
    x : TYPE
        position sur la grille en y.
    y : int
        position sur la grille en y.
    pad_x : int
        Padding en x.
    pad_y : int
        Padding en y.

    Returns
    -------
    entry : ttk.Entry
        objet entry de ttk, lié à la fenêtre.
    """
    label = ttk.Label(window, txt)
    label.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    return label

def add_button(window, txt, func, x, y, pad_x, pad_y):
    """
    Parameters
    ----------
    window : tk.Tk()
        fenetre, objet principale du programme lié à tkinter.
    txt : str
        texte associé.
    func : obj fonction
        fonction que doit exécuter le boutton une fois appuyé
    x : TYPE
        position sur la grille en y.
    y : int
        position sur la grille en y.
    pad_x : int
        Padding en x.
    pad_y : int
        Padding en y.

    Returns
    -------
    entry : ttk.Entry
        objet entry de ttk, lié à la fenêtre.
    """
    button = ttk.Button(window, txt, command=func)
    button.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    return button

def add_entry(window, txt, x, y, pad_x, pad_y):
    """
    Parameters
    ----------
    window : tk.Tk()
        fenetre, objet principale du programme lié à tkinter.
    txt : str
        texte associé.
    x : TYPE
        position sur la grille en y.
    y : int
        position sur la grille en y.
    pad_x : int
        Padding en x.
    pad_y : int
        Padding en y.

    Returns
    -------
    entry : ttk.Entry
        objet entry de ttk, lié à la fenêtre.
    """
    entry = ttk.Entry(window)
    entry.grid(row=x, column=y, padx=pad_x, pady=pad_y)
    return entry

def add_img(window, file_name, anchor_, size_x, size_y, x, y, pad_x, pad_y):
    img = Image.open(file_name)
    img = img.resize((size_x, size_y))
    tk_image = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(window, width=size_x, height=size_y)
    canvas.grid(column=y, row=x, padx=pad_x, pady=pad_y)
    canvas.create_image(0, 0, image=tk_image, anchor=anchor_)

window = init_window_frame("A title", "960x540")

window.mainloop()