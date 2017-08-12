import folium
import pandas

def get_color(height):
    if height < 1000:
        return 'yellow'
    elif 1000 <= height < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38, -99], zoom_start=4)

fg_v = folium.FeatureGroup(name='Volcanoes')
fg_p = folium.FeatureGroup(name='Population')

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])



for lt, ln, elev, name in zip(lat, lon, elev, name):
    color = get_color(elev)
    fg_v.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup='{} - {} m'.format(name, elev), color=color, fill_color=color))

fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding="utf-8-sig"),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
if 10000000 <= x['properties']['POP2005'] <=20000000 else 'red'}
))

map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save('test.html')
