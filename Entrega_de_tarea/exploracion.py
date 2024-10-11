import time
import requests
import plotly.express as px
from operator import itemgetter
import plotly.io as pio

pio.renderers.default = 'browser'

def realizar_solicitud_con_reintentos(url, intentos=3, espera=5, tiempo_espera=30):
    for i in range(intentos):
        try:
            respuesta = requests.get(url, timeout=tiempo_espera)
            respuesta.raise_for_status()
            return respuesta
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Reintentando ({i + 1}/{intentos}) en {espera} segundos...")
            time.sleep(espera)
    print(f"Error persistente al conectar con la URL: {url}")
    return None

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
respuesta_principal = realizar_solicitud_con_reintentos(url)

if not respuesta_principal:
    print("No se pudo obtener la lista de historias principales.")
    exit()

identificadores = respuesta_principal.json()
articulos = []
for id_articulo in identificadores[:10]:
    url_articulo = f"https://hacker-news.firebaseio.com/v0/item/{id_articulo}.json"
    r = realizar_solicitud_con_reintentos(url_articulo)

    if not r:
        print(f"Artículo omitido: {id_articulo}")
        continue

    print(f"id: {id_articulo}\tstatus: {r.status_code}")

    try:
        datos_articulo = r.json()
        articulo = {
            'titulo': datos_articulo['title'],
            'enlace_hn': f"https://news.ycombinator.com/item?id={id_articulo}",
            'comentarios': datos_articulo.get('descendants', 0),
        }
        articulos.append(articulo)
    except KeyError:
        print(f"Error al procesar el artículo: {id_articulo}")

articulos = sorted(articulos, key=itemgetter('comentarios'), reverse=True)

titulos = [f"<a href='{item['enlace_hn']}'>{item['titulo']}</a>" for item in articulos]
num_comentarios = [item['comentarios'] for item in articulos]

titulo_grafico = "Discusiones más activas en Hacker News"
etiquetas = {'x': 'Publicación', 'y': 'Número de comentarios'}
grafico = px.bar(x=titulos, y=num_comentarios, title=titulo_grafico, labels=etiquetas, hover_name=titulos)

grafico.update_traces(marker_color='royalblue', marker_line_color='black', marker_line_width=1.5)
grafico.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickangle=-45,
    yaxis=dict(
        title=dict(font=dict(size=18)),
        tickfont=dict(size=16)
    ),
    template='plotly_white'
)

grafico.show()
