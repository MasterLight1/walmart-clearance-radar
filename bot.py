import os
import requests

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    requests.post(url, data=datos)

enviar_mensaje(
    "🚀 Walmart Clearance Radar iniciado correctamente."
)
