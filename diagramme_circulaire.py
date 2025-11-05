import matplotlib.pyplot as plt

def digramme_circulaire(bande_freq, nombre_feq):
    
    plt.pie(nombre_feq, labels=bande_freq, autopct='%1.f%%', counterclock=False, startangle=105)
    plt.title("Répartition des expérimentations par bande de fréquence en GHz")
    plt.show()
    
digramme_circulaire([2.6, 3.8, 26], [33, 80, 3])
    



