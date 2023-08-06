import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key

    try:
        response = requests.get(complete_url)
        data = response.json()

        if response.status_code == 200:
            main_data = data["main"]
            temperature = main_data["temp"]
            temperature_celsius = temperature - 273.15
            print("Current temperature in {}: {:.2f}°C".format(city, temperature_celsius))
        else:
            print("Error: {}".format(data['message']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
    except KeyError as e:
        print("Error: Invalid response format from the API.")
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

if __name__ == "__main__":
    api_key = "8e65aa89c03d761b733c967bc94460ae"
    for i in range(5):
        city = input("Enter the name of city {}: ".format(i+1))
        get_weather(api_key, city)
