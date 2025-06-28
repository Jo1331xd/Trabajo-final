from models.classes import Inventario
from dao.inventario_dao import InventarioDao

# Crea el objeto que maneja todos los datos del inventario
dao = InventarioDao()

# Credenciales de acceso al sistema (usuario y clave predefinidos)
USUARIO = "admin"
CLAVE = "123456"

# Función para registrar un nuevo zapato en el inventario
def registrar_zapato():
    print("\n=== REGISTRAR NUEVO ZAPATO ===")
    
    nombre = input("Nombre del zapato: ")  # Pide nombre y valida que no esté vacío
    if nombre == "":
        print("El nombre no puede estar vacío.\n")
        return
    
    try:
        # Pide el precio y valida que sea un número mayor a 0
        precio = float(input("Precio: C$"))
        if precio <= 0:
            print("El precio debe ser mayor a 0.\n")
            return
    except:
        print("Error: Ingrese un precio válido.\n")
        return
        
    try:
        # Pide el stock y valida que sea un número mayor a 0
        stock = int(input("Cantidad de pares: "))
        if stock <= 0:
            print("El stock debe ser mayor a 0.\n")
            return
    except:
        print("Error: Ingrese una cantidad válida.\n")
        return
        
    try:
        # Pide la talla y valida que sea un número mayor a 0
        talla = int(input("Talla: "))
        if talla <= 0:
            print("La talla debe ser mayor a 0.\n")
            return
    except:
        print("Error: Ingrese una talla válida.\n")
        return
        
    # Pide el género, edad, y estilo sin validaciones adicionales
    genero = input("Género (Masculino/Femenino): ")
    edad = input("Edad (Niño/Joven/Adulto): ")
    estilo = input("Estilo (Casual/Deportivo/Formal): ")
    
    # Crea el nuevo zapato con los datos ingresados y lo guarda
    producto = Inventario(nombre, precio, stock, talla, genero, edad, estilo)
    dao.add(producto)
    print(f"\n Zapato registrado con éxito. ID: {producto.id_zapato}\n")

# Función que muestra el inventario en formato de tabla
def mostrar_inventario():
    dao.mostrar_inventario()

# Función para registrar una venta de zapatos
def registrar_venta():
    print("\nProductos disponibles:")
    if not dao.productos:
        print("No hay productos registrados.\n")
        return
    
    # Mostrar productos con contador manual (sin usar enumerate)
    contador = 1
    for producto in dao.productos:
        print(f"{contador}. {producto.nombre} (ID: {producto.id_zapato}) - Stock: {producto.stock}")
        contador = contador + 1
    
    try:
        # Pide al usuario que seleccione un producto
        opcion = int(input("\nSeleccione el número del producto: ")) - 1
        if 0 <= opcion < len(dao.productos):
            producto = dao.productos[opcion]
            cantidad = int(input("¿Cuántos pares se vendieron?: "))
            
            # Intenta registrar la venta
            if dao.registrar_venta(producto, cantidad):
                print("Venta registrada con éxito.\n")
            else:
                print(f"No hay suficientes pares en inventario. Stock actual: {producto.stock}\n")
        else:
            print("Opción no válida.\n")
    except ValueError:
        print("Por favor ingrese un número válido.\n")

# Función auxiliar que muestra productos numerados para editar/eliminar
def mostrar_productos_con_numeros():
    print("\nProductos registrados:")
    contador = 1
    for producto in dao.productos:
        print(f"{contador}. {producto.nombre} (ID: {producto.id_zapato})")
        contador = contador + 1

# Función para editar el precio y stock de un zapato existente
def editar_zapato():
    if not dao.productos:
        print("No hay productos registrados.\n")
        return
    
    mostrar_productos_con_numeros()  # Muestra lista numerada de productos
    
    try:
        # Pide al usuario seleccionar qué producto editar
        opcion_producto = int(input("\nSeleccione el número del producto a editar: ")) - 1
        if 0 <= opcion_producto < len(dao.productos):
            producto = dao.productos[opcion_producto]
            
            try:
                # Pide nuevos valores y los valida
                nuevo_precio = float(input(f"Nuevo precio (actual: C${producto.precio:.2f}): "))
                nuevo_stock = int(input(f"Nuevo stock (actual: {producto.stock}): "))
                if nuevo_precio <= 0 or nuevo_stock < 0:
                    print("Error: El precio debe ser mayor a 0 y el stock no puede ser negativo.\n")
                    return
                # Actualiza los valores y guarda
                producto.precio = nuevo_precio
                producto.stock = nuevo_stock
                dao.guardar_datos()
                print("Producto editado con éxito.\n")
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.\n")
        else:
            print("Producto no válido.\n")
    except ValueError:
        print("Por favor ingrese un número válido.\n")

# Función para eliminar un zapato del inventario
def eliminar_zapato():
    if not dao.productos:
        print("No hay productos registrados.\n")
        return
    
    mostrar_productos_con_numeros()  # Muestra lista numerada de productos
    
    try:
        # Pide al usuario seleccionar qué producto eliminar
        opcion_producto = int(input("\nSeleccione el número del producto a eliminar: ")) - 1
        if 0 <= opcion_producto < len(dao.productos):
            producto = dao.productos[opcion_producto]
            # Pide confirmación antes de eliminar
            confirmacion = input(f"¿Está seguro de eliminar '{producto.nombre}'? (s/n): ")
            if confirmacion.lower() == "s":
                dao.eliminar_producto(producto)  # Elimina el producto
                print("Producto eliminado con éxito.\n")
            else:
                print("Eliminación cancelada.\n")
        else:
            print("Producto no válido.\n")
    except ValueError:
        print("Por favor ingrese un número válido.\n")

# Función que muestra un resumen de todas las ventas realizadas
def resumen_venta():
    total_pares = 0
    total_ganancia = 0
    print("\nResumen de ventas:")
    print("-" * 50)
    
    # Filtra solo productos que se han vendido
    productos_vendidos = [p for p in dao.productos if p.vendidos > 0]
    if not productos_vendidos:
        print("No se han registrado ventas aún.\n")
        return
    
    # Recorre productos vendidos y calcula totales
    for producto in productos_vendidos:
        ganancia = producto.vendidos * producto.precio
        print(f"{producto.nombre}: {producto.vendidos} pares vendidos - Ganancia: C${ganancia:.2f}")
        total_pares += producto.vendidos
        total_ganancia += ganancia
    
    # Muestra el resumen total
    print("-" * 50)
    print(f"Total de pares vendidos: {total_pares}")
    print(f"Ganancia total: C${total_ganancia:.2f}\n")

# Función que muestra el historial completo de productos registrados
def mostrar_historial():
    dao.mostrar_historial()

# Función que maneja el inicio de sesión con 3 intentos máximo
def iniciar_sesion():
    print("\n" + "="*50)
    print("    SISTEMA DE GESTIÓN DE INVENTARIO")
    print("           INICIO DE SESIÓN")
    print("="*50)
    
    intentos = 0  # Contador de intentos fallidos
    
    # Permite hasta 3 intentos de inicio de sesión
    while intentos < 3:
        print(f"\nIntento {intentos + 1} de 3")
        
        # Pide usuario y clave
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        
        # Verifica si las credenciales son correctas
        if usuario == USUARIO and clave == CLAVE:
            print("\n Acceso permitido")
            print("Bienvenido al sistema de inventario\n")
            return True  # Acceso exitoso
        else:
            intentos = intentos + 1
            if intentos < 3:
                print(f"\n Clave incorrecta. Acceso denegado.")
                print(f"Le quedan {3 - intentos} intentos.")
            else:
                print("\n Clave incorrecta. Acceso denegado.")
                print("Se han agotado los intentos. Cerrando programa...")
                return False  # Acceso denegado
    
    return False

# Función principal que muestra el menú y maneja las opciones del usuario
def menu():
    while True:  # Bucle infinito hasta que el usuario seleccione salir
        try:
            # Muestra las opciones disponibles
            print("===== MENÚ DE OPCIONES =====")
            print("1. Registrar zapato")
            print("2. Mostrar inventario ")
            print("3. Registrar venta")
            print("4. Editar zapato")
            print("5. Eliminar zapato")
            print("6. Resumen de ventas")
            print("7. Historial completo")
            print("8. Salir")
            opcion = input("Seleccione una opción: ")

            # Ejecuta la función correspondiente según la opción elegida
            if opcion == "1":
                registrar_zapato()
            elif opcion == "2":
                mostrar_inventario()
            elif opcion == "3":
                registrar_venta()
            elif opcion == "4":
                editar_zapato()
            elif opcion == "5":
                eliminar_zapato()
            elif opcion == "6":
                resumen_venta()
            elif opcion == "7":
                mostrar_historial()
            elif opcion == "8":
                print("Saliendo del programa...")
                break  # Sale del bucle y termina el programa
            else:
                print("Opción no válida. Intente de nuevo.\n")
                
        except Exception as e:
            # Maneja errores inesperados sin cerrar el programa
            print(f"\nERROR: Ha ocurrido un problema - {str(e)}")
            print("El programa se reiniciará automáticamente...\n")

# Función principal que inicia todo el sistema
def iniciar_programa():
    if iniciar_sesion():  # Si el inicio de sesión es exitoso
        menu()            # Muestra el menú principal
    else:                 # Si falla el inicio de sesión
        print("\nAdiós.....")
        exit()            # Cierra el programa

if __name__ == "__main__":
    iniciar_programa()
