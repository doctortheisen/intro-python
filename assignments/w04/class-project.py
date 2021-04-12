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
# requirements: 

# Run main function
EXECUTE main function 
# Create a Python Application which asks the user for their zip code or city.
PRINT prompt to enter location
INPUT (location OR city OR exit)

PRINT input being validated
    TRY input
        PRINT success location match found
        EXCEPT
            PRINT fail location match not found & RETURN to INPUT 
# Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
# Use the Requests library in order to request data from the webservice.
METHOD REQUEST_LIBRARY 
    RETRIEVE weather forecast from openweathermap.org API
    TRY input
        PRINT success forecast located
        EXCEPT
            PRINT fail error message
# Display the weather forecast in a readable format to the user.
PRETTIFY retrieved record of weather forecast & PRINT
# Allow the user to run the program multiple times.
INPUT enter another location OR exit
# Use Python 3.