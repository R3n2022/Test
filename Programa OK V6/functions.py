#Librerias
import requests
from bs4 import BeautifulSoup
from lxml import etree

# Xpath donde estan los precios
xprecios = '//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]/div[@class="ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left"]/div[1]/div[1]/div[1]//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="price-tag-amount"]/span[2]'

# Funcion para traer todos los productos
def listado_todos_los_productos(producto):
    lista_titulos = []
    lista_Urls = []
    lista_precios = []
    siguiente = 'https://listado.mercadolibre.com.ar/' +producto
    while True:
        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            # Titulos
            titulos = soup.find_all('h2', attrs={"class": "ui-search-item__title shops__item-title"})
            titulos = [i.text for i in titulos]
            lista_titulos.extend(titulos)
            # Url
            urls = soup.find_all('a', attrs={"class": "ui-search-item__group__element shops__items-group-details ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_Urls.extend(urls)
            # Precios
            dom = etree.HTML(str(soup))
            precios = dom.xpath(xprecios)
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            # Se Valida nuevamente el valor inicial
            inicial = soup.find('span', attrs={"class": "andes-pagination__link"}).text
            inicial = int(inicial)
            # Se Valida nuevamente la cantidad
            cantidad = soup.find('li', attrs={"class": "andes-pagination__page-count"}).text.split(" ")[1]
            cantidad = int(cantidad)
        else:
            print("Error de Respuesta en listas -> Revisar Bucle Listas de productos")
            break
        print(inicial, cantidad)
        if inicial == cantidad:
            print("Proceso de busqueda total finalizado con exito!")
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]/ul/li[@class="andes-pagination__button andes-pagination__button--next shops__pagination-button"]/a')[0].get('href')

    return lista_titulos,lista_Urls,lista_precios

# Funcion con Limite de productos

def limite_producto(producto,limite):
    lista_titulos = []
    lista_Urls = []
    lista_precios = []
    siguiente = 'https://listado.mercadolibre.com.ar/' + producto
    while True:
        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            # Titulos
            titulos = soup.find_all('h2', attrs={"class": "ui-search-item__title shops__item-title"})
            titulos = [i.text for i in titulos]
            lista_titulos.extend(titulos)
            # Url
            urls = soup.find_all('a', attrs={"class": "ui-search-item__group__element shops__items-group-details ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_Urls.extend(urls)
            # Precios
            dom = etree.HTML(str(soup))
            precios = dom.xpath(xprecios)
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            # Se Valida nuevamente el valor inicial
            inicial = soup.find('span', attrs={"class": "andes-pagination__link"}).text
            inicial = int(inicial)
            # Se Valida nuevamente la cantidad
            cantidad = soup.find('li', attrs={"class": "andes-pagination__page-count"}).text.split(" ")[1]
            cantidad = int(cantidad)
        else:
            print("Error de Respuesta en listas -> Revisar Bucle Listas de productos")
            break
        print(inicial, cantidad)
        if len(lista_titulos) >= int(limite):
            return lista_titulos[:int(limite)], lista_Urls[:int(limite)], lista_precios[:int(limite)]
        if inicial == cantidad:
            print("Proceso de busqueda parcial finalizado con exito!")
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]/ul/li[@class="andes-pagination__button andes-pagination__button--next shops__pagination-button"]/a')[0].get('href')

    return lista_titulos, lista_Urls, lista_precios

