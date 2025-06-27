import pickle
import os
from models.classes import Inventario, HistorialVenta

class InventarioDao:
    def __init__(self):
        self.productos = []
        self.historial_ventas = []
        self.ultimo_id_zapato = 0
        self.ultimo_id_venta = 0
        
        self.inventario_file = os.path.join(os.path.dirname(__file__), "..", "inventario.bin")
        self.ventas_file = os.path.join(os.path.dirname(__file__), "..", "historial_ventas.bin")
        self.contadores_file = os.path.join(os.path.dirname(__file__), "..", "contadores.bin")
        
        self.cargar_datos()
    
    def cargar_datos(self):
        try:
            if os.path.exists(self.inventario_file):
                with open(self.inventario_file, "rb") as f:
                    self.productos = pickle.load(f)
            
            if os.path.exists(self.ventas_file):
                with open(self.ventas_file, "rb") as f:
                    self.historial_ventas = pickle.load(f)
            
            if os.path.exists(self.contadores_file):
                with open(self.contadores_file, "rb") as f:
                    contadores = pickle.load(f)
                    self.ultimo_id_zapato = contadores.get("ultimo_id_zapato", 0)
                    self.ultimo_id_venta = contadores.get("ultimo_id_venta", 0)
        except:
            pass
    
    def generar_id_zapato(self):
        self.ultimo_id_zapato += 1
        return f"ZAP-{self.ultimo_id_zapato:05d}"
    
    def generar_id_venta(self):
        self.ultimo_id_venta += 1
        return f"VEN-{self.ultimo_id_venta:05d}"
    
    def guardar_datos(self):
        try:
            with open(self.inventario_file, "wb") as f:
                pickle.dump(self.productos, f)
            
            with open(self.ventas_file, "wb") as f:
                pickle.dump(self.historial_ventas, f)
            
            with open(self.contadores_file, "wb") as f:
                contadores = {
                    "ultimo_id_zapato": self.ultimo_id_zapato,
                    "ultimo_id_venta": self.ultimo_id_venta
                }
                pickle.dump(contadores, f)
        except:
            pass
    
    def add(self, producto):
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
