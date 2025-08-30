from src.db.mi_db import MiDB
from src.modelo.caja import Caja

class ServicioCaja:
    def __init__(self):
        self.db = MiDB("mi_base.db")

    def crear_caja(self, nombre, saldo_inicial):
        caja = Caja(nombre, saldo_inicial)
        self.db.agregar_caja(caja)

    def buscar_caja(self, nombre):
        return self.db.obtener_caja(nombre).to_dict()

    def buscar_cajas(self):
        cajas = self.db.obtener_cajas()
        return [caja.to_dict() for caja in cajas]

    def actualizar_saldo(self, nombre, monto):
        caja = self.db.obtener_caja(nombre)
        caja.actualizar_saldo(monto)
        self.db.actualizar_caja(caja)