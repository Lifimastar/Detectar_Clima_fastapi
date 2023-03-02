from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/clima/{ciudad}")
async def clima(ciudad: str):
    """
    reemplaza "YOUR_API_KEY" por tu api key de la pagina openweather.org al registrarte.
    """
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=YOUR_API_KEY")
    if response.status_code == 200:
        data = response.json()
        clima = {
            "ciudad": ciudad,
            "temperatura": round(data["main"]["temp"] - 273.15, 1),
            "descripcion": data["weather"][0]["description"].capitalize(),
            "icono": data["weather"][0]["icon"]
        }
        return clima
    else:
        return {"error": "Ciudad no encontrada"}




