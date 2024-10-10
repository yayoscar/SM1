import requests
import json
# Realizar una llamada a la API y almacenar la respuesta.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Código de estado: {r.status_code}")
# Explorar la estructura de los datos.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)