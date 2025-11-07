import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\delafcl4\Documents\experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()


def usage():
    
    counts =[]
    usages = [
            "Usage - Mobilité connectée",
            "Usage - Internet des objets",
            "Usage - Ville intelligente",
            "Usage - Réalité virtuelle",
            "Usage - Télémédecine",
            "Usage - Industrie du futur",
            "Usage - Autre"
            ]
    
    for col in usages:
        if col in df.columns:
            quantitede1 = df[col].value_counts().get(1)
            counts.append(int((quantitede1*100)/len(df)))
        else:
            pass
    

    print(counts)
    x = np.array(usages)
    y = np.array(counts)
    
    plt.figure(figsize=(10, 5))
    plt.bar(x,100, color="#ff8066", edgecolor="black")
    plt.bar(x,y, color="skyblue", edgecolor="black")
    plt.title("Nombre d'expérimentations par type d'usage")
    plt.xlabel("Nombre de test réaliser")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    print(x, y)
    
    plt.show()
    
usage()