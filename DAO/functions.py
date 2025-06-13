from models.Inventario import Inventario

class InventarioDao:
    def __init__(self):
        self.productos = []

    def add(self, producto):
        self.productos.append(producto)

def show(self):
    print("Lista de productos disponibles:")
    print("\n")
    for producto in self.productos:
        print(producto)