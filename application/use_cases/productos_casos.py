import string
from dataclasses import dataclass
from datetime import datetime
from typing import List

from application.dtos.response import Response
from domain.entities.producto import Product
from application.dtos.producto_dto import ProductDTO
from domain.repositories.product_repositories import ProductRepository

@dataclass
class ProductUseCase:
    product_repository: ProductRepository

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository


    def create_product(self, product: ProductDTO) -> Response[Product]:
        try:
            new_product = Product(
                nombre=product.nombre,
                descripcion=product.descripcion,
                precio=product.precio,
                cantidad=product.cantidad,
                fecha_actualizacion=datetime.now()
            )

            guardar_producto = self.product_repository.save(new_product)

            return Response[Product](success=True, status=200, data=guardar_producto)
        
        except ValueError as e:
            raise ValueError(f"Error al crear el producto: {str(e)}")

        return self.product_repository.create_product(new_product)

    def get_product_by_id(self, product_id: int) -> Response[Product]:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            return Response[Product](success=False, error="Producto no encontrado.", status=400)

        return Response[Product](success=True, data=product, status=200)

    def list_products(self) -> Response[List[Product]]:
        List[Product] = self.product_repository.find_all()
        return Response[List[Product]](success=True, data=List[Product], status=200)

    def delete_product(self, product_id: int) -> Response[str]:
        try:
            existing_product = self.product_repository.find_by_id(product_id)
            if not existing_product:
                raise ValueError(f"Producto con ID {product_id} no encontrado.")
            self.product_repository.delete_product(product_id)
            return Response[str](success=True, data="Producto eliminado con exito", status=200)
        except ValueError as e:
            return Response[str](success=False, error=str(e), status=400)
