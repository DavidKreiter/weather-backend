# Weather Backend Service

This service is the backend microservice for the Weather App final project.

It exposes a REST API that receives a city key, fetches live weather data from OpenWeatherMap, and returns a clean JSON response.

## Supported Cities

- new-york
- sydney
- cape-town
- bangkok

## API Endpoint

```http
GET /weather/<location_key>
