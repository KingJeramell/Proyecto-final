import http
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd





url= ("https://www.powergamesenlinea.com/")


# Hacer una solicitud Get a la URL
soli= requests.get(url)
#Verificar el estado de la solicitud
soup = BeautifulSoup(soli.text, 'html.parser')



# extraer el titulo de la pagina
titulo = soup.title.string
print("el titulo de la pagina es:", titulo)



# Buscar productos y precios 
productos = soup.find_all('a', class_='item-name')
precios = soup.find_all('div', class_='item-price')

print("\nPRODUCTOS y PRECIOS ENCONTRADOS CON SUS LINK:")

#para interactuar con los productos y precios
for producto, precio in zip(productos, precios):
    producto_texto = producto.text.strip()
    precio_texto = precio.text.strip()
    producto_url = producto.get('href') # Obtener el enlace del producto
    link = urljoin(url, producto_url)
    print(producto_texto)
    print(precio_texto)
    print(link)
    print( )
    
    fichaProducto = soup.find_all('div', class_="product=card__image")

    for element in fichaProducto:
        imagenProducto = element.find('img', class_='/_sh/18/1843m.webp').get('src')







    
