"""
Modelo Venta - Representa una venta en el sistema
"""

from datetime import datetime

class Venta:
    def __init__(self, codigo_zapato="", nombre_zapato="", cantidad=0, precio_unitario=0.0, fecha=None):
        """
        Inicializa un objeto Venta
        
        Args:
            codigo_zapato (str): Código del zapato vendido
            nombre_zapato (str): Nombre del zapato vendido
            cantidad (int): Cantidad vendida
            precio_unitario (float): Precio por unidad
            fecha (str): Fecha de la venta
        """
        self.codigo_zapato = codigo_zapato
        self.nombre_zapato = nombre_zapato
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total = cantidad * precio_unitario
    
    def to_string(self):
        """Convierte la venta a string para guardar en archivo"""
        return f"{self.codigo_zapato}|{self.nombre_zapato}|{self.cantidad}|{self.precio_unitario}|{self.total}|{self.fecha}"
    
    @classmethod
    def from_string(cls, linea):
        """Crea un objeto Venta desde una línea de texto"""
        try:
            datos = linea.strip().split("|")
            if len(datos) == 6:
                return cls(
                    codigo_zapato=datos[0],
                    nombre_zapato=datos[1],
                    cantidad=int(datos[2]),
                    precio_unitario=float(datos[3]),
                    fecha=datos[5]
                )
        except (ValueError, IndexError):
            return None
        return None
    
    def __str__(self):
        return f"Venta: {self.nombre_zapato} | Cantidad: {self.cantidad} | Total: ${self.total:.2f} | Fecha: {self.fecha}"
    
    def __repr__(self):
        return self.__str__()

