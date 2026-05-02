import requests
# Consulta el clima usando una API abierta
url = "https://open-meteo.com"
try:
    respuesta = requests.get(url)
    temp = respuesta.json()['current_weather']['temperature']
    print(f"--- ACTIVIDAD PYTHON: API ---")
    print(f"Temperatura detectada: {temp}°C")
except:
    print("Instala 'requests' con: pip install requests")
