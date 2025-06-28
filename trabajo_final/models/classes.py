import time

# Clase que representa un zapato en el inventario
class Inventario:
    # Constructor - guarda toda la información de un zapato cuando se crea
    def __init__(self, nombre, precio, stock, talla, genero, edad, estilo, id_zapato=None):
        self.id_zapato = id_zapato  
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.talla = talla
        self.genero = genero
        self.edad = edad
        self.estilo = estilo
        self.vendidos = 0  # Empieza en 0 porque no se ha vendido nada
        self.fecha_registro = time.strftime("%Y-%m-%d %H:%M:%S")  # Fecha actual
    
    # Función que muestra todos los detalles del zapato de forma completa
    def mostrar_info_completa(self):
        ganancia = self.vendidos * self.precio  # Calcula cuánto dinero se ganó con este zapato
        print(f"ID: {self.id_zapato}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: C${self.precio:.2f}")
        print(f"Stock actual: {self.stock} pares")
        print(f"Talla: {self.talla}")
        print(f"Genero: {self.genero}")
        print(f"Edad: {self.edad}")
        print(f"Estilo: {self.estilo}")
        print(f"Pares vendidos: {self.vendidos}")
        print(f"Ganancia generada: C${ganancia:.2f}")
        print(f"Fecha de registro: {self.fecha_registro}")
        print()

    # Función especial que convierte el zapato en texto para mostrarlo
    def __str__(self):
        ganancia = self.vendidos * self.precio
        return (
            f"ID: {self.id_zapato}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: C${self.precio:.2f}\n"
            f"Stock actual: {self.stock} pares\n"
            f"Talla: {self.talla}\n"
            f"Genero: {self.genero}\n"
            f"Edad: {self.edad}\n"
            f"Estilo: {self.estilo}\n"
            f"Pares vendidos: {self.vendidos}\n"
            f"Ganancia generada: C${ganancia:.2f}\n"
            f"Fecha de registro: {self.fecha_registro}\n"
        )

# Clase que guarda información de cada venta realizada
class HistorialVenta:
    # Constructor - guarda los datos de una venta
    def __init__(self, id_zapato, nombre_zapato, cantidad, precio_unitario, id_venta=None):
        self.id_venta = id_venta
        self.id_zapato = id_zapato
        self.nombre_zapato = nombre_zapato
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total_venta = cantidad * precio_unitario  # Calcula el total automáticamente
        self.fecha_venta = time.strftime("%Y-%m-%d %H:%M:%S")  # Fecha actual
    
    # Función que muestra toda la información de la venta
    def mostrar_info_venta(self):
        print(f"ID Venta: {self.id_venta}")
        print(f"ID Zapato: {self.id_zapato}")
        print(f"Producto: {self.nombre_zapato}")
        print(f"Cantidad vendida: {self.cantidad} pares")
        print(f"Precio unitario: C${self.precio_unitario:.2f}")
        print(f"Total de la venta: C${self.total_venta:.2f}")
        print(f"Fecha: {self.fecha_venta}")
        print()
