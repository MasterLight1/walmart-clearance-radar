from config import MIN_DISCOUNT


def es_buen_deal(deal):
    """
    Decide si una oferta merece ser enviada.
    """

    # Regla 1:
    # Debe superar el descuento mínimo configurado
    if deal.descuento < MIN_DISCOUNT:
        return False


    # Regla 2:
    # Debe tener ahorro real
    if deal.ahorro() < 10:
        return False


    # Regla 3:
    # El precio final debe ser válido
    if deal.precio_actual <= 0:
        return False


    return True
