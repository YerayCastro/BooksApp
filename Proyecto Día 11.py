import bs4
import requests


# Para crear una url sin pagina
url_base = "https://books.toscrape.com/catalogue/page-{}.html"


"""
# Para  poder sacar datos de varias urls
for n in range(1, 11):
    print(url_base.format(n))
"""


"""

resultado = requests.get(url_base.format("1"))
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

libros = sopa.select(".product_pod")

#Para acceder a libros, la etiqueta y al título
ejemplo = libros[0].select("a")[1]["title"]
print(ejemplo)
"""


# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar páginas
for pagina in range(1, 51):

    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    # iterar libros
    for libro in libros:

        # Chequear que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # guardar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver libros de 4 o 5 estrellas por consola
for t in titulos_rating_alto:
    print(t)