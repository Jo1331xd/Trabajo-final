from models.classes import Inventario
from dao.inventario_dao import InventarioDao

dao = InventarioDao()

def registrar_zapato():
    nombre = input("Nombre del zapato: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad de pares: "))
    talla = int(input("Talla: "))
    genero = input("Género (Masculino/Femenino/Unisex): ")
    edad = input("Edad (Niño/Joven/Adulto): ")
    estilo = input("Estilo (Casual, Deportivo, etc.): ")
    
    producto = Inventario(nombre, precio, stock, talla, genero, edad, estilo)
    dao.add(producto)
    print("Zapato registrado con éxito.\n")

def mantener_conteo():
    print("Conteo de pares por nombre:\n")
    for producto in dao.productos:
        print(f"{producto.nombre}: {producto.stock} pares")

def registrar_venta():
    nombre = input("Ingrese el nombre del zapato vendido: ")
    cantidad = int(input("¿Cuántos pares se vendieron?: "))
    for producto in dao.productos:
        if producto.nombre == nombre:
            if producto.stock >= cantidad:
                producto.stock -= cantidad
                producto.vendidos += cantidad
                print("Venta registrada con éxito.\n")
            else:
                print("No hay suficientes pares en inventario.\n")
            return
    print("Producto no encontrado.\n")

def indice_registro():
    print("1. Editar zapato")
    print("2. Eliminar zapato")
    opcion = input("Seleccione una opción: ")
    nombre = input("Ingrese el nombre del zapato: ")
    for producto in dao.productos:
        if producto.nombre == nombre:
            if opcion == "1":
                producto.precio = float(input("Nuevo precio: "))
                producto.stock = int(input("Nuevo stock: "))
                print("Producto editado.\n")
            elif opcion == "2":
                dao.productos.remove(producto)
                print("Producto eliminado.\n")
            return
    print("Producto no encontrado.\n")

def resumen_venta():
    total_pares = 0
    total_ganancia = 0
    print("Resumen de ventas:\n")
    for producto in dao.productos:
        if producto.vendidos > 0:
            ganancia = producto.vendidos * producto.precio
            print(f"{producto.nombre}: {producto.vendidos} pares vendidos - Ganancia: ${ganancia:.2f}")
            total_pares += producto.vendidos
            total_ganancia += ganancia
    print(f"\nTotal de pares vendidos: {total_pares}")
    print(f"Ganancia total: ${total_ganancia:.2f}\n")

def menu():
    while True:
        print("===== MENÚ DE OPCIONES =====")
        print("1. Registrar zapato")
        print("2. Mantener conteo de pares")
        print("3. Registrar venta")
        print("4. Índice de registro (Editar/Eliminar)")
        print("5. Resumen de venta")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_zapato()
        elif opcion == "2":
            mantener_conteo()
        elif opcion == "3":
            registrar_venta()
        elif opcion == "4":
            indice_registro()
        elif opcion == "5":
            resumen_venta()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()