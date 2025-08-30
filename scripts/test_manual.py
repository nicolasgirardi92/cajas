import requests

url = "http://127.0.0.1:9000/cajas/Nico"
data = {"saldo": 1000}
r = requests.put(url, json=data)

print(r.status_code)
print(r.json())
