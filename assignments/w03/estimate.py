# estimate.py
# usage:    estimate installation cost given company name,
#           feet of cable needed.
#
# PRINT welcome message
print('\nWelcome to the fiber optic install estimator.')
# INPUT company name
companyname = input('Enter company name: ')
# INPUT number of feet of cable needed.
cable = float(input('Enter feet of cable needed: '))
# COMPUTE .87 * cable
cableestimate = cable * 0.87
# PRINT estimate and company name
print ('$', cableestimate, 'for', companyname)