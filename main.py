#Inclusion des modules
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
# import folium as fl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#Variable global
line_list = [{}] # Cette ligne repertorie toutes les lignes du csv sous forme de dictionnaire
format_list = [        # Cette liste repertorie les differentes cles d'une ligne pour les dictionnaire au dessus
    "experimentateur",
    "bande_frequence",
    "frequence_basses",
    "frequence_haute",
    "nombre_autorisation",
    "lien_autorisation",
    "latitude",
    "longitude",
    "code_insee",
    "commune",
    "departement",
    "region",
    "debut",
    "fin",
    "descritpion",
    "techno_mimo",
    "techno_beamforming",
    "techno_duplexage",
    "techno_nsa",
    "techno_sa",
    "techno_synchro",
    "techno_slicing",
    "techno_small_cell",
    "techno_acces_dynamique",
    "techno_mobilite",
    "techno_iot",
    "techno_ville_intelligente",
    "techno_realite_virtuelle",
    "techno_telemedecine",
    "techno_industrie",
    "techno_rercherche_developpement",
    "techno_autre",
    ]

def build_line( experimenter, frenquency, low_frenquency, 
        high_frequency, autorisation_nb, autorisation_link,
        latitude, longitude, insee_code, 
        area, department, country,
        date_begin, date_end, description, 
        t_mimo, t_beam, t_time_multiplexing,
        t_nsa, t_sa, t_synchro,
        t_slicing, t_small_cells, t_dynamic_spectrum,
        t_mobility, t_objets, t_smart_cities,
        t_virtual_reality, t_medical, t_industry,
        t_technic, t_other):
    
    """
        Cette fonction sert à créer une list qui sera rentrée en argument
        de la fonction "add_line".
        
        Les parametres de cette fonctions sont les differents champs du csv du fichier "Exp5G-Formats.pdf"
        
    """
    return ( experimenter, frenquency, low_frenquency, 
            high_frequency, autorisation_nb, autorisation_link,
            latitude, longitude, insee_code, 
            area, department, country,
            date_begin, date_end, description, 
            t_mimo, t_beam, t_time_multiplexing,
            t_nsa, t_sa, t_synchro,
            t_slicing, t_small_cells, t_dynamic_spectrum,
            t_mobility, t_objets, t_smart_cities,
            t_virtual_reality, t_medical, t_industry,
            t_technic, t_other)

def add_line(line):
    """
    Parameters
    ----------
    line : list ou tuple
        line est la list qui sert à etre enregsitree dans la liste des enregistrements
        
    Cette fonction ajoute un enregistrement à la liste des lignes du fichier csv

    """
    res = {}
    
    for i, format_elt in enumerate(format_list):
        res[format_elt] = line[i]
        
    line_list.append(res)
    
def search_by(name, value):
    """
    Parameters
    ----------
    name : str
        nom du champs recherche
    value : str
        nom recherche dans les enregistrements
        
    Cette fonction recherche les enregistrements qui contiennent un element en particulier

    Returns
    -------
    res : list
        liste des indices des enregistrements qui contiennent le champs demande

    """
    res = []
    for i, elt in enumerate(line_list):
        if(elt[name] == value):
            res.append(i)
    return res

def occurrence(name, value):
    """
    Parameters
    ----------
    name : str
        nom du champs recherche
    value : str
        nom recherche dans les enregistrements
        
    Cherche le nombre de fois qu'une valeur est trouvée dans unn certain champs

    Returns
    -------
    occur : int
        nombre d'occurences

    """
    occur = 0
    for elt in line_list:
        if(elt[name] == value):
            occur += 1
    return occur
