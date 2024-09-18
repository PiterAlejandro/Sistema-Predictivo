import folium
import requests
from folium.plugins import Fullscreen, LocateControl, Geocoder, Search

def basemap(request):
    API_KEY = 'AIzaSyBGh9aqZNtbOGcWNkBOeGaqnvr29TpTIyE'
    location = [-11.008973, -66.083399]
    radius = 5000 

    map = folium.Map(
        location=location,
        zoom_start=15, 
        tiles='cartodbdark_matter'
    )

    place_types = ['hospital', 'Escuela', 'tiendas', 'Supermercado', 'beneficiadoras, plazas, mercados, canchas ']
    for place_type in place_types:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location[0]},{location[1]}&radius={radius}&type={place_type}&key={API_KEY}"
        response = requests.get(url)
        results = response.json().get('results', [])
        for place in results:
            lat = place['geometry']['location']['lat']
            lng = place['geometry']['location']['lng']
            name = place['name']
            address = place.get('vicinity', 'Dirección no disponible')

            folium.Marker(
                location=[lat, lng],
                tooltip=f"{name} ({place_type.capitalize()})",
                popup=f"{name}<br>{address}<br>Tipo: {place_type.capitalize()}",
                icon=folium.Icon(color="blue" if place_type == "hospital" else "green")
            ).add_to(map)

    folium.TileLayer('cartodbpositron').add_to(map)
    folium.LayerControl(position='bottomright').add_to(map)
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)
    map = map._repr_html_()

    description = ("El Mapa Catastral brinda información general sobre la cartografía, normativa, guías, herramientas "
                   "y otros relacionados al registro catastral en el municipio de Riberalta en la provincia Vaca Diez. "
                   "El mapa catastral también permite interactuar con otras capas o mapas del Sistema de Información "
                   "Territorial (SIT) del GAMLP como ser el mapa de Uso de Suelos (LUSU), mapa de Riesgos y otros.")


    context = {
        'map': map,
        'description': description
    }

    return context
