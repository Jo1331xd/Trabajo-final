import json
import os
from models.classes import Inventario, HistorialVenta

class InventarioDao:
    def __init__(self):
        self.productos = []
        self.historial_ventas = []
        self.ultimo_id_zapato = 0
        self.ultimo_id_venta = 0
        
        # Crear carpeta data si no existe
        self.data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        self.inventario_file = os.path.join(self.data_dir, "inventario.json")
        self.ventas_file = os.path.join(self.data_dir, "historial_ventas.json")
        self.contadores_file = os.path.join(self.data_dir, "contadores.json")
        
        self.cargar_datos()
    
    def cargar_datos(self):
        try:
            # Cargar inventario
            if os.path.exists(self.inventario_file):
                with open(self.inventario_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.productos = [Inventario.from_dict(item) for item in data]
            
            # Cargar historial de ventas
            if os.path.exists(self.ventas_file):
                with open(self.ventas_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.historial_ventas = [HistorialVenta.from_dict(item) for item in data]
            
            # Cargar contadores
            if os.path.exists(self.contadores_file):
                with open(self.contadores_file, 'r', encoding='utf-8') as f:
                    contadores = json.load(f)
                    self.ultimo_id_zapato = contadores.get('ultimo_id_zapato', 0)
                    self.ultimo_id_venta = contadores.get('ultimo_id_venta', 0)
        except:
            pass
    
    def generar_id_zapato(self):
        """Genera un nuevo ID de zapato en formato ZAP-00001"""
        self.ultimo_id_zapato += 1
        return f"ZAP-{self.ultimo_id_zapato:05d}"
    
    def generar_id_venta(self):
        """Genera un nuevo ID de venta en formato VEN-00001"""
        self.ultimo_id_venta += 1
        return f"VEN-{self.ultimo_id_venta:05d}"
    
    def guardar_datos(self):
        try:
            # Guardar inventario
            with open(self.inventario_file, 'w', encoding='utf-8') as f:
                data = [producto.to_dict() for producto in self.productos]
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Guardar historial de ventas
            with open(self.ventas_file, 'w', encoding='utf-8') as f:
                data = [venta.to_dict() for venta in self.historial_ventas]
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Guardar contadores
            with open(self.contadores_file, 'w', encoding='utf-8') as f:
                contadores = {
                    'ultimo_id_zapato': self.ultimo_id_zapato,
                    'ultimo_id_venta': self.ultimo_id_venta
                }
                json.dump(contadores, f, indent=2)
        except:
            pass
    
    def add(self, producto):
        # Asignar ID si no lo tiene
        if not producto.id_zapato:
            producto.id_zapato = self.generar_id_zapato()
        self.productos.append(producto)
        self.guardar_datos()
    
    def buscar_por_id(self, id_zapato):
        for producto in self.productos:
            if producto.id_zapato == id_zapato:
                return producto
        return None
    
    def buscar_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            self.guardar_datos()
    
    def registrar_venta(self, producto, cantidad):
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            producto.vendidos += cantidad
            
            venta = HistorialVenta(producto.id_zapato, producto.nombre, cantidad, producto.precio)
            venta.id_venta = self.generar_id_venta()
            self.historial_ventas.append(venta)
            self.guardar_datos()
            return True
        return False
    
    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        
        print("\n" + "-"*100)
        print("INVENTARIO ACTUAL - TIENDA DE ZAPATOS")
        print("-"*100)
        
        print(f"| {'ID':<9} | {'NOMBRE':<19} | {'PRECIO':<9} | {'STOCK':<7} | {'TALLA':<7} | {'GENERO':<11} | {'VENDIDOS':<9} | {'GANANCIA':<11} |")
        print("|" + "-"*11 + "|" + "-"*21 + "|" + "-"*11 + "|" + "-"*9 + "|" + "-"*9 + "|" + "-"*13 + "|" + "-"*11 + "|" + "-"*13 + "|")
        
        total_ganancia = 0
        for producto in self.productos:
            ganancia = producto.vendidos * producto.precio
            total_ganancia += ganancia
            print(f"| {producto.id_zapato:<9} | {producto.nombre[:19]:<19} | ${producto.precio:<8.2f} | {producto.stock:<7} | {producto.talla:<7} | {producto.genero[:11]:<11} | {producto.vendidos:<9} | ${ganancia:<10.2f} |")
        
        print("-"*100)
        print(f"GANANCIA TOTAL: ${total_ganancia:.2f}")
        print("-"*100 + "\n")
    
    def mostrar_historial(self):
        if not self.productos:
            print("No hay registros en el historial.")
            return
        
        print("\n" + "-"*80)
        print("HISTORIAL COMPLETO DE REGISTROS")
        print("-"*80)
        
        for i, producto in enumerate(self.productos, 1):
            print(f"\n[{i}] " + "-"*50)
            print(producto)
        
        print("-"*80 + "\n")
