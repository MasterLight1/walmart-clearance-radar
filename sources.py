"""
Fuentes externas de ofertas.

Aquí conectaremos:
- Amazon
- Walmart
- Target
- etc.
"""

from models import Deal


def crear_deal_amazon(
    titulo,
    precio_actual,
    precio_anterior,
    descuento,
    url,
    categoria
):
    """
    Convierte datos de Amazon en un objeto Deal.
    """

    return Deal(
        tienda="Amazon",
        titulo=titulo,
        precio_actual=precio_actual,
        precio_anterior=precio_anterior,
        descuento=descuento,
        url=url,
        categoria=categoria
    )



def obtener_ofertas_amazon():

    # Aquí llegará la conexión real posteriormente.
    # Por ahora devuelve una lista vacía.
    return []
