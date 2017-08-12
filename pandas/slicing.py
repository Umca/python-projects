import os
import pandas
from geopy.geocoders import Nominatim

nom = Nominatim()
a = nom.geocode('Doroshenka Str 8, Zaporizhzhya, Ukraine')
print(a.latitude)

data = pandas.read_json('supermarkets.json')
data = data.set_index('ID')

data['Continent'] = data.shape[0] * ["North America"]
data.ix[2,'Continent'] = 'Big Earth'

data_t = data.T

data_t['my address'] = data_t.shape[0] * ["bla bla"]

data = data_t.T

data['Address'] = data['Address'] +', ' +data['City'] +', ' + data['State'] +', '+ data['Country']

data['Coords']=data['Address'].apply(nom.geocode)

data['Latitude'] = data['Coords'].apply(lambda x: x.latitude if x.getattr(latitude) else None)

print(data)
