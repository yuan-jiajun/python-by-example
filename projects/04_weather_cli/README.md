# 🌤️ Project 04: Real-time Weather CLI

## Difficulty: 🚀 Professional

## Description
Build a professional command-line weather application that fetches real-time weather
data from the Open-Meteo API (free, no API key needed!) and displays it beautifully
in the terminal. This project combines API consumption, decorators, type hinting,
error handling, and testing.

## Requirements

1. Fetch current weather data for any city using the Open-Meteo geocoding + weather API
2. Display temperature, humidity, wind speed, and weather condition
3. Support multiple cities in a single query
4. Cache API responses using a decorator to avoid repeated requests
5. Use type hints throughout the codebase
6. Handle network errors and invalid city names gracefully
7. Display weather data in a formatted, visually appealing way

## Concepts You'll Practice

- HTTP Requests (`urllib` — no external dependencies!)
- Decorators (caching)
- Type Hinting
- Error Handling (network, API, data)
- JSON parsing
- String formatting and CLI design

## Example Output

```
🌤️  WEATHER CLI
===============

Enter city name: Gaza

╔══════════════════════════════════════╗
║  📍 Gaza, Palestinian Territory     ║
╠══════════════════════════════════════╣
║  🌡️  Temperature:  28.3°C           ║
║  💧 Humidity:      65%              ║
║  💨 Wind Speed:    12.5 km/h        ║
║  ☀️  Condition:     Clear sky        ║
╚══════════════════════════════════════╝
```

## How to Run

```bash
cd projects/04_weather_cli
python solution.py
```

> **Note:** This project uses the free [Open-Meteo API](https://open-meteo.com/) —
> no API key or sign-up required!

## Bonus Challenges

- [ ] Add 5-day forecast display
- [ ] Add temperature unit conversion (°C / °F)
- [ ] Save favorite cities to a config file
