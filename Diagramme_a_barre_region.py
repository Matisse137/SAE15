import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\delafcl4\Documents\experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()



def frequence_region():
    region_counts = df["Région"].value_counts()  
    
    plt.figure(figsize=(10,6))
    region_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Nombre d'expérimentations 5G par région")
    plt.xlabel("Région")
    plt.ylabel("Fréquence")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
frequence_region () 



