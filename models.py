from dataclasses import dataclass


@dataclass
class Deal:
    tienda: str
    titulo: str
    precio_actual: float
    precio_anterior: float
    descuento: float
    url: str
    categoria: str
    ubicacion: str = ""

    def ahorro(self):
        return self.precio_anterior - self.precio_actual

    def resumen(self):
        return (
            f"🔥 {self.tienda}\n"
            f"📦 {self.titulo}\n"
            f"💰 Ahora: ${self.precio_actual}\n"
            f"🏷️ Antes: ${self.precio_anterior}\n"
            f"📉 Descuento: {self.descuento}%\n"
            f"💵 Ahorras: ${self.ahorro():.2f}\n"
            f"🔗 {self.url}"
        )
