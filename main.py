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
line_list = [{}]

def add_line( experimenter, frenquency, low_frenquency, 
        high_frequency, autorisation_nb, autorisation_nb
        latitude, longitude, insee_code, 
        area, department, country,
        date_begin, date_end, description, 
        t_mimo, t_beam, t_time_multiplexing
        t_nsa, t_sa, t_synchro,
        t_slicing, t_small_cells, t_dynamic_spectrum,
        t_mobility, t_objets, t_smart_cities,
        t_virtual_reality, t_medical, t_industry,
        t_technic, t_other):
    return 0