"""
Fuentes externas de ofertas.

Aquí conectaremos:
- Amazon
- Walmart
- Target
- etc.
"""

from models import Deal
from amazon_provider import buscar_productos_amazon



def crear_deal_amazon(
    titulo,
    precio_actual,
    precio_anterior,
    descuento,
    url,
    categoria
):
    """
    Convierte información recibida
    de Amazon en un objeto Deal.
    """

    return Deal(
        tienda="Amazon",
        titulo=titulo,
        precio_actual=float(precio_actual),
        precio_anterior=float(precio_anterior),
        descuento=float(descuento),
        url=url,
        categoria=categoria
    )



def obtener_ofertas_amazon():

    productos = buscar_productos_amazon()

    ofertas = []


    for producto in productos:

        oferta = crear_deal_amazon(
            titulo=producto["titulo"],
            precio_actual=producto["precio_actual"],
            precio_anterior=producto["precio_anterior"],
            descuento=producto["descuento"],
            url=producto["url"],
            categoria=producto["categoria"]
        )

        ofertas.append(oferta)


    return ofertas
