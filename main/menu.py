from models.Inventario import Inventario

inventario_productos = []

# ──────────────────────────────
def gi(p, t, e, mv=None):
    while True:
        try:
            v = t(input(p))
            if mv is not None and v < mv:
                raise ValueError
            return v
        except ValueError:
            print(e)

def get_option(p, opts):
    while True:
        print(p)
        [print(f"{i+1}. {o}") for i, o in enumerate(opts)]
        try:
            c = int(input("Seleccione una opción: ").strip()) - 1
            if 0 <= c < len(opts):
                return opts[c]
            else:
                print("Opción no válida. Ingrese un número de la lista.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
# ──────────────────────────────
def mostrar_producto(prod: Inventario, numero: int, ancho: int = 45):
    """Imprime los datos del producto dentro de un recuadro ASCII."""
    def borde(izq, relleno, der):
        return f"{izq}{relleno * ancho}{der}"

    def linea(etiqueta, valor):
        texto = f"{etiqueta:<12}: {str(valor)}"
        return f"║ {texto:<{ancho-2}} ║"

    print(borde("╔", "═", "╗"))
    print(f"║ {'Producto #'+str(numero):^{ancho-2}} ║")
    print(borde("╠", "═", "╣"))

    # ✅ ORDEN CORRECTO VISUAL Y LÓGICO
    print(linea("Nombre",    prod.nombre))
    print(linea("Categoría", prod.categoria_edad))
    print(linea("Género",    prod.genero))
    print(linea("Estilo",    prod.estilo))
    print(linea("Stock",     f"{prod.stock} pares"))
    print(linea("Talla",     prod.talla))
    print(linea("Precio",    f"${prod.precio}"))
    print(linea("Vendidos",  prod.vendidos))

    print(borde("╚", "═", "╝"))

# ──────────────────────────────
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    estilos        = ["Deportivo", "Formal", "Running", "Baloncesto", "Casual"]
    generos        = ["Masculino", "Femenino"]
    categoria_edad = ["Adulto", "Infantil"]

    
    nombre    = input("Nombre: ")
    categoria = get_option("Seleccione la categoría de edad:", categoria_edad)
    genero    = get_option("Seleccione el género:", generos)
    estilo    = get_option("Seleccione el estilo:", estilos)
    stock     = gi("Stock inicial: ", int, "Error: Stock inválido.", 0)
    talla     = gi("Talla: ", float, "Error: Talla inválida. Ingrese un número positivo.", 0)
    precio    = gi("Precio: $", float, "Error: Precio inválido.", 0.01)

    inventario_productos.append(Inventario(
        nombre, categoria, genero, estilo, stock, talla, precio
    ))

    print(f"\n✅ Producto '{nombre}' agregado con éxito.")

# ──────────────────────────────
def ver_productos():
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario_productos:
        print("No hay productos en el inventario aún.")
        return
    for i, p in enumerate(inventario_productos, start=1):
        mostrar_producto(p, i)
        print()

def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    if not inventario_productos:
        print("No hay productos para buscar.")
        return
    nombre_buscado = input("Nombre: ").strip().lower()
    producto_encontrado = next((p for p in inventario_productos
                                if p.nombre.lower() == nombre_buscado), None)
    if producto_encontrado:
        print("\n--- Producto Encontrado ---")
        mostrar_producto(producto_encontrado, 1)
    else:
        print(f"Producto '{nombre_buscado}' no encontrado.")

def realizar_venta():
    print("\n--- REALIZAR VENTA ---")
    if not inventario_productos:
        print("No hay productos para vender.")
        return
    nombre_venta = input("Nombre del producto a vender: ").strip().lower()
    cantidad_venta = gi("Cantidad a vender: ", int, "Error: Cantidad inválida.", 1)
    producto_venta = next((p for p in inventario_productos
                           if p.nombre.lower() == nombre_venta), None)

    if producto_venta:
        if producto_venta.stock >= cantidad_venta:
            producto_venta.stock -= cantidad_venta
            producto_venta.vendidos += cantidad_venta
            print(f"✅ Venta realizada: {cantidad_venta} pares de '{producto_venta.nombre}'. "
                  f"Nuevo stock: {producto_venta.stock}")
        else:
            print(f"❌ Stock insuficiente para '{producto_venta.nombre}'. Stock actual: {producto_venta.stock}")
    else:
        print(f"❌ Producto '{nombre_venta}' no encontrado.")

# ──────────────────────────────
def main():
    acciones_menu = {
        '1': agregar_producto,
        '2': ver_productos,
        '3': buscar_producto,
        '4': realizar_venta
    }
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Agregar nuevo producto")
        print("2. Ver productos en inventario")
        print("3. Buscar producto por nombre")
        print("4. Realizar venta")
        print("5. Editar Producto (pendiente)")
        print("6. Salir")
        print("------------------------------")
        opcion = input("Elige una opción: ").strip()
        if opcion == '6':
            print("\nSaliendo... ¡Hasta luego!")
            break
        acciones_menu.get(opcion,
            lambda: print("\n❌ Opción no válida. Elige un número del 1 al 6."))()
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
