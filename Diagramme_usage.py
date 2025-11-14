import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\delafcl4\Documents\experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()


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
    

    #print(counts)
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
    plt.show()
    #print(x, y)
    
    plt.show()
    
usage()
