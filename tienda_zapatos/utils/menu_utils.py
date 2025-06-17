"""
Utilidades para menús y validaciones
"""

def mostrar_menu_principal():
    """Muestra el menú principal del sistema con diseño mejorado"""
    print("\n" + "╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║"+"👟 SISTEMA DE GESTIÓN - TIENDA DE ZAPATOS  👟".center(56)+"║")
    print("║" + " "*58 + "║")
    print("╠" + "═"*58 + "╣")
    print("║" + " "*58 + "║")
    print("║  📦 1. Registrar Zapato" + " "*32 + "  ║")
    print("║  📋 2. Mostrar Inventario" + " "*30 + "  ║")
    print("║  🔍 3. Buscar Zapato" + " "*35 + "  ║")
    print("║  💰 4. Registrar Venta" + " "*33 + "  ║")
    print("║  ✏️  5. Editar Zapato" + " "*34 + "   ║")
    print("║  🗑️  6. Eliminar Zapato" + " "*31 + "    ║")
    print("║  📊 7. Resumen de Ventas" + " "*31 + "  ║")
    print("║  📈 8. Estadísticas por Zapato" + " "*26 +  " ║")
    print("║" + " "*58 + "║")
    print("║  🚪 0. Salir del Sistema" + " "*31 + "  ║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

def validar_opcion_menu(opcion, rango_max):
    """
    Valida que la opción del menú sea válida
    
    Args:
        opcion (str): Opción ingresada por el usuario
        rango_max (int): Número máximo de opciones válidas
        
    Returns:
        int: Opción válida o -1 si es inválida
    """
    try:
        opcion_int = int(opcion)
        if 0 <= opcion_int <= rango_max:
            return opcion_int
        else:
            return -1
    except ValueError:
        return -1

def validar_precio(precio_str):
    """
    Valida que el precio sea un número válido
    
    Args:
        precio_str (str): Precio como string
        
    Returns:
        float: Precio válido o -1 si es inválido
    """
    try:
        precio = float(precio_str)
        if precio >= 0:
            return precio
        else:
            return -1
    except ValueError:
        return -1

def validar_cantidad(cantidad_str):
    """
    Valida que la cantidad sea un número entero válido
    
    Args:
        cantidad_str (str): Cantidad como string
        
    Returns:
        int: Cantidad válida o -1 si es inválida
    """
    try:
        cantidad = int(cantidad_str)
        if cantidad >= 0:
            return cantidad
        else:
            return -1
    except ValueError:
        return -1

def confirmar_accion(mensaje):
    """
    Pide confirmación al usuario para una acción
    
    Args:
        mensaje (str): Mensaje de confirmación
        
    Returns:
        bool: True si confirma, False en caso contrario
    """
    respuesta = input(f"{mensaje} (s/n): ").lower().strip()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")

def mostrar_titulo(titulo):
    """
    Muestra un título formateado
    
    Args:
        titulo (str): Título a mostrar
    """
    print(f"\n{'-'*len(titulo)}")
    print(titulo)
    print(f"{'-'*len(titulo)}")

def formatear_tabla_zapatos(zapatos):
    """
    Formatea una lista de zapatos en formato tabla
    
    Args:
        zapatos (list): Lista de objetos Zapato
        
    Returns:
        str: Tabla formateada
    """
    if not zapatos:
        return "No hay zapatos para mostrar."
    
    # Encabezados
    linea = f"{'Código':<10} {'Nombre':<20} {'Talla':<8} {'Género':<10} {'Precio':<10} {'Stock':<8}"
    linea += "\n" + "-" * 76
    
    # Datos
    for zapato in zapatos:
        linea += f"\n{zapato.codigo:<10} {zapato.nombre[:19]:<20} {zapato.talla:<8} {zapato.genero:<10} ${zapato.precio:<9.2f} {zapato.cantidad:<8}"
    
    return linea

def validar_talla(talla_str):
    """
    Valida que la talla sea un número positivo (entero o decimal)
    
    Args:
        talla_str (str): Talla como string
        
    Returns:
        float: Talla válida o -1 si es inválida
    """
    try:
        talla = float(talla_str)
        if talla > 0:
            return talla
        else:
            return -1
    except ValueError:
        return -1

def validar_genero():
    """
    Permite al usuario seleccionar el género con validación
    
    Returns:
        str: Género válido ('Hombre' o 'Mujer')
    """
    opciones_genero = {
        '1': 'Hombre',
        '2': 'Mujer'
    }
    
    while True:
        print("\n👤 Seleccione el género:")
        print("│")
        print("├─ 1. Hombre")
        print("└─ 2. Mujer")
        
        opcion = input("\n➤ Ingrese su opción (1-2): ").strip()
        
        if opcion in opciones_genero:
            return opciones_genero[opcion]
        
        print("❌ Error: Opción inválida. Seleccione 1 o 2.")

def validar_edad():
    """
    Permite al usuario seleccionar la edad con validación
    
    Returns:
        str: Edad válida ('Adulto' o 'Infantil')
    """
    opciones_edad = {
        '1': 'Adulto',
        '2': 'Infantil'
    }
    
    while True:
        print("\n👶 Seleccione la categoría de edad:")
        print("│")
        print("├─ 1. Adulto")
        print("└─ 2. Infantil")
        
        opcion = input("\n➤ Ingrese su opción (1-2): ").strip()
        
        if opcion in opciones_edad:
            return opciones_edad[opcion]
        
        print("❌ Error: Opción inválida. Seleccione 1 o 2.")

def validar_estilo():
    """
    Permite al usuario seleccionar el estilo con validación
    
    Returns:
        str: Estilo válido
    """
    opciones_estilo = {
        '1': 'Deportivo',
        '2': 'Basketball',
        '3': 'Football',
        '4': 'Running',
        '5': 'Formal',
        '6': 'Casual',
        '7': 'Botas',
        '8': 'Sandalias'
    }
    
    while True:
        print("\n👟 Seleccione el estilo del zapato:")
        print("│")
        print("├─ 1. Deportivo")
        print("├─ 2. Basketball")
        print("├─ 3. Football")
        print("├─ 4. Running")
        print("├─ 5. Formal")
        print("├─ 6. Casual")
        print("├─ 7. Botas")
        print("└─ 8. Sandalias")
        
        opcion = input("\n➤ Ingrese su opción (1-8): ").strip()
        
        if opcion in opciones_estilo:
            return opciones_estilo[opcion]
        
        print("❌ Error: Opción inválida. Seleccione un número del 1 al 8.")

def mostrar_titulo_bonito(titulo, emoji="📋"):
    """
    Muestra un título con diseño mejorado
    
    Args:
        titulo (str): Título a mostrar
        emoji (str): Emoji para decorar
    """
    ancho = len(titulo) + 4
    print(f"\n┌{'─' * ancho}┐")
    print(f"│ {emoji} {titulo} │")
    print(f"└{'─' * ancho}┘")

