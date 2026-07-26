import os
import requests


TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def enviar_telegram(mensaje):
    """
    Envía un mensaje al usuario mediante Telegram.
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    datos = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }

    respuesta = requests.post(url, data=datos)

    return respuesta.json()


def enviar_deal(deal):
    """
    Formatea una oferta y la envía.
    """

    mensaje = (
        "🚨🔥 DEAL ENCONTRADO 🔥🚨\n\n"
        f"🏪 Tienda: {deal.tienda}\n"
        f"📦 Producto: {deal.titulo}\n\n"
        f"💰 Precio actual: ${deal.precio_actual}\n"
        f"🏷️ Precio anterior: ${deal.precio_anterior}\n\n"
        f"📉 Descuento: {deal.descuento}%\n"
        f"💵 Ahorro: ${deal.ahorro():.2f}\n\n"
        f"📂 Categoría: {deal.categoria}\n\n"
        f"🔗 Enlace:\n{deal.url}"
    )

    return enviar_telegram(mensaje)
