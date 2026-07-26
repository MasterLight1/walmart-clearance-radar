from models import Deal
from filters import es_buen_deal
from notifier import enviar_deal


def buscar_ofertas_amazon():
    """
    Módulo inicial de Amazon.
    Más adelante conectaremos aquí la fuente real de datos.
    """

    ofertas = [

        Deal(
            tienda="Amazon",
            titulo="Ejemplo - Ninja Air Fryer",
            precio_actual=39.99,
            precio_anterior=129.99,
            descuento=75,
            url="https://www.amazon.com",
            categoria="electrodomesticos"
        )

    ]


    for oferta in ofertas:

        if es_buen_deal(oferta):
            enviar_deal(oferta)



def iniciar_amazon():
    buscar_ofertas_amazon()
