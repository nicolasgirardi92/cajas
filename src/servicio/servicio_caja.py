from src.db.mi_db import MiDB
from src.modelo.caja import Caja

class ServicioCaja:
    def __init__(self):
        self.db = MiDB("mi_base.db")

    def crear_caja(self, nombre, saldo_inicial):
        caja = Caja(nombre, saldo_inicial)
        self.db.agregar_caja(caja)

    def buscar_caja(self, nombre):
        return self.db.obtener_caja(nombre)