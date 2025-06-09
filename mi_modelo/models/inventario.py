"""
Módulo: inventario.py
Descripción: Clases para gestionar inventario de una tienda de zapatos.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ProductoZapato:
    """Representa un producto de zapato en el inventario."""
    id_producto: int
    nombre: str
    marca: str
    talla: float
    cantidad: int
    precio: float

    def __str__(self) -> str:
        return (
            f"ID: {self.id_producto} | "
            f"{self.marca} - {self.nombre} | "
            f"Talla: {self.talla} | "
            f"Cantidad: {self.cantidad} pares | "
            f"Precio: ${self.precio:.2f}"
        )


class Inventario:
    """Administra el inventario de zapatos."""

    def __init__(self):
        self._productos: List[ProductoZapato] = []
        self._proximo_id = 1

    def agregar_producto(self, nombre: str, marca: str, talla: float, cantidad: int, precio: float) -> ProductoZapato:
        """Agrega un nuevo producto al inventario."""
        producto = ProductoZapato(
            id_producto=self._proximo_id,
            nombre=nombre,
            marca=marca,
            talla=talla,
            cantidad=cantidad,
            precio=precio
        )
        self._productos.append(producto)
        self._proximo_id += 1
        return producto

    def listar_productos(self) -> List[ProductoZapato]:
        """Devuelve la lista de todos los productos en inventario."""
        return self._productos

    def encontrar_producto(self, id_producto: int) -> Optional[ProductoZapato]:
        """Busca un producto por su id."""
        for producto in self._productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def actualizar_cantidad(self, id_producto: int, cantidad: int) -> bool:
        """Actualiza la cantidad de un producto. Retorna True si fue exitoso."""
        producto = self.encontrar_producto(id_producto)
        if producto:
            producto.cantidad = cantidad
            return True
        return False

    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto del inventario por su id."""
        producto = self.encontrar_producto(id_producto)
        if producto:
            self._productos.remove(producto)
            return True
        return False
