"""
Paquete de DAOs para la tienda de zapatos
"""

from .base_dao import BaseDAO
from .zapato_dao import ZapatoDAO
from .venta_dao import VentaDAO

__all__ = ['BaseDAO', 'ZapatoDAO', 'VentaDAO']

