"""
Sistema de Gestión de Tienda de Zapatos
Proyecto Final - Grupo 7

Archivo principal del sistema
"""

from services.tienda_service import TiendaService
from utils.menu_utils import *
import sys

def main():
    """Función principal del sistema"""
    # Crear instancia del servicio
    tienda = TiendaService()
    
    # Mensaje de bienvenida
    limpiar_pantalla()
    print("¡Bienvenido al Sistema de Gestión de Tienda de Zapatos!")
    print("Proyecto Final - Grupo 7")
    pausar()
    
    # Bucle principal del menú
    while True:
        try:
            limpiar_pantalla()
            mostrar_menu_principal()
            
            opcion = input("Seleccione una opción (0-8): ").strip()
            opcion_valida = validar_opcion_menu(opcion, 8)
            
            if opcion_valida == -1:
                print("Error: Opción inválida. Ingrese un número del 0 al 8.")
                pausar()
                continue
            
            # Procesar la opción seleccionada
            if opcion_valida == 0:
                # Salir del sistema
                limpiar_pantalla()
                print("¡Gracias por usar el Sistema de Gestión de Tienda de Zapatos!")
                print("Proyecto Final - Grupo 7")
                print("¡Hasta luego!")
                sys.exit(0)
            
            elif opcion_valida == 1:
                # Registrar zapato
                tienda.registrar_zapato()
                pausar()
            
            elif opcion_valida == 2:
                # Mostrar inventario
                tienda.mostrar_inventario()
                pausar()
            
            elif opcion_valida == 3:
                # Buscar zapato
                tienda.buscar_zapato()
                pausar()
            
            elif opcion_valida == 4:
                # Registrar venta
                tienda.registrar_venta()
                pausar()
            
            elif opcion_valida == 5:
                # Editar zapato
                tienda.editar_zapato()
                pausar()
            
            elif opcion_valida == 6:
                # Eliminar zapato
                tienda.eliminar_zapato()
                pausar()
            
            elif opcion_valida == 7:
                # Resumen de ventas
                tienda.mostrar_resumen_ventas()
                pausar()
            
            elif opcion_valida == 8:
                # Estadísticas por zapato
                tienda.mostrar_estadisticas_por_zapato()
                pausar()
        
        except KeyboardInterrupt:
            # Manejar Ctrl+C
            print("\n\nSaliendo del sistema...")
            sys.exit(0)
        
        except Exception as e:
            # Manejar errores inesperados
            print(f"\nError inesperado: {e}")
            print("El sistema continuará funcionando...")
            pausar()

if __name__ == "__main__":
    main()

