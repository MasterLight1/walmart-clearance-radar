"""
Proveedor de datos de Amazon.

Aquí irá la conexión con la fuente real.
"""

from amazon_queries import QUERIES


def buscar_productos_amazon():

    """
    Busca productos usando las consultas configuradas.

    Formato esperado de salida:

    [
        {
            "titulo": "",
            "precio_actual": 0,
            "precio_anterior": 0,
            "descuento": 0,
            "url": "",
            "categoria": ""
        }
    ]
    """

    productos = []


    for query in QUERIES:

        # Aquí irá la conexión real.
        # Por ahora solo mostramos las búsquedas preparadas.
        print(f"Buscando en Amazon: {query}")


    return productos
