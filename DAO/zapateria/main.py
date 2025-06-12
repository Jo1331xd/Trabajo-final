from AD_zapateria.zapato import Zapato
from registro.zapato_dao import ZapatoDAO

dao = ZapatoDAO()

# Insertar un zapato nuevo
zapato_nuevo = Zapato(marca="Nike", talla=42, precio=85.50, stock=10)
dao.insertar(zapato_nuevo)

# Mostrar todos los zapatos
print("Lista de zapatos:")
for z in dao.obtener_todos():
    print(f"{z.id} - {z.marca} - Talla {z.talla} - ${z.precio} - Stock: {z.stock}")

# Buscar por ID
zapato = dao.obtener_por_id(1)
if zapato:
    print("\nZapato encontrado:", zapato.marca)

# Actualizar
zapato.precio = 79.99
dao.actualizar(zapato)

# Eliminar (descomenta si querés borrar)
# dao.eliminar(1)
