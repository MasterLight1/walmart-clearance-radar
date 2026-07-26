
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
    Convierte información de Amazon
    en un objeto Deal.
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

    """
    Aquí llegará la conexión real.

    Por ahora simulamos la estructura
    que esperamos recibir.
    """

    datos = [
        {
            "titulo": "Ninja Air Fryer",
            "precio_actual": 39.99,
            "precio_anterior": 129.99,
            "descuento": 70,
            "url": "https://www.amazon.com",
            "categoria": "electrodomesticos"
        }
    ]


    ofertas = []

    for producto in datos:

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
