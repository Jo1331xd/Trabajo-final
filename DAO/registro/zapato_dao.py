import sqlite3
from AD_zapateria.zapato import Zapato

class ZapatoDAO:
    def __init__(self, db_name="zapateria.db"):
        self.conn = sqlite3.connect(db_name)
        self.crear_tabla()

    def crear_tabla(self):
        sql = """
        CREATE TABLE IF NOT EXISTS zapatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            talla INTEGER NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
        """
        self.conn.execute(sql)
        self.conn.commit()

    def insertar(self, zapato):
        sql = "INSERT INTO zapatos (marca, talla, precio, stock) VALUES (?, ?, ?, ?)"
        self.conn.execute(sql, (zapato.marca, zapato.talla, zapato.precio, zapato.stock))
        self.conn.commit()

    def obtener_todos(self):
        cursor = self.conn.execute("SELECT * FROM zapatos")
        return [Zapato(id=row[0], marca=row[1], talla=row[2], precio=row[3], stock=row[4]) for row in cursor]

    def obtener_por_id(self, zapato_id):
        cursor = self.conn.execute("SELECT * FROM zapatos WHERE id = ?", (zapato_id,))
        fila = cursor.fetchone()
        if fila:
            return Zapato(id=fila[0], marca=fila[1], talla=fila[2], precio=fila[3], stock=fila[4])
        return None

    def actualizar(self, zapato):
        sql = "UPDATE zapatos SET marca = ?, talla = ?, precio = ?, stock = ? WHERE id = ?"
        self.conn.execute(sql, (zapato.marca, zapato.talla, zapato.precio, zapato.stock, zapato.id))
        self.conn.commit()

    def eliminar(self, zapato_id):
        self.conn.execute("DELETE FROM zapatos WHERE id = ?", (zapato_id,))
        self.conn.commit()

