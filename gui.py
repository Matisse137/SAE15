import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # pour insérer une image

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

    # garder une référence sinon l'image disparaît
    canvas.image = tk_image
    return canvas


def launch_window():
    window, frame = init_window_frame("Analyse CSV", "960x540")
    add_label(frame, "Texte de test", 0, 0, 2, 2)
    add_button(frame, "Quitter", window.destroy, 1, 0, 2, 2)
    window.mainloop()

launch_window()
