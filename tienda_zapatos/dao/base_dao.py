"""
DAO Base - Funcionalidad común para manejo de archivos
"""

import os

class BaseDAO:
    def __init__(self, archivo):
        """
        Inicializa el DAO base
        
        Args:
            archivo (str): Nombre del archivo donde se guardarán los datos
        """
        self.archivo = os.path.join("data", archivo)
        self._crear_directorio_si_no_existe()
    
    def _crear_directorio_si_no_existe(self):
        """Crea el directorio data si no existe"""
        if not os.path.exists("data"):
            os.makedirs("data")
    
    def _leer_archivo(self):
        """Lee todas las líneas del archivo"""
        if not os.path.exists(self.archivo):
            return []
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as file:
                return [linea.strip() for linea in file.readlines() if linea.strip()]
        except Exception as e:
            print(f"Error al leer archivo {self.archivo}: {e}")
            return []
    
    def _escribir_archivo(self, lineas):
        """Escribe todas las líneas al archivo"""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as file:
                for linea in lineas:
                    file.write(linea + '\n')
            return True
        except Exception as e:
            print(f"Error al escribir archivo {self.archivo}: {e}")
            return False
    
    def _agregar_linea(self, linea):
        """Agrega una línea al final del archivo"""
        try:
            with open(self.archivo, 'a', encoding='utf-8') as file:
                file.write(linea + '\n')
            return True
        except Exception as e:
            print(f"Error al agregar línea al archivo {self.archivo}: {e}")
            return False

