import pandas as pd


fichier_csv = pd.read_csv(r"C:\Users\delafcl4\Documents\experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
fichier_csv.head()


def frequence():
    for i in fichier_csv():
        frequence = fichier_csv.iloc[2,1]

frequence()