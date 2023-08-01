import requests

# Replace 'YOUR_API_KEY' with the provided API key
API_KEY = 'b6907d289e10d714a6e88b30761fae22'
BASE_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "list" in data:
        print(f"Weather forecast for {data['city']['name']}:")
        for forecast in data['list']:
            time = forecast['dt_txt']
            weather_description = forecast['weather'][0]['description']
            print(f"Time: {time}")
            print(f"Description: {weather_description}")
            print()
    else:
        print("Error: Failed to fetch weather data for the city.")

def get_wind_speed(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "list" in data:
        print(f"Wind Speed forecast for {data['city']['name']}:")
        for forecast in data['list']:
            time = forecast['dt_txt']
            wind_speed = forecast['wind']['speed']
            print(f"Time: {time}")
            print(f"Wind Speed: {wind_speed} m/s")
            print()
    else:
        print("Error: Failed to fetch wind speed data for the city.")

def get_pressure(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "list" in data:
        print(f"Pressure forecast for {data['city']['name']}:")
        for forecast in data['list']:
            time = forecast['dt_txt']
            pressure = forecast['main']['pressure']
            print(f"Time: {time}")
            print(f"Pressure: {pressure} hPa")
            print()
    else:
        print("Error: Failed to fetch pressure data for the city.")

def main():
    while True:
        print("1. Get weather forecast for a city")
        print("2. Get Wind Speed forecast for a city")
        print("3. Get Pressure forecast for a city")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter the name of the city: ")
            get_weather(city)
        elif choice == '2':
            city = input("Enter the name of the city: ")
            get_wind_speed(city)
        elif choice == '3':
            city = input("Enter the name of the city: ")
            get_pressure(city)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
