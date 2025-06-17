"""
Modelo Zapato - Representa un zapato en el sistema
"""

class Zapato:
    def __init__(self, codigo="", nombre="", descripcion="", talla="", genero="", edad="", estilo="", precio=0.0, cantidad=0):
        """
        Inicializa un objeto Zapato
        
        Args:
            codigo (str): Código único del zapato
            nombre (str): Nombre del zapato
            descripcion (str): Descripción detallada
            talla (str): Talla del zapato
            genero (str): Género (Hombre/Mujer/Unisex)
            edad (str): Edad objetivo (Niño/Adulto)
            estilo (str): Estilo del zapato
            precio (float): Precio unitario
            cantidad (int): Cantidad en inventario
        """
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.talla = talla
        self.genero = genero
        self.edad = edad
        self.estilo = estilo
        self.precio = precio
        self.cantidad = cantidad
    
    def to_string(self):
        """Convierte el zapato a string para guardar en archivo"""
        return f"{self.codigo}|{self.nombre}|{self.descripcion}|{self.talla}|{self.genero}|{self.edad}|{self.estilo}|{self.precio}|{self.cantidad}"
    
    @classmethod
    def from_string(cls, linea):
        """Crea un objeto Zapato desde una línea de texto"""
        try:
            datos = linea.strip().split("|")
            if len(datos) == 9:
                return cls(
                    codigo=datos[0],
                    nombre=datos[1],
                    descripcion=datos[2],
                    talla=datos[3],
                    genero=datos[4],
                    edad=datos[5],
                    estilo=datos[6],
                    precio=float(datos[7]),
                    cantidad=int(datos[8])
                )
        except (ValueError, IndexError):
            return None
        return None
    
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} | Talla: {self.talla} | Género: {self.genero} | Precio: ${self.precio:.2f} | Stock: {self.cantidad}"
    
    def __repr__(self):
        return self.__str__()

