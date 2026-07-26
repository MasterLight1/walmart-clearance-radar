from config import MIN_DISCOUNT, SEARCH_MODE, CATEGORIES


def es_buen_deal(deal):
    """
    Decide si una oferta merece ser enviada.
    """

    # Regla 1:
    # Debe superar el descuento mínimo
    if deal.descuento < MIN_DISCOUNT:
        return False


    # Regla 2:
    # Debe tener ahorro real
    if deal.ahorro() < 10:
        return False


    # Regla 3:
    # Precio válido
    if deal.precio_actual <= 0:
        return False


    # Regla 4:
    # Filtrar categorías si está activado el modo favorito
    if SEARCH_MODE == "favorites":

        if deal.categoria.lower() not in [
            categoria.lower()
            for categoria in CATEGORIES
        ]:
            return False


    return True
