from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Product:
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float = 0.0
    cantidad: int = 0
    fecha_creacion: datetime = datetime.now()
    fecha_actualizacion: datetime = datetime.now()

    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if self.nombre:
            raise ValueError("El nombre no puede estar vacío.")
        

