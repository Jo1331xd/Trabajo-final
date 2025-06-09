"""
Archivo principal para gestionar y mostrar inventario de tienda de zapatos.
Diseño minimalista y elegante para consola.
"""

from models.inventario import Inventario, ProductoZapato

def mostrar_encabezado():
    print()
    print("="*70)
    print("INVENTARIO DE TIENDA DE ZAPATOS".center(70))
    print("="*70)
    print()

def mostrar_producto(producto: ProductoZapato):
    print(f"ID: {producto.id_producto} | {producto.marca} - {producto.nombre}")
    print(f"Talla: {producto.talla} | Cantidad: {producto.cantidad} pares | Precio: ${producto.precio:.2f}")
    print("-"*70)

def main():
    inventario = Inventario()
    
    # Agregar productos de ejemplo
    inventario.agregar_producto(nombre="Air Runner", marca="Nike", talla=42, cantidad=10, precio=89.99)
    inventario.agregar_producto(nombre="Classic Leather", marca="Reebok", talla=40, cantidad=5, precio=75.50)
    inventario.agregar_producto(nombre="Suede Classic", marca="Puma", talla=41, cantidad=8, precio=65.00)

    mostrar_encabezado()
    productos = inventario.listar_productos()
    if not productos:
        print("No hay productos en inventario.")
    else:
        for producto in productos:
            mostrar_producto(producto)
    print()

if __name__ == "__main__":
    main()
