#  Weather Backend Service

This service is the backend microservice for the Weather App final project.

It exposes a REST API that receives a city key, fetches live weather data from OpenWeatherMap, and returns a clean JSON response.

---

##  Supported Cities

- new-york
- sydney
- cape-town
- bangkok

---

##  API Endpoint

GET /weather/<location_key>

### Example

GET /weather/new-york

---

##  Response Example

{
  "city": "New York",
  "temperature": 11.41,
  "description": "overcast clouds",
  "humidity": 70,
  "wind_speed": 2.57
}

---

##  Environment Variables

This service requires an OpenWeatherMap API key.

| Variable | Description |
|----------|------------|
| API_KEY  | OpenWeatherMap API key |

---

##  Run Locally

Install dependencies:

pip install -r requirements.txt

Set API key (PowerShell):

$env:API_KEY="your_api_key_here"

Run the app:

python app.py

Open in browser:

http://localhost:5000/weather/new-york

---

##  Curl Example

curl http://localhost:5000/weather/new-york

---

##  Run with Docker

Build the image:

docker build -t weather-backend .

Run the container:

docker run -p 5000:5000 -e API_KEY="your_api_key_here" weather-backend

Test in browser:

http://localhost:5000/weather/new-york

---

## Notes

- The API key is not stored in the code or in the repository.
- It must be provided as an environment variable when running the service.
