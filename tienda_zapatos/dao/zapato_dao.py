"""
ZapatoDAO - Manejo de datos de zapatos
"""

from .base_dao import BaseDAO
from models.zapato import Zapato

class ZapatoDAO(BaseDAO):
    def __init__(self):
        super().__init__("zapatos.txt")
    
    def guardar_zapato(self, zapato):
        """
        Guarda un zapato en el archivo
        
        Args:
            zapato (Zapato): Objeto zapato a guardar
            
        Returns:
            bool: True si se guardó correctamente, False en caso contrario
        """
        if self.buscar_por_codigo(zapato.codigo):
            print(f"Error: Ya existe un zapato con el código {zapato.codigo}")
            return False
        
        return self._agregar_linea(zapato.to_string())
    
    def obtener_todos(self):
        """
        Obtiene todos los zapatos del archivo
        
        Returns:
            list: Lista de objetos Zapato
        """
        lineas = self._leer_archivo()
        zapatos = []
        
        for linea in lineas:
            zapato = Zapato.from_string(linea)
            if zapato:
                zapatos.append(zapato)
        
        return zapatos
    
    def buscar_por_codigo(self, codigo):
        """
        Busca un zapato por su código
        
        Args:
            codigo (str): Código del zapato a buscar
            
        Returns:
            Zapato: Objeto Zapato si se encuentra, None en caso contrario
        """
        zapatos = self.obtener_todos()
        for zapato in zapatos:
            if zapato.codigo == codigo:
                return zapato
        return None
    
    def buscar_por_nombre(self, nombre):
        """
        Busca zapatos por nombre (búsqueda parcial)
        
        Args:
            nombre (str): Nombre o parte del nombre a buscar
            
        Returns:
            list: Lista de zapatos que coinciden
        """
        zapatos = self.obtener_todos()
        encontrados = []
        
        for zapato in zapatos:
            if nombre.lower() in zapato.nombre.lower():
                encontrados.append(zapato)
        
        return encontrados
    
    def actualizar_zapato(self, codigo, zapato_actualizado):
        """
        Actualiza un zapato existente
        
        Args:
            codigo (str): Código del zapato a actualizar
            zapato_actualizado (Zapato): Nuevo objeto zapato
            
        Returns:
            bool: True si se actualizó correctamente, False en caso contrario
        """
        zapatos = self.obtener_todos()
        encontrado = False
        
        for i, zapato in enumerate(zapatos):
            if zapato.codigo == codigo:
                zapatos[i] = zapato_actualizado
                encontrado = True
                break
        
        if encontrado:
            lineas = [zapato.to_string() for zapato in zapatos]
            return self._escribir_archivo(lineas)
        
        return False
    
    def eliminar_zapato(self, codigo):
        """
        Elimina un zapato por su código
        
        Args:
            codigo (str): Código del zapato a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False en caso contrario
        """
        zapatos = self.obtener_todos()
        zapatos_filtrados = [zapato for zapato in zapatos if zapato.codigo != codigo]
        
        if len(zapatos_filtrados) < len(zapatos):
            lineas = [zapato.to_string() for zapato in zapatos_filtrados]
            return self._escribir_archivo(lineas)
        
        return False
    
    def actualizar_stock(self, codigo, nueva_cantidad):
        """
        Actualiza solo el stock de un zapato
        
        Args:
            codigo (str): Código del zapato
            nueva_cantidad (int): Nueva cantidad en stock
            
        Returns:
            bool: True si se actualizó correctamente, False en caso contrario
        """
        zapato = self.buscar_por_codigo(codigo)
        if zapato:
            zapato.cantidad = nueva_cantidad
            return self.actualizar_zapato(codigo, zapato)
        return False

