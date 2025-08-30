import requests

url = "http://127.0.0.1:9000/cajas/"
data = {"nombre": "Nico", "saldo": 1000}
r = requests.post(url, json=data)

print(r.status_code)
print(r.json())
