# Configuración general de DealHunter USA


# Ubicación actual (Harrisburg, Pennsylvania)
ZIP_CODE = "17112"

# Radio aproximado de búsqueda en millas
SEARCH_RADIUS = 25


# Descuento mínimo para enviar alerta
# Ejemplo: 70 significa 70% de descuento
MIN_DISCOUNT = 70


# Categorías favoritas
CATEGORIES = [
    "ropa",
    "calzado",
    "electrodomesticos",
    "juguetes",
    "hogar",
    "electronica",
    "herramientas"
]

# Modo de búsqueda:
# "all" = todas las categorías
# "favorites" = solo categorías seleccionadas

SEARCH_MODE = "favorites"
# Tiendas activas
STORES = [
    "Amazon",
    "Walmart",
    "Target",
    "Best Buy",
    "Home Depot",
    "Lowe's",
    "Kohl's",
    "Macy's",
    "Sam's Club",
    "Costco"
]


# Cada cuántos minutos se ejecutará el radar
SCAN_INTERVAL_MINUTES = 10
