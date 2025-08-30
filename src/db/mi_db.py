import sqlite3
from src.modelo.caja import Caja

class MiDB:
    def __init__(self, db_path=":memory:"):
        self.path = db_path
        self._crear_tabla()

    def _crear_tabla(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cajas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dueño TEXT NOT NULL unique,
                    saldo INTEGER NOT NULL
                )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_caja INTEGER NOT NULL REFERENCES usuarios (id),
                monto INTEGER NOT NULL
                )
        """)
            conn.commit()

    def agregar_caja(self, caja):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
            "INSERT INTO cajas (dueño, saldo) VALUES (?, ?)",
            (caja.nombre, caja.saldo)
            )
            conn.commit()


    def obtener_caja(self, nombre):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cajas WHERE dueño = ?", (nombre,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return Caja(fila[1], fila[2], fila[0])

    def obtener_cajas(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cajas")
            filas = cursor.fetchall()
            return [Caja(f[1], f[2], f[0]) for f in filas]

    def actualizar_caja(self, caja):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE cajas SET saldo = ? WHERE id = ?",
                (caja.saldo, caja.id_usuario)
            )
            conn.commit()