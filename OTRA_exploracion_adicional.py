import requests
import plotly.express as px
import pandas as pd

response = requests.get('https://restcountries.com/v3.1/all')
countries_data = response.json()

countries = []
for country in countries_data:
    countries.append({
        'name': country.get('name', {}).get('common', 'N/A'),
        'population': country.get('population', 0),
        'area': country.get('area', 0),
    })


df = pd.DataFrame(countries)

top_countries = df.nlargest(10, 'population')


fig = px.bar(top_countries, 
             x='name', 
             y='population', 
             title='Top 10 Países Más Poblados',
             text='population')


fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')
fig.update_layout(
    title='Población de los 10 Países Más Poblados',
    xaxis_title='País',
    yaxis_title='Población',
)

fig.show()
