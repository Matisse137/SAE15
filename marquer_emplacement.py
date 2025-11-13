import pandas as pd


df = pd.read_csv(r"C:\Users\delafcl4\Documents\experimentations_5G.csv", encoding="Windows-1252", sep=";", engine="python")
df.head()

m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

for i in range(len(df)):
    latitude,longitude = df.+loc[i, ["Latitude", "Longitude"]]
    latitude = float(latitude.replace(',', '.'))
    longitude = float(longitude.replace(',', '.'))
    print(latitude,longitude)
    
    folium.Marker(
        location=[latitude, longitude],
        tooltip="Clique pour plus d'infos",
        ).add_to(m)

m.save("01_carte_base.html")
