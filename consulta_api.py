import requests

url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx"

params = {
    "user": "danah.gonzalezm@duocuc.cl",
    "pass": "Arquitectura123",
    "function": "GetSeries",
    "timeseries": "F073.TCO.PRE.Z.D", # peso chileno a dolar
    "firstdate": "2024-10-03",
    "lastdate": "2024-10-09"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()  
    print(data) 
else:
    print(f"Error en la solicitud: {response.status_code}")
