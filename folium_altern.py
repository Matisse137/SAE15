import folium

# Carte centrée sur Paris avec un zoom de 12
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

folium.Marker(
    location=[48.8566, 2.3522],
    popup="Paris, capitale de la France",
    tooltip="Clique pour plus d'infos",
    
).add_to(m)

m.save("01_carte_base.html")