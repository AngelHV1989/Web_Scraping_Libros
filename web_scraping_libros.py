"""
Este es un modulo basado en web scraping en el cual obtendremos en nuestra consola el titulo de los libros de la
web 'https://books.toscrape.com/index.html' que contengan una valoración de 4 o más estrellas
"""

import bs4
import requests

# crear url sin numero de página
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o más estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # comprobar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)