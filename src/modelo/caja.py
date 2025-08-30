class Caja:
    def __init__(self, nombre, saldo_inicial, id_usuario=None):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.id_usuario = id_usuario

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "saldo": self.saldo
        }