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
    print('Enter zip code, city, or exit): ')
    loc = input()
    return loc

# Display the weather forecast in a readable format to the user.
#def prettify_loc(retrieved_match):
    # NOT DEVELOPED
    # pretty_print = # action to clean up retrieved_match
    # PRETTIFY retrieved record of weather forecast
    #print(pretty_print)

# Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
# Use the Requests library in order to request data from the webservice.
def validate_loc(loc):
    #PRINT input being validated
    print('You entered: ', loc, ' Validating...')
    retrieved_match = ''
    try:
        # THIS PART IS NOT DONE
        #REQUEST_LIBRARY 
        #RETRIEVE weather forecast from openweathermap.org API
        # retrieved_match = #API retrieval function return value
        # Match found. Validate with location API.
        print('Success! Match found.')
        # prettify_loc(retrieved_match)
    except:
        #PRINT fail error message
        print('Failure: Location match not found. Please enter information again.')
        # Send user back to input another function.
        get_loc()
    return retrieved_match

# Run main function
# EXECUTE main function
# Allow the user to run the program multiple times.
run_again = 'yes'
while (run_again == 'yes') or (run_again == 'y'):
    loc = get_loc()
    validate_loc(loc)
    print('Do you want to check another location? (yes or no)')
    run_again = input()
    
    if (run_again == 'no'):
        print("Exiting program.")
        exit