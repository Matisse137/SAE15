import folium
import webbrowser
import pandas as pd

#Créer une carte
carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Enregistrer dans un fichier HTML
fichier = "carte_interactive.html"
carte.save(fichier)
# Charger le fichier CSV
df = pd.read_csv(r"experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()

carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)


for i in range(len(df)):
    latitude, longitude, Bande_de_fréquences = df.loc[i, ["Latitude", "Longitude", "Bande de fréquences"]]
    latitude = float(latitude.replace(',', '.'))
    longitude = float(longitude.replace(',', '.'))
    experimentateur = df.loc[i, "Expérimentateur"]
    regions = df.loc[i, "Région"]
    bande = df.loc[i, "Bande de fréquences"]
    description = df.loc[i, "Description"]
    numero_arcep = df.loc[i, "Numéro de la décision d'autorisation de l'Arcep"]

    # Créer le texte du popup en HTML
    popup_text = f"""
    <b>Expérimentateur :</b> {experimentateur}<br>
    <b>Région :</b> {regions}<br>
    <b>Numéro ARCEP :</b> {numero_arcep}<br>
    <b>Bande de fréquences :</b> {bande}<br>
    <b>Description :</b> {description}
    """

    # Ajouter le marqueur
    folium.Marker(
        location=[latitude, longitude],
        tooltip="Cliquer pour plus d'infos",  
        popup=popup_text  # affiché au clic
    ).add_to(carte)
    


carte.save("carte_interactive.html")

webbrowser.open(fichier)

