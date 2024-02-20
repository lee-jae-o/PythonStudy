import urllib.request
import json

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        with urllib.request.urlopen(base_url) as response:
            data = json.load(response)

        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    except Exception as e:
        print(f"Failed to fetch weather information. Error: {e}")

def main():
    city = input("Enter the city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()