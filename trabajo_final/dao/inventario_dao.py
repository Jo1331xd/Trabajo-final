import pickle  # Para guardar datos en archivos binarios
import os      # Para manejar archivos del sistema
from models.classes import Inventario, HistorialVenta

# Clase que maneja todos los datos del inventario y las ventas
class InventarioDao:
    # Constructor - prepara las listas y archivos necesarios
    def __init__(self):
        self.productos = []           # Lista que guarda todos los zapatos
        self.historial_ventas = []    # Lista que guarda todas las ventas
        self.ultimo_id_zapato = 0     # Contador para generar IDs únicos de zapatos
        self.ultimo_id_venta = 0      # Contador para generar IDs únicos de ventas
        
        # Nombres de archivos donde se guardan los datos
        self.archivo_inventario = "inventario.bin"
        self.archivo_ventas = "historial_ventas.bin"
        self.archivo_contadores = "contadores.bin"
        
        self.cargar_datos()  # Carga los datos guardados al iniciar
    
    # Función que carga todos los datos guardados desde los archivos
    def cargar_datos(self):
        try:
            # Si existe archivo de inventario, lo carga
            if os.path.exists(self.archivo_inventario):
                with open(self.archivo_inventario, "rb") as f:
                    self.productos = pickle.load(f)
            
            # Si existe archivo de ventas, lo carga
            if os.path.exists(self.archivo_ventas):
                with open(self.archivo_ventas, "rb") as f:
                    self.historial_ventas = pickle.load(f)
            
            # Si existe archivo de contadores, lo carga
            if os.path.exists(self.archivo_contadores):
                with open(self.archivo_contadores, "rb") as f:
                    contadores = pickle.load(f)
                    self.ultimo_id_zapato = contadores.get("ultimo_id_zapato", 0)
                    self.ultimo_id_venta = contadores.get("ultimo_id_venta", 0)
        except:
            pass  # Si hay error, continúa con valores por defecto
    
    # Función que crea un ID único para cada zapato
    def generar_id_zapato(self):
        self.ultimo_id_zapato += 1
        return f"ZAP-{self.ultimo_id_zapato:05d}"  # Formato: ZAP-00001
    
    # Función que crea un ID único para cada venta
    def generar_id_venta(self):
        self.ultimo_id_venta += 1
        return f"VEN-{self.ultimo_id_venta:05d}"  # Formato: VEN-00001
    
    # Función que guarda todos los datos en archivos
    def guardar_datos(self):
        try:
            # Guarda la lista de productos
            with open(self.archivo_inventario, "wb") as f:
                pickle.dump(self.productos, f)
            
            # Guarda la lista de ventas
            with open(self.archivo_ventas, "wb") as f:
                pickle.dump(self.historial_ventas, f)
            
            # Guarda los contadores de IDs
            with open(self.archivo_contadores, "wb") as f:
                contadores = {
                    "ultimo_id_zapato": self.ultimo_id_zapato,
                    "ultimo_id_venta": self.ultimo_id_venta
                }
                pickle.dump(contadores, f)
        except:
            pass  # Si hay error, continúa sin guardar
    
    # Función que agrega un nuevo zapato al inventario
    def add(self, producto):
        if not producto.id_zapato:  # Si no tiene ID, le asigna uno
            producto.id_zapato = self.generar_id_zapato()
        self.productos.append(producto)  # Lo agrega a la lista
        self.guardar_datos()  # Guarda los cambios
    
    # Función que busca un zapato por su ID
    def buscar_por_id(self, id_zapato):
        for producto in self.productos:
            if producto.id_zapato == id_zapato:
                return producto  # Devuelve el zapato si lo encuentra
        return None  # Devuelve None si no lo encuentra
    
    # Función que busca un zapato por su nombre
    def buscar_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():  # Compara sin importar mayúsculas
                return producto
        return None
    
    # Función que elimina un zapato del inventario
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)  # Lo quita de la lista
            self.guardar_datos()  # Guarda los cambios
    
    # Función que registra una venta de zapatos
    def registrar_venta(self, producto, cantidad):
        if producto.stock >= cantidad:  # Verifica si hay suficientes zapatos
            producto.stock -= cantidad      # Reduce el stock
            producto.vendidos += cantidad   # Aumenta los vendidos
            
            # Crea registro de la venta
            venta = HistorialVenta(producto.id_zapato, producto.nombre, cantidad, producto.precio)
            venta.id_venta = self.generar_id_venta()
            self.historial_ventas.append(venta)
            self.guardar_datos()
            return True  # Venta exitosa
        return False  # No hay suficiente stock
    
    # Función que muestra el inventario en formato de tabla organizada
    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        
        # Dibuja la tabla con líneas y encabezados
        print("\n" + "-"*120)
        print("                    INVENTARIO ACTUAL - TIENDA DE ZAPATOS")
        print("-"*120)
        
        # Cabecera de la tabla con columnas organizadas
        print(f"| {'ID':<12} | {'NOMBRE':<20} | {'PRECIO':<10} | {'STOCK':<8} | {'TALLA':<8} | {'GENERO':<12} | {'VENDIDOS':<10} | {'GANANCIA':<12} |")
        print("|" + "-"*14 + "|" + "-"*22 + "|" + "-"*12 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*14 + "|" + "-"*12 + "|" + "-"*14 + "|")
        
        # Recorre todos los productos y los muestra en la tabla
        total_ganancia = 0
        for producto in self.productos:
            ganancia = producto.vendidos * producto.precio  # Calcula ganancia de cada producto
            total_ganancia += ganancia  # Suma al total
            print(f"| {producto.id_zapato:<12} | {producto.nombre[:20]:<20} | C${producto.precio:<9.2f} | {producto.stock:<8} | {producto.talla:<8} | {producto.genero[:12]:<12} | {producto.vendidos:<10} | C${ganancia:<11.2f} |")
        
        # Muestra el total al final
        print("-"*120)
        print(f"                          GANANCIA TOTAL: C${total_ganancia:.2f}")
        print("-"*120 + "\n")
    
    # Función que muestra todos los productos registrados con detalles completos
    def mostrar_historial(self):
        if not self.productos:
            print("No hay registros en el historial.")
            return
        
        print("\n" + "-"*80)
        print("HISTORIAL COMPLETO DE REGISTROS")
        print("-"*80)
        
        # Muestra cada producto numerado con todos sus detalles
        contador = 1
        for producto in self.productos:
            print(f"\n[{contador}] " + "-"*50)
            print(producto)  # Usa la función __str__ de la clase Inventario
            contador = contador + 1
        
        print("-"*80 + "\n")
