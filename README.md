# Submódulo 1 - Identifica un conjunto de datos de casos de uso

## Visualizando Datos

**1. Cubos:** Un número elevado a la tercera potencia es un cubo. Grafica los primeros cinco números cúbicos y luego grafica los primeros 5000 números cúbicos.

**2. Cubos Coloreados:** Aplica un mapa de colores a tu gráfico de cubos.

**3. Movimiento Molecular:** Modifica `rw_visual.py` reemplazando `plt.scatter()` con `plt.plot()`. Para simular el camino de un grano de polen en la superficie de una gota de agua, pasa los valores `rw.valores_x` y `rw.valores_y`, e incluye un argumento `linewidth`. Usa 5,000 en lugar de 50,000 puntos.

**4. Caminatas Aleatorias Modificadas:** En la clase `RandomWalk`, `paso_x` y `paso_y` se generan a partir del mismo conjunto de condiciones. La dirección se elige aleatoriamente de la lista `[1, -1]` y la distancia de la lista `[0, 1, 2, 3, 4]`. Modifica los valores en estas listas para ver qué sucede con la forma general de tus caminatas. Prueba con una lista más larga de opciones para la distancia, como de 0 a 8, o elimina el `-1` de la lista de direcciones `x` o `y`.

**5. Refactorización:** El método `llenar_caminata()` es extenso. Crea un nuevo método llamado `obtener_paso()` para determinar la dirección y la distancia de cada paso, y luego calcular el paso. Deberías terminar con dos llamadas a `obtener_paso()` en `llenar_caminata()`:

```python
paso_x = self.obtener_paso()
paso_y = self.obtener_paso()
```

Esta refactorización debería reducir el tamaño de `llenar_caminata()` y hacer que el método sea más fácil de leer y entender.

**6. Dos D8:** Crea una simulación que muestre lo que sucede cuando lanzas dos dados de ocho caras 1000 veces. Intenta imaginar cómo crees que se verá la visualización antes de ejecutar la simulación; luego verifica si tu intuición era correcta. Aumenta gradualmente el número de lanzamientos hasta que comiences a ver los límites de las capacidades de tu sistema.

**7. Tres Dados:** Cuando lanzas tres dados D6, el número más pequeño que puedes obtener es 3 y el número más grande es 18. Crea una visualización que muestre lo que sucede cuando lanzas tres dados D6.

**8. Multiplicación:** Cuando lanzas dos dados, generalmente sumas los dos números para obtener el resultado. Crea una visualización que muestre lo que sucede si multiplicas estos números en su lugar.

**9. Comprensiones de Dados:** Para mayor claridad, los listados en esta sección utilizan la forma larga de los bucles `for`. Si te sientes cómodo utilizando comprensiones de listas, intenta escribir una comprensión para uno o ambos bucles en cada uno de estos programas.

**10. Practicando con Ambas Bibliotecas:** Intenta utilizar Matplotlib para crear una visualización de lanzamiento de dados y utiliza Plotly para hacer la visualización de una caminata aleatoria. (Necesitarás consultar la documentación de cada biblioteca para completar este ejercicio).

## Descargando datos

**1. Precipitaciones en Sitka**: Sitka está en un bosque lluvioso templado, por lo que recibe una cantidad considerable de lluvia. En el archivo de datos `sitka_weather_2021_simple.csv` hay un encabezado llamado `PRCP`, que representa las cantidades diarias de lluvia. Haz una visualización enfocada en los datos de esta columna. Puedes repetir el ejercicio para Death Valley si te interesa ver cuánta poca lluvia cae en un desierto.

**2. Comparación Sitka–Death Valley**: Las escalas de temperatura en los gráficos de Sitka y Death Valley reflejan los diferentes rangos de datos. Para comparar con precisión el rango de temperaturas en Sitka y Death Valley, necesitas escalas idénticas en el eje y. Cambia la configuración del eje y en uno o ambos gráficos de las **5** y **6**. Luego haz una comparación directa entre los rangos de temperatura en Sitka y Death Valley (o cualquier otro par de lugares que quieras comparar).

**3. San Francisco**: ¿Las temperaturas en San Francisco son más parecidas a las de Sitka o a las de Death Valley? Descarga algunos datos para San Francisco y genera un gráfico de temperaturas máximas y mínimas para comparar.

**4. Índices Automáticos**: En esta sección, escribimos de manera fija los índices correspondientes a las columnas `TMIN` y `TMAX`. Usa la fila de encabezado para determinar los índices de estos valores, de modo que tu programa pueda funcionar tanto para Sitka como para Death Valley. Usa el nombre de la estación para generar automáticamente un título apropiado para tu gráfico.

**5. Explora**: Genera algunas visualizaciones adicionales que examinen otros aspectos meteorológicos que te interesen, en cualquier ubicación que tengas curiosidad por explorar.

**6. Refactorización:** El bucle que extrae datos de `all_eq_dicts` utiliza variables para la magnitud, longitud, latitud y el título de cada terremoto antes de agregar estos valores a sus listas correspondientes. Este enfoque fue elegido para mayor claridad sobre cómo extraer datos de un archivo GeoJSON, pero no es necesario en tu código. En lugar de usar estas variables temporales, extrae cada valor de `eq_dict` y agrégalo a la lista correspondiente en una sola línea. Hacer esto debería reducir el cuerpo de este bucle a solo cuatro líneas.

**7. Título Automatizado:** En esta sección, usamos el título genérico *Terremotos Globales*. En su lugar, puedes usar el título del conjunto de datos en la parte de metadatos del archivo GeoJSON. Extrae este valor y asígnalo a la variable `title`.

**8. Terremotos Recientes:** Puedes encontrar archivos de datos en línea que contienen información sobre los terremotos más recientes en periodos de 1 hora, 1 día, 7 días y 30 días. Ve a [https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) y verás una lista de enlaces a conjuntos de datos para varios periodos de tiempo, enfocados en terremotos de diferentes magnitudes. Descarga uno de estos conjuntos de datos y crea una visualización de la actividad sísmica más reciente.

**9. Incendios Mundiales:** En los recursos para este capítulo, encontrarás un archivo llamado `world_fires_1_day.csv`. Este archivo contiene información sobre incendios que arden en diferentes ubicaciones alrededor del mundo, incluyendo la latitud, longitud y el brillo de cada incendio. Usando el procesamiento de datos de la primera parte de este capítulo y el trabajo de mapeo de esta sección, crea un mapa que muestre qué partes del mundo están afectadas por incendios.

Puedes descargar versiones más recientes de estos datos en [https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data). Puedes encontrar enlaces a los datos en formato CSV en la sección *SHP, KML, and TXT Files*.