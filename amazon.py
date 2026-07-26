from models import Deal
from filters import es_buen_deal
from notifier import enviar_deal
from history import ya_enviado, guardar_deal


def buscar_ofertas_amazon():

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

            if not ya_enviado(oferta.titulo):

                enviar_deal(oferta)

                guardar_deal(oferta)



def iniciar_amazon():

    buscar_ofertas_amazon()
