## ZipCode Weather App
## Author: Lane Dorscher
## Date: 11/23/2025
## Description:
##     A CLI program that accepts a U.S. ZIP code, validates it using regex,
##     and retrieves weather information using the OpenWeatherMap API.

##     Features:
##     - Input validation
##     - Loop with quit conditions
##     - External API request
##     - Clean error handling

import json, re, requests

QUIT_CRITERIA = ["Q", "QUIT", "EXIT", "E"]
WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
APP_ID = "906b6939735602a519447e37a839d229"

## ZIPCODE_LENGTH_REQUIREMENT = 5
ZIP_REGEX = r'^\d{5}$' ## r'^\d{5}(?:-\d{4})?$'
ACCEPTED_FORMATS = {
    "12345",
}

def get_user_input(prompt:str) -> str | None:
    '''
    Prompt the user for input

    Returns: User's input as str or None of user entered acceptable QUIT phrase
    '''
    user_input = input(prompt).strip()
    
    if (user_input.upper() in QUIT_CRITERIA):
        return None
    
    return user_input

def is_zipcode_valid(zipcode:str) -> bool:
    '''
    Validates a zipcode using regular expression
    
    Returns: True if valid, otherwise False
    '''
    temp = re.search(ZIP_REGEX, zipcode)
    return temp is not None

## Calls weather API parsing the given zipcode
def get_weather_data(zipcode) -> str | None:
    '''
        Calls weather API with the provided zipcode
        
        Returns: data in json formatting or None if error was caught
    '''

    url = f"{WEATHER_API}?zip={zipcode}&units=imperial&APPID={APP_ID}"
    try:
        response = requests.get(url)
        # response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"\nError retrieving weather data: {e}\n")
        return None
    
def display_weather_summary(data: dict) -> None:
    """
    Displays a readable weather summary:
    "It is a [condition] day in [city, country].
     Temperature: x
     Feels like: y
     Humidity: z%"
    """
    if not data:
        print("No weather data to display.")
        return

    main_data = data.get("main", {})
    weather_data = data.get("weather", [{}])[0]
    city = data.get("name", "Unknown")
    country = data.get("sys", {}).get("country", "")
    condition = weather_data.get("description", "N/A")
    temp = main_data.get("temp", "N/A")
    feels_like = main_data.get("feels_like", "N/A")
    humidity = main_data.get("humidity", "N/A")

    print(f"\nIt is a {condition} day in {city}, {country}.")
    print(f"Temperature: {temp}°F")
    print(f"Feels like: {feels_like}°F")
    print(f"Humidity: {humidity}%\n")


def main():
    '''Main function of the program'''
    
    print("Welcome to the ZIP Code Weather App!")
    print("Enter a 5-digit ZIP code to retrieve weather information.")

    while(True):

        zipcode = get_user_input(f"\nEnter ZIP code [Accepted example: {ACCEPTED_FORMATS}] (or 'Q' to exit): ")

        if (zipcode is None):
            print("Thank you for using the ZipCode Weather App!")
            break

        if (is_zipcode_valid(zipcode) == False):
            print(f"\nInvalid ZIP: \"{zipcode}\". Accepted format examples: {ACCEPTED_FORMATS}")
            continue

        raw_data = get_weather_data(zipcode)
        if raw_data:
            # print(json.dumps(raw_data, indent=4))
            display_weather_summary(raw_data)
        

    print("Goodbye!")

if __name__ == "__main__":
    main()