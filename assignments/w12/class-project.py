# class-project.py
#
# usage:    Application to interact with a webservice in order to obtain data.
# 
# description:  Your program must prompt the user for their city or zip code and 
#               request weather forecast data from openweathermap.org.
#       
#               Your program must display the weather information in a
#               READABLE format to the user.
#
# Asks the user for their zip code or city.
# prompt to enter location
def get_loc():
    loc = ''
    print('Enter city, zip, or exit: ')
    loc = input()
    return loc

import requests
from requests.models import Response
from pprint import pprint

# Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
# Use the Requests library in order to request data from the webservice.
def validate_loc(loc):
    #PRINT input being validated
    print('You entered: ', loc, ' Validating...')
    try:
        API_key = "fd343d2f9dad702a422107612762b802"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
        # Determine whether user entered city or zip.
        if loc.strip().isdigit():
            API_loc_type = "&zip="
        else:
            API_loc_type = "&q="
        
        # Compose final url
        final_url = base_url + "appid=" + API_key + API_loc_type + loc + "&units=imperial"
        # Access and store weather data
        weather_data = requests.get(final_url).json()
        # Display the weather forecast in a readable format to the user.
        print("\nCurrent Weather Data:\n")
        # Access location
        name = weather_data['name']
        # Access temperature 
        temp = weather_data['main']['temp']
        # Access wind speed
        wind_speed = weather_data['wind']['speed']
        # Access description 
        description = weather_data['weather'][0]['description']
        # Access latitude
        latitude = weather_data['coord']['lat']
        # Access longitude
        longitude = weather_data['coord']['lon']
        
        # Printing Data
        print('\nLocation : ',name)
        print('\nTemperature (Fahrenheit): ',temp)
        print('\nWind Speed (Miles per Hour): ',wind_speed)
        print('\nSky Description : ',description)
        print('\nLatitude : ',latitude)
        print('\nLongitude : ',longitude)
    except:
        #PRINT fail error message
        print('Failure: Location match not found. Please enter information again.')
        # Send user back to input another function.
        loc = get_loc()
        # Check if user wants to exit.
        if loc == "exit":
            exit
        else:
            validate_loc(loc)
    return

# Run main function
# EXECUTE main function
# Allow the user to run the program multiple times.
run_again = 'yes'
while (run_again == 'yes') or (run_again == 'y'):
    loc = get_loc()
    validate_loc(loc)
    print('\nDo you want to check another location? (yes or no)')
    run_again = input()
    
    if (run_again == 'no'):
        print("Exiting program.")
        exit