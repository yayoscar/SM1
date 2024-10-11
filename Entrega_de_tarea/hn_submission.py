import time
import requests
import plotly.express as px
from operator import itemgetter
import plotly.io as pio

pio.renderers.default = 'browser'

def obtener_con_reintentos(url, max_reintentos=3, espera=5, tiempo_limite=30):
    for intento in range(max_reintentos):
        try:
            respuesta = requests.get(url, timeout=tiempo_limite)
            respuesta.raise_for_status()
            return respuesta
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Reintentando ({intento + 1}/{max_reintentos}) en {espera} segundos...")
            time.sleep(espera)
    print(f"Error permanente al conectar con la URL: {url}")
    return None

url_historias = "https://hacker-news.firebaseio.com/v0/topstories.json"
respuesta_historias = obtener_con_reintentos(url_historias)

if not respuesta_historias:
    print("No se pudo obtener la lista de historias principales.")
    exit()

ids_publicaciones = respuesta_historias.json()
datos_publicaciones = []
for id_publicacion in ids_publicaciones[:10]:
    url_publicacion = f"https://hacker-news.firebaseio.com/v0/item/{id_publicacion}.json"
    r = obtener_con_reintentos(url_publicacion)

    if not r:
        print(f"Publicación omitida: {id_publicacion}")
        continue

    print(f"id: {id_publicacion}\tstatus: {r.status_code}")

    try:
        diccionario_respuesta = r.json()
        datos_publicacion = {
            'titulo': diccionario_respuesta['title'],
            'enlace_hn': f"https://news.ycombinator.com/item?id={id_publicacion}",
            'comentarios': diccionario_respuesta.get('descendants', 0),
        }
        datos_publicaciones.append(datos_publicacion)
    except KeyError:
        print(f"Error al procesar la publicación: {id_publicacion}")

datos_publicaciones = sorted(datos_publicaciones, key=itemgetter('comentarios'), reverse=True)

titulos = [f"<a href='{item['enlace_hn']}'>{item['titulo']}</a>" for item in datos_publicaciones]
num_comentarios = [item['comentarios'] for item in datos_publicaciones]

titulo_grafico = "Discusiones más activas en Hacker News"
etiquetas = {'x': 'Publicación', 'y': 'Número de comentarios'}
grafico = px.bar(x=titulos, y=num_comentarios, title=titulo_grafico, labels=etiquetas, hover_name=titulos)
grafico.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

grafico.show()
