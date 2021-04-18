#doubler.py
#
# usage:    A program that uses a while loop to determine how long 
#           it takes for an investment to double at a given interest rate.
#   
# input:    annualized interest rate, initial investment amount. 
#
# output:   number of years it takes an investment to double.
#
# 
# PRINT welcome message
print('\nDouble-Your-Money Calculator')

# INPUT principal
principal = float(input('Enter principal ($):  '))

# INPUT interest rate   
interest = float(input('Enter interest rate (as a percentage): '))
#   convert percentage to proportion
interest = interest/100

# initialize loop variables
x = principal
years = 0

# find years until double
while x < (2*principal - principal*interest): # subtract off the last iteration,
                                              # which spills over doubling point
    x = x + x*interest
    years = years + 1

# DEBUG: Verify that x value does not spill over doubling point.
# print(x)

# PRINT result
print (years, 'years to double')