## ¡Pruébalo tú mismo!

#### Ejercicio 1: Otros Lenguajes

Modifica la llamada a la API en `python_repos.py` para que genere un gráfico que muestre los proyectos más populares en otros lenguajes. Prueba lenguajes como JavaScript, Ruby, C, Java, Perl, Haskell y Go.

#### Ejercicio 2: Discusiones Activas

Usando los datos de `hn_submissions.py`, crea un gráfico de barras que muestre las discusiones más activas que están ocurriendo actualmente en Hacker News. La altura de cada barra debe corresponder al número de comentarios que tiene cada publicación. La etiqueta de cada barra debe incluir el título de la publicación y actuar como un enlace a la página de discusión de esa publicación. Si obtienes un `KeyError` al crear un gráfico, utiliza un bloque `try-except` para omitir las publicaciones promocionales.

#### Ejercicio 3: Pruebas para `python_repos.py`

En `python_repos.py`, imprimimos el valor de `status_code` para asegurarnos de que la llamada a la API fue exitosa. Escribe un programa llamado `test_python_repos.py` que use `pytest` para afirmar que el valor de `status_code` es 200. Piensa en algunas otras afirmaciones que puedas hacer, por ejemplo, que la cantidad de elementos devueltos es la esperada y que el número total de repositorios es mayor que una cierta cantidad.

#### Ejercicio 4: Exploración Adicional

Visita la documentación de Plotly y de la API de GitHub o de la API de Hacker News. Usa algo de la información que encuentres allí para personalizar el estilo de los gráficos que ya hemos hecho o para obtener información diferente y crear tus propias visualizaciones. Si tienes curiosidad por explorar otras APIs, echa un vistazo a las APIs mencionadas en el repositorio de GitHub en [https://github.com/public-apis](https://github.com/public-apis).

