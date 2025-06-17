# Sistema de Gestión de Tienda de Zapatos

**Proyecto Final - Grupo 7**

## Descripción

Sistema completo de gestión para una tienda de zapatos desarrollado en Python. Permite registrar inventario, controlar ventas, generar reportes y mantener estadísticas detalladas del negocio.

## Funcionalidades Principales

### 🔧 Gestión de Inventario
- **Registrar Zapato**: Agregar nuevos modelos al catálogo
- **Mostrar Inventario**: Visualizar todo el stock disponible
- **Buscar Zapato**: Localizar productos por código o nombre
- **Editar Zapato**: Modificar información de productos existentes
- **Eliminar Zapato**: Remover productos del sistema

### 💰 Gestión de Ventas
- **Registrar Venta**: Procesar ventas y actualizar inventario automáticamente
- **Resumen de Ventas**: Visualizar histórico de transacciones
- **Estadísticas por Zapato**: Análisis detallado de rendimiento por producto

## Estructura del Proyecto

```
tienda_zapatos/
├── main.py                 # Archivo principal
├── models/                 # Modelos de datos
│   ├── __init__.py
│   ├── zapato.py          # Clase Zapato
│   └── venta.py           # Clase Venta
├── dao/                   # Data Access Objects
│   ├── __init__.py
│   ├── base_dao.py        # DAO base
│   ├── zapato_dao.py      # DAO para zapatos
│   └── venta_dao.py       # DAO para ventas
├── services/              # Lógica de negocio
│   ├── __init__.py
│   └── tienda_service.py  # Servicio principal
├── utils/                 # Utilidades
│   ├── __init__.py
│   └── menu_utils.py      # Funciones de menú y validación
├── data/                  # Archivos de datos
│   ├── zapatos.txt        # Base de datos de zapatos
│   └── ventas.txt         # Base de datos de ventas
└── README.md             # Este archivo
```

## Instalación y Uso

### Requisitos
- Python 3.6 o superior
- No requiere dependencias externas

### Instalación
1. Clona o descarga el proyecto
2. Navega al directorio del proyecto
3. Ejecuta el programa principal

### Ejecución
```bash
python main.py
```

## Características Técnicas

### Arquitectura Modular
- **Separación de responsabilidades**: Modelos, DAOs, Servicios y Utilidades
- **Patrón DAO**: Abstracción del acceso a datos
- **Manejo de archivos**: Persistencia en archivos de texto plano
- **Validación de datos**: Verificación de entrada del usuario
- **Manejo de errores**: Gestión robusta de excepciones

### Persistencia de Datos
- **Formato**: Archivos de texto con separadores de campo
- **Codificación**: UTF-8 para soporte de caracteres especiales
- **Ubicación**: Carpeta `data/` (se crea automáticamente)

### Validaciones Implementadas
- Códigos únicos para zapatos
- Precios y cantidades numéricas válidas
- Stock suficiente para ventas
- Confirmación para operaciones críticas

## Equipo de Desarrollo - Grupo 7

| Nombre | ID | Rol |
|--------|----|----|n| Luis Xavier Aburto | 19011934 | Analista de sistema |
| José Cristo Carvallo | 24014111 | Líder del proyecto |
| Ariadna Barboza | 24013695 | Ing. control de calidad |
| Julio Muñoz | 24013290 | Desarrollador (Programador) |

## Funcionalidades del Sistema

### 1. Menú de Opciones (MDP_001)
Interfaz principal que permite navegar entre todas las funcionalidades del sistema.

### 2. Registro de Zapatos (RZ_001)
Permite registrar zapatos con la siguiente información:
- Código único
- Nombre descriptivo
- Descripción detallada
- Talla
- Género (Hombre/Mujer/Unisex)
- Edad objetivo (Niño/Adulto)
- Estilo
- Precio
- Cantidad en inventario

### 3. Control de Inventario (MTC_001)
Mantiene el conteo automático de:
- Stock por modelo
- Valor total del inventario
- Número de productos diferentes

### 4. Registro de Ventas (RDV_001)
Procesa ventas con:
- Validación de stock disponible
- Cálculo automático de totales
- Actualización de inventario
- Registro de fecha y hora

### 5. Gestión de Datos (IDR_001)
Opciones para:
- Editar información de zapatos
- Eliminar productos
- Búsqueda por código o nombre

### 6. Reportes de Ventas (REDV_001)
Genera:
- Resumen general de ventas
- Estadísticas por producto
- Análisis de rendimiento
- Histórico de transacciones

## Guía de Uso

### Primera Ejecución
1. Ejecuta `python main.py`
2. El sistema creará automáticamente la carpeta `data/`
3. Aparecerá el menú principal

### Registrar un Zapato
1. Selecciona opción "1. Registrar Zapato"
2. Ingresa la información solicitada
3. El sistema validará los datos automáticamente

### Realizar una Venta
1. Selecciona opción "4. Registrar Venta"
2. Ingresa el código del zapato
3. Especifica la cantidad a vender
4. Confirma la transacción

### Ver Reportes
- Opción 2: Inventario completo
- Opción 7: Resumen de ventas
- Opción 8: Estadísticas detalladas

## Notas Técnicas

- Los archivos de datos se generan automáticamente
- El sistema maneja caracteres especiales (acentos, ñ)
- Todas las operaciones incluyen validación de datos
- El programa es robusto ante errores de entrada
- Se puede interrumpir safely con Ctrl+C

## Cronograma del Proyecto

| Funcionalidad | Responsable | Fecha Inicio | Fecha Fin |
|---------------|-------------|--------------|-----------|n| Menú de Opciones | Desarrollador | 03/06/25 | 07/06/25 |
| Registro de Zapatos | Analista de sistema | 07/06/25 | 11/06/25 |
| Control de Inventario | Líder | 11/06/25 | 15/06/25 |
| Registro de Ventas | Ing. control de calidad | 15/06/25 | 19/06/25 |
| Gestión de Datos | Analista de sistema | 19/06/25 | 23/06/25 |
| Reportes de Ventas | Ing. control de calidad | 23/06/25 | 27/06/25 |

---

**© 2025 - Grupo 7 - Proyecto Final**

