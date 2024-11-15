import requests

# API Key is now configured
API_KEY = "6a7b7a9da58891b56d99829a2c9e6b8d"

def get_weather(city):
    try:
        # Create URL with your API key
        base_url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius
        }
        
        # Get weather data
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nWeather in {city}:")
            print(f"Temperature: {round(data['main']['temp'])}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
            print(f"Feels like: {round(data['main']['feels_like'])}°C")
        elif response.status_code == 401:
            print("Error: Invalid API key! Please check your API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found! Please check the city name.")
        else:
            print(f"Error: Could not get weather data for {city}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Weather App!")
    print("You can check weather for any city in the world.")
    
    while True:
        print("\n=== Weather App ===")
        print("1. Check weather")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            city = input("Enter city name: ").strip()
            if city:
                get_weather(city)
            else:
                print("Please enter a valid city name!")
        elif choice == "2":
            print("\nThank you for using the Weather App!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()