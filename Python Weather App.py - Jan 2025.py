def welcome_message():
    print("Welcome to the Weather Forecast Application! We will keep you up to day with the current weather to help you plan your day!\n")

def get_city():
    while True:
        city = input("Enter the city name for the weather forecast: ").strip()
        if city in weather_data:
            return city
        else:
            print("Sorry, we don't have weather data for that city. Please try again.")

def display_weather(city):
    data = weather_data[city]
    print(f"\nWeather Forecast for {city}:")
    print(f"Temperature: {data['temperature']}")
    print(f"Conditions: {data['conditions']}")
    print(f"Wind Speed: {data['wind_speed']}")
    print(f"Humidity: {data['humidity']}\n")

def thank_you_message():
    print("Thank you for using the Weather Forecast Application! Have a great day!")

weather_data = {
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"},
    "Berlin": {"temperature": "16°C", "conditions": "Sunny", "wind_speed": "4 km/h", "humidity": "75%"},
    "Dubai": {"temperature": "35°C", "conditions": "Hot", "wind_speed": "12 km/h", "humidity": "20%"},
    "Moscow": {"temperature": "10°C", "conditions": "Snowy", "wind_speed": "6 km/h", "humidity": "90%"},
    "Toronto": {"temperature": "14°C", "conditions": "Partly Cloudy", "wind_speed": "8 km/h", "humidity": "70%"},
    "Beijing": {"temperature": "19°C", "conditions": "Hazy", "wind_speed": "9 km/h", "humidity": "65%"},
    "Mumbai": {"temperature": "30°C", "conditions": "Humid", "wind_speed": "10 km/h", "humidity": "85%"},
    "Cape Town": {"temperature": "24°C", "conditions": "Clear", "wind_speed": "5 km/h", "humidity": "55%"},
    "Madrid": {"temperature": "25°C", "conditions": "Sunny", "wind_speed": "7 km/h", "humidity": "40%"},
    "Rome": {"temperature": "22°C", "conditions": "Partly Cloudy", "wind_speed": "6 km/h", "humidity": "50%"},
    "Amsterdam": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "10 km/h", "humidity": "85%"},
    "Vienna": {"temperature": "20°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "75%"},
    "Oslo": {"temperature": "10°C", "conditions": "Snowy", "wind_speed": "8 km/h", "humidity": "80%"},
    "Stockholm": {"temperature": "12°C", "conditions": "Windy", "wind_speed": "9 km/h", "humidity": "70%"}
}

def main():
    welcome_message()
    city = get_city()
    display_weather(city)
    thank_you_message()

if __name__ == "__main__":
    main()

# Weather Apps Open weather .com, meteomatics.com and developer.accuweather

