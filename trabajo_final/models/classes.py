import time

class Inventario:
    def __init__(self, nombre, precio, stock, talla, genero, edad, estilo, id_zapato=None):
        self.id_zapato = id_zapato  
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.talla = talla
        self.genero = genero
        self.edad = edad
        self.estilo = estilo
        self.vendidos = 0
        self.fecha_registro = time.strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            'id_zapato': self.id_zapato,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'talla': self.talla,
            'genero': self.genero,
            'edad': self.edad,
            'estilo': self.estilo,
            'vendidos': self.vendidos,
            'fecha_registro': self.fecha_registro
        }
    
    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data['nombre'], data['precio'], data['stock'], 
            data['talla'], data['genero'], data['edad'], 
            data['estilo'], data['id_zapato']
        )
        obj.vendidos = data.get('vendidos', 0)
        obj.fecha_registro = data.get('fecha_registro', time.strftime("%Y-%m-%d %H:%M:%S"))
        return obj

    def __str__(self):
        ganancia = self.vendidos * self.precio
        return (
            f"ID: {self.id_zapato}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock actual: {self.stock} pares\n"
            f"Talla: {self.talla}\n"
            f"Genero: {self.genero}\n"
            f"Edad: {self.edad}\n"
            f"Estilo: {self.estilo}\n"
            f"Pares vendidos: {self.vendidos}\n"
            f"Ganancia generada: ${ganancia:.2f}\n"
            f"Fecha de registro: {self.fecha_registro}\n"
        )

class HistorialVenta:
    def __init__(self, id_zapato, nombre_zapato, cantidad, precio_unitario, id_venta=None):
        self.id_venta = id_venta  # Se asignará desde el DAO
        self.id_zapato = id_zapato
        self.nombre_zapato = nombre_zapato
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total_venta = cantidad * precio_unitario
        self.fecha_venta = time.strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            'id_venta': self.id_venta,
            'id_zapato': self.id_zapato,
            'nombre_zapato': self.nombre_zapato,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'total_venta': self.total_venta,
            'fecha_venta': self.fecha_venta
        }
    
    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data['id_zapato'], data['nombre_zapato'], 
            data['cantidad'], data['precio_unitario'], 
            data.get('id_venta')
        )
        obj.total_venta = data.get('total_venta', obj.total_venta)
        obj.fecha_venta = data.get('fecha_venta', obj.fecha_venta)
        return obj
