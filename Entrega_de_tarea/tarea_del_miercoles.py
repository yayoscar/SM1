from operator import itemgetter
import requests

url_principales = "https://hacker-news.firebaseio.com/v0/topstories.json"
respuesta = requests.get(url_principales)
print(f"Código de estado: {respuesta.status_code}")

ids_publicaciones = respuesta.json()
datos_publicaciones = []

for id_publicacion in ids_publicaciones[:5]:
    url_publicacion = f"https://hacker-news.firebaseio.com/v0/item/{id_publicacion}.json"
    respuesta_pub = requests.get(url_publicacion)
    print(f"id: {id_publicacion}\tstatus: {respuesta_pub.status_code}")
    diccionario_respuesta = respuesta_pub.json()
    
    datos_publicacion = {
        'titulo': diccionario_respuesta['title'],
        'enlace_hn': f"https://news.ycombinator.com/item?id={id_publicacion}",
        'comentarios': diccionario_respuesta.get('descendants', 0),
    }
    datos_publicaciones.append(datos_publicacion)

datos_publicaciones = sorted(datos_publicaciones, key=itemgetter('comentarios'), reverse=True)

for datos_pub in datos_publicaciones:
    print(f"\nTítulo: {datos_pub['titulo']}")
    print(f"Enlace a la discusión: {datos_pub['enlace_hn']}")
    print(f"Comentarios: {datos_pub['comentarios']}")
