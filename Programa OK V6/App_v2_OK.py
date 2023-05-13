# Librerias
from functions import listado_todos_los_productos,limite_producto

producto = input("Indique por favor el producto a buscar ")
limite = input("indique por favor cuantas paginas desee mostrar ")

def mercadoLibre():

    if 'limite' != 0:
        titulos,urls,precios = listado_todos_los_productos(data["producto"])
    else:
        titulos,urls,precios = limite_producto(data["producto"],data["limite"])
    return jsonify({"datos": {"titulos": titulos, "urls": urls, "precios": precios}})
