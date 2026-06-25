from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.producto import Product

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def find_all(self) -> List[Product]:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        pass

