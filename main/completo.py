from models.producto import Inventario

def main():
    # Crear un ejemplo de producto
    zapato = Inventario("Zapato Deportivo", 59.99, 20, 42, "Masculino", "Adulto", "Deportivo")
    
    # Mostrar la información del producto
    print(zapato)

if __name__ == "__main__":
    main()

