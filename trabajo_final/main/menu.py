from models.classes import Inventario
from dao.inventario_dao import InventarioDao

dao = InventarioDao()

def registrar_zapato():
    try:
        nombre = input("Nombre del zapato: ")
        if not nombre.strip():
            print("El nombre no puede estar vacío.\n")
            return
        
        precio = float(input("Precio: "))
        if precio <= 0:
            print("El precio debe ser mayor a 0.\n")
            return
            
        stock = int(input("Cantidad de pares: "))
        if stock <= 0:
            print("El stock debe ser mayor a 0.\n")
            return
            
        talla = int(input("Talla: "))
        if talla <= 0:
            print("La talla debe ser mayor a 0.\n")
            return
            
        genero = input("Género (Masculino/Femenino): ")
        edad = input("Edad (Niño/Joven/Adulto): ")
        estilo = input("Estilo (Casual, Deportivo, etc.): ")
        
        producto = Inventario(nombre, precio, stock, talla, genero, edad, estilo)
        dao.add(producto)
        print(f"Zapato registrado con éxito. ID asignado: {producto.id_zapato}\n")
        
    except ValueError:
        print("Error: Por favor ingrese valores válidos (números para precio, stock y talla).\n")

def mostrar_inventario():
    dao.mostrar_inventario()

def registrar_venta():
    print("\nProductos disponibles:")
    if not dao.productos:
        print("No hay productos registrados.\n")
        return
    
    for i, producto in enumerate(dao.productos, 1):
        print(f"{i}. {producto.nombre} (ID: {producto.id_zapato}) - Stock: {producto.stock}")
    
    try:
        opcion = int(input("\nSeleccione el número del producto: ")) - 1
        if 0 <= opcion < len(dao.productos):
            producto = dao.productos[opcion]
            cantidad = int(input("¿Cuántos pares se vendieron?: "))
            
            if dao.registrar_venta(producto, cantidad):
                print("Venta registrada con éxito.\n")
            else:
                print(f"No hay suficientes pares en inventario. Stock actual: {producto.stock}\n")
        else:
            print("Opción no válida.\n")
    except ValueError:
        print("Por favor ingrese un número válido.\n")

def indice_registro():
    if not dao.productos:
        print("No hay productos registrados.\n")
        return
    
    print("\nProductos registrados:")
    for i, producto in enumerate(dao.productos, 1):
        print(f"{i}. {producto.nombre} (ID: {producto.id_zapato})")
    
    try:
        opcion_producto = int(input("\nSeleccione el número del producto: ")) - 1
        if 0 <= opcion_producto < len(dao.productos):
            producto = dao.productos[opcion_producto]
            
            print("\n1. Editar zapato")
            print("2. Eliminar zapato")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                try:
                    nuevo_precio = float(input(f"Nuevo precio (actual: ${producto.precio:.2f}): "))
                    nuevo_stock = int(input(f"Nuevo stock (actual: {producto.stock}): "))
                    if nuevo_precio <= 0 or nuevo_stock < 0:
                        print("Error: El precio debe ser mayor a 0 y el stock no puede ser negativo.\n")
                        return
                    producto.precio = nuevo_precio
                    producto.stock = nuevo_stock
                    dao.guardar_datos()
                    print("Producto editado con éxito.\n")
                except ValueError:
                    print("Error: Por favor ingrese valores numéricos válidos.\n")
            elif opcion == "2":
                dao.eliminar_producto(producto)
                print("Producto eliminado con éxito.\n")
            else:
                print("Opción no válida.\n")
        else:
            print("Producto no válido.\n")
    except ValueError:
        print("Por favor ingrese un número válido.\n")

def resumen_venta():
    total_pares = 0
    total_ganancia = 0
    print("\nResumen de ventas:")
    print("-" * 50)
    
    productos_vendidos = [p for p in dao.productos if p.vendidos > 0]
    if not productos_vendidos:
        print("No se han registrado ventas aún.\n")
        return
    
    for producto in productos_vendidos:
        ganancia = producto.vendidos * producto.precio
        print(f"{producto.nombre}: {producto.vendidos} pares vendidos - Ganancia: ${ganancia:.2f}")
        total_pares += producto.vendidos
        total_ganancia += ganancia
    
    print("-" * 50)
    print(f"Total de pares vendidos: {total_pares}")
    print(f"Ganancia total: ${total_ganancia:.2f}\n")

def mostrar_historial():
    dao.mostrar_historial()

def menu():
    while True:
        try:
            print("===== MENÚ DE OPCIONES =====")
            print("1. Registrar zapato")
            print("2. Mostrar inventario (matriz)")
            print("3. Registrar venta")
            print("4. Editar/Eliminar zapato")
            print("5. Resumen de ventas")
            print("6. Historial completo")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                registrar_zapato()
            elif opcion == "2":
                mostrar_inventario()
            elif opcion == "3":
                registrar_venta()
            elif opcion == "4":
                indice_registro()
            elif opcion == "5":
                resumen_venta()
            elif opcion == "6":
                mostrar_historial()
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.\n")
                
        except Exception as e:
            print(f"\nERROR: Ha ocurrido un problema - {str(e)}")
            print("El programa se reiniciará automáticamente...\n")

if __name__ == "__main__":
    menu()
