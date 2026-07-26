from amazon import iniciar_amazon
from notifier import enviar_telegram


def iniciar_radar():

    enviar_telegram(
        "🦅 DealHunter USA iniciado.\n\n"
        "🔎 Buscando ofertas..."
    )

    iniciar_amazon()


if __name__ == "__main__":
    iniciar_radar()
