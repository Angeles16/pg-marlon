from dataclasses import dataclass

@dataclass
class ProductDTO:
    nombre: str
    descripcion: str
    precio: float
    cantidad: int