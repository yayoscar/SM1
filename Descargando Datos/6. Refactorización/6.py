import json


with open('') as f:
    all_eq_data = json.load(f)


magnitudes, longitudes, latitudes, titles = [], [], [], []


all_eq_dicts = all_eq_data['features']
for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict['properties']['mag'])
    longitudes.append(eq_dict['geometry']['coordinates'][0])
    latitudes.append(eq_dict['geometry']['coordinates'][1])
    titles.append(eq_dict['properties']['title'])
