from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido"

@app.route("/cajas/", methods=['POST'])
def cajas():
    return "Este Metodo crea cajas"

@app.route("/cajas/", methods=['GET'])
def cajas():
    return "Este Metodo devuelve todas cajas"

@app.route("/cajas/<nombre>", methods=['GET'])
def cajas(nombre):
    return "Este Metodo devuelve la caja de " + nombre

@app.route("/cajas/<nombre>", methods=['UPDATE'])
def cajas(nombre):
    return "Este Metodo Actualiza el saldo de " + nombre

@app.route("/cajas/transferencia", methods=['DELETE'])
def transferencia():
    return "Este Metodo Transfiere entre 2 Cajas"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=9000)
