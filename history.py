import json
import os
from datetime import datetime


ARCHIVO = "deal_history.json"


def cargar_historial():

    if not os.path.exists(ARCHIVO):
        return {}

    with open(ARCHIVO, "r") as archivo:
        return json.load(archivo)



def ya_enviado(titulo):

    historial = cargar_historial()

    return titulo in historial



def guardar_deal(deal):

    historial = cargar_historial()

    historial[deal.titulo] = {
        "tienda": deal.tienda,
        "precio": deal.precio_actual,
        "fecha": str(datetime.now())
    }


    with open(ARCHIVO, "w") as archivo:
        json.dump(historial, archivo, indent=4)
