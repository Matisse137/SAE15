import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\delafcl4\Documents\experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()

Techno_NSA = df["Techno - Mode de fonctionnement NSA (Non Stand Alone)"].value_counts()  

