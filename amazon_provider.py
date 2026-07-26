"""
Proveedor de datos de Amazon.

Recibe datos de una fuente externa
y los prepara para DealHunter.
"""

from deal_source import obtener_ofertas


def buscar_productos_amazon():

    """
    Obtiene productos desde la fuente
    externa de ofertas.
    """

    productos = obtener_ofertas()

    return productos
