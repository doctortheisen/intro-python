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
# Check for rates
# If user purchases less than 100 feet they are charged $.87 per foot.
if cable <= 100:
    cableestimate = cable * 0.87
# If the user purchases more than 100 feet they are charged $.80 per foot.
elif (cable > 100) & (cable <= 250):
   cableestimate = cable * .80
# If the user purchases more than 250 feet they will be charged $.70 per foot.
elif (cable > 250) & (cable <= 500):
   cableestimate = cable * .70
# If they purchase more than 500 feet they will be charged $.50 per foot.
else:
   cableestimate = cable * .50

# PRINT estimate and company name
print ('$', cableestimate, 'for', companyname)