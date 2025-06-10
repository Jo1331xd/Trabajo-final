import models

inventario_productos = []

def mostrar_menu():
    """Muestra las opciones del menú al usuario."""
    print("\n--- GESTIÓN DE INVENTARIO ---")
    print("1. Agregar nuevo producto")
    print("2. Ver productos en inventario")
    print("3. Buscar producto por nombre")
    print("4. Realizar venta (disminuir stock)")
    print("5. Salir")
    print("------------------------------")

def agregar_producto():
    """Permite al usuario agregar un nuevo producto al inventario."""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio: $"))
        stock = int(input("Stock inicial (pares): "))
        talla = input("Talla: ")
        genero = input("Género (ej. 'Masculino', 'Femenino', 'Unisex'): ")
        edad = input("Edad (ej. 'Adulto', 'Niño'): ")
        estilo = input("Estilo (ej. 'Deportivo', 'Casual', 'Formal'): ")

        nuevo_producto = models.Inventario(nombre, precio, stock, talla, genero, edad, estilo)
        inventario_productos.append(nuevo_producto)
        print(f"\nProducto '{nombre}' agregado con éxito.")
    except ValueError:
        print("Error: El precio y el stock deben ser números válidos.")
    input("Presiona Enter para volver al menú...")

def ver_inventario():
    """Muestra todos los productos actualmente en el inventario."""
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario_productos:
        print("No hay productos en el inventario aún.")
    else:
        for i, producto in enumerate(inventario_productos):
            print(f"\n--- Producto #{i+1} ---")
            print(producto) 
    input("Presiona Enter para volver al menú...")

def buscar_producto():
    """Busca un producto por nombre y muestra su información."""
    print("\n--- BUSCAR PRODUCTO ---")
    if not inventario_productos:
        print("No hay productos para buscar.")
        input("Presiona Enter para volver al menú...")
        return

    nombre_buscado = input("Ingresa el nombre del producto a buscar: ").strip().lower()
    encontrado = False
    for producto in inventario_productos:
        if producto.nombre.lower() == nombre_buscado:
            print("\n--- Producto Encontrado ---")
            print(producto)
            encontrado = True
            break
    if not encontrado:
        print(f"Producto '{nombre_buscado}' no encontrado en el inventario.")
    input("Presiona Enter para volver al menú...")

def realizar_venta():
    """Permite 'vender' un producto, disminuyendo su stock."""
    print("\n--- REALIZAR VENTA ---")
    if not inventario_productos:
        print("No hay productos en el inventario para vender.")
        input("Presiona Enter para volver al menú...")
        return

    nombre_venta = input("Nombre del producto a vender: ").strip().lower()
    cantidad_venta = 0
    try:
        cantidad_venta = int(input("Cantidad a vender: "))
        if cantidad_venta <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
            input("Presiona Enter para volver al menú...")
            return
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        input("Presiona Enter para volver al menú...")
        return

    producto_encontrado = None
    for producto in inventario_productos:
        if producto.nombre.lower() == nombre_venta:
            producto_encontrado = producto
            break

    if producto_encontrado:
        if producto_encontrado.stock >= cantidad_venta:
            producto_encontrado.stock -= cantidad_venta
            producto_encontrado.vendidos += cantidad_venta
            print(f"Venta realizada: {cantidad_venta} pares de '{producto_encontrado.nombre}'.")
            print(f"Nuevo stock de '{producto_encontrado.nombre}': {producto_encontrado.stock}")
        else:
            print(f"Stock insuficiente para '{producto_encontrado.nombre}'. Stock actual: {producto_encontrado.stock}")
    else:
        print(f"Producto '{nombre_venta}' no encontrado en el inventario.")
    input("Presiona Enter para volver al menú...")


def main():
    """Función principal que ejecuta el bucle del menú."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ver_inventario()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            realizar_venta()
        elif opcion == '5':
            print("\nSaliendo del programa de gestión de inventario. ¡Hasta luego!")
            break  # Sale del bucle y termina el programa
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            input("Presiona Enter para intentar de nuevo...")

if __name__ == "__main__":
    main()