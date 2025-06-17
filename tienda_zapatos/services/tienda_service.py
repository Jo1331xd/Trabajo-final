"""
Servicio principal para la gestión de la tienda de zapatos
"""

from dao.zapato_dao import ZapatoDAO
from dao.venta_dao import VentaDAO
from models.zapato import Zapato
from models.venta import Venta
from utils.menu_utils import *

class TiendaService:
    def __init__(self):
        self.zapato_dao = ZapatoDAO()
        self.venta_dao = VentaDAO()
    
    def registrar_zapato(self):
        """Registra un nuevo zapato en el sistema con validaciones mejoradas"""
        mostrar_titulo_bonito("REGISTRAR NUEVO ZAPATO", "📦")
        
        try:
            # Código del zapato
            print("\n🏷️  Ingrese el código del zapato:")
            codigo = input("➤ Código: ").strip().upper()
            if not codigo:
                print("❌ Error: El código no puede estar vacío.")
                return False
            
            # Verificar si ya existe
            if self.zapato_dao.buscar_por_codigo(codigo):
                print(f"❌ Error: Ya existe un zapato con el código '{codigo}'.")
                return False
            
            # Información básica
            print("\n📝 Información básica:")
            nombre = input("➤ Nombre del zapato: ").strip()
            if not nombre:
                print("❌ Error: El nombre no puede estar vacío.")
                return False
                
            descripcion = input("➤ Descripción: ").strip()
            if not descripcion:
                descripcion = f"Zapato {nombre}"
            
            # Validar talla
            while True:
                talla_str = input("\n👟 Talla del zapato: ")
                talla = validar_talla(talla_str)
                if talla > 0:
                    break
                print("❌ Error: Ingrese una talla válida (número positivo).")
            
            # Seleccionar género
            genero = validar_genero()
            
            # Seleccionar edad
            edad = validar_edad()
            
            # Seleccionar estilo
            estilo = validar_estilo()
            
            # Validar precio
            while True:
                print("\n💰 Precio del zapato:")
                precio_str = input("➤ Precio: $")
                precio = validar_precio(precio_str)
                if precio >= 0:
                    break
                print("❌ Error: Ingrese un precio válido (número positivo).")
            
            # Validar cantidad
            while True:
                print("\n📊 Cantidad inicial en inventario:")
                cantidad_str = input("➤ Cantidad: ")
                cantidad = validar_cantidad(cantidad_str)
                if cantidad >= 0:
                    break
                print("❌ Error: Ingrese una cantidad válida (número entero positivo).")
            
            # Mostrar resumen
            print("\n" + "═"*50)
            print("📋 RESUMEN DEL NUEVO ZAPATO:")
            print("═"*50)
            print(f"🏷️  Código: {codigo}")
            print(f"📝 Nombre: {nombre}")
            print(f"📄 Descripción: {descripcion}")
            print(f"👟 Talla: {talla}")
            print(f"👤 Género: {genero}")
            print(f"👶 Edad: {edad}")
            print(f"🎯 Estilo: {estilo}")
            print(f"💰 Precio: ${precio:.2f}")
            print(f"📊 Cantidad: {cantidad}")
            print("═"*50)
            
            if not confirmar_accion("\n¿Desea guardar este zapato?"):
                print("❌ Registro cancelado.")
                return False
            
            # Crear y guardar zapato
            zapato = Zapato(codigo, nombre, descripcion, str(talla), genero, edad, estilo, precio, cantidad)
            
            if self.zapato_dao.guardar_zapato(zapato):
                print(f"\n✅ ¡Zapato '{nombre}' registrado exitosamente!")
                return True
            else:
                print("\n❌ Error al guardar el zapato.")
                return False
                
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            return False
    
    def mostrar_inventario(self):
        """Muestra todo el inventario de zapatos con diseño mejorado"""
        mostrar_titulo_bonito("INVENTARIO DE ZAPATOS", "📋")
        
        zapatos = self.zapato_dao.obtener_todos()
        
        if not zapatos:
            print("\n📦 No hay zapatos registrados en el inventario.")
            return
        
        # Calcular estadísticas
        stock_total = sum(zapato.cantidad for zapato in zapatos)
        valor_total = sum(zapato.cantidad * zapato.precio for zapato in zapatos)
        
        # Mostrar estadísticas generales
        print(f"\n📊 ESTADÍSTICAS GENERALES:")
        print(f"│")
        print(f"├─ Total de modelos: {len(zapatos)}")
        print(f"├─ Stock total: {stock_total} pares")
        print(f"└─ Valor total inventario: ${valor_total:.2f}")
        
        print(f"\n{formatear_tabla_zapatos(zapatos)}")
    
    def buscar_zapato(self):
        """Busca zapatos por código o nombre con diseño mejorado"""
        mostrar_titulo_bonito("BUSCAR ZAPATO", "🔍")
        
        print("\n🎯 Seleccione el tipo de búsqueda:")
        print("│")
        print("├─ 1. Buscar por código")
        print("└─ 2. Buscar por nombre")
        
        while True:
            opcion = input("\n➤ Seleccione opción (1-2): ")
            if opcion in ['1', '2']:
                break
            print("❌ Opción inválida.")
        
        if opcion == '1':
            codigo = input("\n🏷️ Ingrese el código: ").strip().upper()
            zapato = self.zapato_dao.buscar_por_codigo(codigo)
            
            if zapato:
                print("\n✅ Zapato encontrado:")
                print(f"┌{'─' * 60}┐")
                print(f"│ {zapato} │")
                print(f"└{'─' * 60}┘")
            else:
                print(f"\n❌ No se encontró ningún zapato con el código '{codigo}'.")
        
        else:  # opcion == '2'
            nombre = input("\n📝 Ingrese el nombre (o parte del nombre): ").strip()
            zapatos = self.zapato_dao.buscar_por_nombre(nombre)
            
            if zapatos:
                print(f"\n✅ Se encontraron {len(zapatos)} zapato(s):")
                print(formatear_tabla_zapatos(zapatos))
            else:
                print(f"\n❌ No se encontraron zapatos con el nombre '{nombre}'.")
    
    def registrar_venta(self):
        """Registra una nueva venta"""
        mostrar_titulo("REGISTRAR VENTA")
        
        try:
            codigo = input("Código del zapato vendido: ").strip()
            zapato = self.zapato_dao.buscar_por_codigo(codigo)
            
            if not zapato:
                print("Error: No se encontró un zapato con ese código.")
                return False
            
            print(f"Zapato encontrado: {zapato.nombre}")
            print(f"Stock disponible: {zapato.cantidad}")
            print(f"Precio: ${zapato.precio:.2f}")
            
            # Validar cantidad vendida
            while True:
                cantidad_str = input("Cantidad a vender: ")
                cantidad = validar_cantidad(cantidad_str)
                
                if cantidad < 0:
                    print("Error: Ingrese una cantidad válida.")
                    continue
                    
                if cantidad > zapato.cantidad:
                    print(f"Error: No hay suficiente stock. Disponible: {zapato.cantidad}")
                    continue
                    
                if cantidad == 0:
                    print("No se registrará ninguna venta.")
                    return False
                    
                break
            
            # Calcular total
            total = cantidad * zapato.precio
            print(f"Total de la venta: ${total:.2f}")
            
            if not confirmar_accion("¿Confirmar venta?"):
                print("Venta cancelada.")
                return False
            
            # Crear venta
            venta = Venta(zapato.codigo, zapato.nombre, cantidad, zapato.precio)
            
            # Guardar venta y actualizar stock
            if self.venta_dao.guardar_venta(venta):
                nuevo_stock = zapato.cantidad - cantidad
                if self.zapato_dao.actualizar_stock(zapato.codigo, nuevo_stock):
                    print("✓ Venta registrada exitosamente!")
                    print(f"Stock actualizado: {nuevo_stock} unidades")
                    return True
                else:
                    print("✗ Error al actualizar el stock.")
                    return False
            else:
                print("✗ Error al registrar la venta.")
                return False
                
        except Exception as e:
            print(f"Error inesperado: {e}")
            return False
    
    def editar_zapato(self):
        """Edita un zapato existente"""
        mostrar_titulo("EDITAR ZAPATO")
        
        codigo = input("Código del zapato a editar: ").strip()
        zapato = self.zapato_dao.buscar_por_codigo(codigo)
        
        if not zapato:
            print("Error: No se encontró un zapato con ese código.")
            return False
        
        print("Datos actuales:")
        print(zapato)
        print("\\nIngrese los nuevos datos (presione Enter para mantener el valor actual):")
        
        # Editar campos
        nombre = input(f"Nombre [{zapato.nombre}]: ").strip()
        if not nombre:
            nombre = zapato.nombre
        
        descripcion = input(f"Descripción [{zapato.descripcion}]: ").strip()
        if not descripcion:
            descripcion = zapato.descripcion
        
        talla = input(f"Talla [{zapato.talla}]: ").strip()
        if not talla:
            talla = zapato.talla
        
        genero = input(f"Género [{zapato.genero}]: ").strip()
        if not genero:
            genero = zapato.genero
        
        edad = input(f"Edad [{zapato.edad}]: ").strip()
        if not edad:
            edad = zapato.edad
        
        estilo = input(f"Estilo [{zapato.estilo}]: ").strip()
        if not estilo:
            estilo = zapato.estilo
        
        # Precio
        precio_str = input(f"Precio [{zapato.precio}]: ").strip()
        if precio_str:
            precio = validar_precio(precio_str)
            if precio < 0:
                print("Precio inválido, se mantiene el actual.")
                precio = zapato.precio
        else:
            precio = zapato.precio
        
        # Cantidad
        cantidad_str = input(f"Cantidad [{zapato.cantidad}]: ").strip()
        if cantidad_str:
            cantidad = validar_cantidad(cantidad_str)
            if cantidad < 0:
                print("Cantidad inválida, se mantiene la actual.")
                cantidad = zapato.cantidad
        else:
            cantidad = zapato.cantidad
        
        # Confirmar cambios
        zapato_actualizado = Zapato(codigo, nombre, descripcion, talla, genero, edad, estilo, precio, cantidad)
        
        print("\\nDatos actualizados:")
        print(zapato_actualizado)
        
        if confirmar_accion("¿Guardar cambios?"):
            if self.zapato_dao.actualizar_zapato(codigo, zapato_actualizado):
                print("✓ Zapato actualizado exitosamente!")
                return True
            else:
                print("✗ Error al actualizar el zapato.")
                return False
        else:
            print("Cambios cancelados.")
            return False
    
    def eliminar_zapato(self):
        """Elimina un zapato del sistema"""
        mostrar_titulo("ELIMINAR ZAPATO")
        
        codigo = input("Código del zapato a eliminar: ").strip()
        zapato = self.zapato_dao.buscar_por_codigo(codigo)
        
        if not zapato:
            print("Error: No se encontró un zapato con ese código.")
            return False
        
        print("Zapato a eliminar:")
        print(zapato)
        
        if confirmar_accion("¿Está seguro de eliminar este zapato?"):
            if self.zapato_dao.eliminar_zapato(codigo):
                print("✓ Zapato eliminado exitosamente!")
                return True
            else:
                print("✗ Error al eliminar el zapato.")
                return False
        else:
            print("Eliminación cancelada.")
            return False
    
    def mostrar_resumen_ventas(self):
        """Muestra un resumen de todas las ventas"""
        mostrar_titulo("RESUMEN DE VENTAS")
        
        ventas = self.venta_dao.obtener_todas()
        
        if not ventas:
            print("No hay ventas registradas.")
            return
        
        print(f"Total de ventas realizadas: {len(ventas)}")
        
        total_ingresos = self.venta_dao.calcular_total_ventas()
        print(f"Ingresos totales: ${total_ingresos:.2f}")
        
        print("\\nÚltimas 10 ventas:")
        print("-" * 80)
        
        for venta in ventas[-10:]:
            print(f"{venta.fecha} | {venta.nombre_zapato} | Cant: {venta.cantidad} | Total: ${venta.total:.2f}")
    
    def mostrar_estadisticas_por_zapato(self):
        """Muestra estadísticas detalladas por zapato"""
        mostrar_titulo("ESTADÍSTICAS POR ZAPATO")
        
        estadisticas = self.venta_dao.obtener_estadisticas_por_zapato()
        
        if not estadisticas:
            print("No hay estadísticas disponibles (no hay ventas registradas).")
            return
        
        print(f"{'Código':<10} {'Nombre':<20} {'Vendidos':<10} {'Ingresos':<12} {'Ventas':<8}")
        print("-" * 70)
        
        total_vendidos = 0
        total_ingresos = 0.0
        
        for codigo, stats in estadisticas.items():
            nombre = stats['nombre'][:19]  # Truncar si es muy largo
            vendidos = stats['cantidad_vendida']
            ingresos = stats['total_ingresos']
            num_ventas = stats['numero_ventas']
            
            print(f"{codigo:<10} {nombre:<20} {vendidos:<10} ${ingresos:<11.2f} {num_ventas:<8}")
            
            total_vendidos += vendidos
            total_ingresos += ingresos
        
        print("-" * 70)
        print(f"{'TOTALES':<31} {total_vendidos:<10} ${total_ingresos:<11.2f}")

