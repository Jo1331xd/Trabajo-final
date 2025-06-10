class Inventario:
    def __init__(self, nombre, precio, stock, talla, genero, edad, estilo):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.talla = talla
        self.genero = genero
        self.edad = edad
        self.estilo = estilo
        self.vendidos = 0
    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Existencia: {self.stock} pares\n"
            f"Talla: {self.talla}\n"
            f"Género: {self.genero}\n"
            f"Edad: {self.edad}\n"
            f"Estilo: {self.estilo}\n"
            f"Pares vendidos: {self.vendidos}\n"
        )