from flask import Flask, jsonify
import requests
import os

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)


cities = {
    "new-york": "New York",
    "sydney": "Sydney",
    "cape-town": "Cape Town",
    "bangkok": "Bangkok"
}

@app.route('/weather/<city>')
def get_weather(city):
    if city not in cities:
        return jsonify({"error": "City not found"}), 404

    city_name = cities[city]

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    print(data)

    if response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch weather data",
            "details": data
        }), response.status_code

    result = {
        "city": city_name,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)