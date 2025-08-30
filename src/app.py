from flask import Flask, request, jsonify
from src.servicio.servicio_caja import ServicioCaja

app = Flask(__name__)

servicio = ServicioCaja()
@app.route("/")
def home():
    return "Bienvenido"

@app.route("/cajas/", methods=['POST'])
def crear_caja():
    data = request.get_json()
    nombre = data['nombre']
    saldo = data['saldo']
    servicio.crear_caja(nombre, saldo)
    return jsonify({"mensaje": f"Caja de '{nombre}' creada con saldo {saldo}"}), 201

@app.route("/cajas/", methods=['GET'])
def obtener_cajas():
    cajas = servicio.buscar_cajas()
    return  jsonify(cajas), 200

@app.route("/cajas/<nombre>", methods=['GET'])
def obtener_caja(nombre):
    caja = servicio.buscar_caja(nombre)
    return jsonify(caja), 200

@app.route("/cajas/<nombre>", methods=['UPDATE'])
def actualizar_saldo(nombre):
    return "Este Metodo Actualiza el saldo de " + nombre

@app.route("/cajas/transferencia", methods=['DELETE'])
def transferencia():
    return "Este Metodo Transfiere entre 2 Cajas"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=9000)
