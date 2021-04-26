# mi-to-km.py
# usage:   a function to convert miles to kilometers.
# 
# input:   number of miles driven
#
# output:  total miles and kilometers
# 
# PRINT welcome message
print('\nConverter: Miles to Kilometers')

# INPUT miles
miles = input('Enter miles:  ')

# validate
try:
    miles = float(miles)
except ValueError:
    print("ValueError: You must enter a number for miles")

# begin function
def convert_distance(miles):
    kilometers = miles * 1.609344
    return kilometers
    
# call function and store product
product = convert_distance(miles)

# print result
print("\n"+ str(miles) + " Miles = " + str(product) + " Kilometers")