"""
VentaDAO - Manejo de datos de ventas
"""

from .base_dao import BaseDAO
from models.venta import Venta

class VentaDAO(BaseDAO):
    def __init__(self):
        super().__init__("ventas.txt")
    
    def guardar_venta(self, venta):
        """
        Guarda una venta en el archivo
        
        Args:
            venta (Venta): Objeto venta a guardar
            
        Returns:
            bool: True si se guardó correctamente, False en caso contrario
        """
        return self._agregar_linea(venta.to_string())
    
    def obtener_todas(self):
        """
        Obtiene todas las ventas del archivo
        
        Returns:
            list: Lista de objetos Venta
        """
        lineas = self._leer_archivo()
        ventas = []
        
        for linea in lineas:
            venta = Venta.from_string(linea)
            if venta:
                ventas.append(venta)
        
        return ventas
    
    def obtener_ventas_por_zapato(self, codigo_zapato):
        """
        Obtiene todas las ventas de un zapato específico
        
        Args:
            codigo_zapato (str): Código del zapato
            
        Returns:
            list: Lista de ventas del zapato
        """
        ventas = self.obtener_todas()
        ventas_zapato = []
        
        for venta in ventas:
            if venta.codigo_zapato == codigo_zapato:
                ventas_zapato.append(venta)
        
        return ventas_zapato
    
    def calcular_total_ventas(self):
        """
        Calcula el total de todas las ventas
        
        Returns:
            float: Total de ventas
        """
        ventas = self.obtener_todas()
        total = 0.0
        
        for venta in ventas:
            total += venta.total
        
        return total
    
    def obtener_estadisticas_por_zapato(self):
        """
        Obtiene estadísticas de ventas agrupadas por zapato
        
        Returns:
            dict: Diccionario con estadísticas por zapato
        """
        ventas = self.obtener_todas()
        estadisticas = {}
        
        for venta in ventas:
            codigo = venta.codigo_zapato
            
            if codigo not in estadisticas:
                estadisticas[codigo] = {
                    'nombre': venta.nombre_zapato,
                    'cantidad_vendida': 0,
                    'total_ingresos': 0.0,
                    'numero_ventas': 0
                }
            
            estadisticas[codigo]['cantidad_vendida'] += venta.cantidad
            estadisticas[codigo]['total_ingresos'] += venta.total
            estadisticas[codigo]['numero_ventas'] += 1
        
        return estadisticas

