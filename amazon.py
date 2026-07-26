from filters import es_buen_deal
from notifier import enviar_deal
from history import ya_enviado, guardar_deal
from sources import obtener_ofertas_amazon


def buscar_ofertas_amazon():

    ofertas = obtener_ofertas_amazon()


    for oferta in ofertas:

        if es_buen_deal(oferta):

            if not ya_enviado(oferta.titulo):

                enviar_deal(oferta)

                guardar_deal(oferta)



def iniciar_amazon():

    buscar_ofertas_amazon()
