import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

def get_weather_data(city):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Data Fetched Successfully")
        return {
            "city": data["location"]["name"],
            "temperature": data["current"]["temperature"],
            "weather_description": data["current"]["weather_descriptions"][0],
            "wind_speed": data["current"]["wind_speed"],
            "wind_direction": data["current"]["wind_dir"],
            "humidity": data["current"]["humidity"],
            "pressure": data["current"]["pressure"],
        }
    else:
        print("Failed to fetch data")
        return None
    
def display_choices(weather_data):
    print("Pick one option:")
    print(f"1: Get weather in {weather_data['city']}")
    print(f"2: Get temperature in {weather_data['temperature']}°C")
    print(f"3: Get weather description: {weather_data['weather_description']}")
    print(f"4: Get wind speed: {weather_data['wind_speed']} km/h")
    print(f"5: Get wind direction: {weather_data['wind_direction']}")
    print(f"6: Get humidity: {weather_data['humidity']}%")
    print(f"7: Get pressure: {weather_data['pressure']} hPa")
    print("8: Get all data")
    print("9: Exit")
    
def handle_choices(choice, weather_data):
    if choice == 1:
        print(f"Weather in {weather_data['city']}:")
    elif choice == 2:
        print(f"Temperature: {weather_data['temperature']}°C")
    elif choice == 3:
        print(f"Weather Description: {weather_data['weather_description']}")
    elif choice == 4:
        print(f"Wind Speed: {weather_data['wind_speed']} km/h")
    elif choice == 5:
        print(f"Wind Direction: {weather_data['wind_direction']}")
    elif choice == 6:
        print(f"Humidity: {weather_data['humidity']}%")
    elif choice == 7:
        print(f"Pressure: {weather_data['pressure']} hPa")
    elif choice == 8:
        print(f"All data: {weather_data}")
    elif choice == 9:
        main()
        return False
    else:
        print("Invalid choice. Please enter a valid option.")
    return True

def main():
    user_input = input("Press Y to continue and N to exit: ").upper()
    if user_input == "Y":
        while True:
            city = input("Enter the city name: ")
            weather_data = get_weather_data(city)
            if weather_data:
                while True:
                    display_choices(weather_data)
                    try:
                        choice = int(input("Enter your choice: "))
                        if not handle_choices(choice, weather_data):
                            return
                    except ValueError:
                        print("Please enter a valid number.")
    elif user_input == "N":
        print("Thank you for using the weather app")
    else:
        print("Invalid input. Please enter Y or N.")
        main()

if __name__ == "__main__":
    main()
            
           
        
        