def puntuar_deal(deal):
    """
    Calcula una puntuación de oportunidad de 0 a 100.
    """

    puntos = 0

    # Puntuación por porcentaje de descuento
    if deal.descuento >= 90:
        puntos += 50
    elif deal.descuento >= 75:
        puntos += 40
    elif deal.descuento >= 60:
        puntos += 30
    elif deal.descuento >= 50:
        puntos += 20


    # Puntuación por ahorro en dólares
    ahorro = deal.ahorro()

    if ahorro >= 100:
        puntos += 30
    elif ahorro >= 50:
        puntos += 20
    elif ahorro >= 20:
        puntos += 10


    # Bonus por categorías interesantes
    categorias_top = [
        "electrodomesticos",
        "electronica",
        "herramientas",
        "calzado"
    ]

    if deal.categoria.lower() in categorias_top:
        puntos += 10


    # Máximo 100 puntos
    return min(puntos, 100)



def nivel_deal(puntos):

    if puntos >= 90:
        return "🔥🔥🔥 LIQUIDACIÓN EXTREMA"

    elif puntos >= 75:
        return "🔥 DEAL EXCELENTE"

    elif puntos >= 60:
        return "⭐ MUY BUENA OFERTA"

    else:
        return "👍 Buena oportunidad"
