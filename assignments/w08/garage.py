# garage.py
#
# usage:    create a virtual garage from menu system
#
from vehicle import Vehicle, Car, Truck
#
num_cars = 0
num_trucks = 0

# Add vehicles menu
def add_vehicle_menu():
    global num_cars
    global num_trucks
    while(True):
        new_vehicle = input('Welcome to Garage Main Menu. Which type vehicle would you like to add to your garage? (Type car, truck, or exit)\n').lower()
            # exit loop if user inputs exit request
        if new_vehicle == 'exit':
            break
        elif new_vehicle == 'car':
#           cars = []
            new_car = Car(
                input('Make? '),
                input('Model? '),
                input('Color? '),
                input('Fuel Type? '),
                input('Options? '),
                input('Engine Size? '),
                input('Number of Doors? '))            
            # How do i store the new_car instance to a list?
            # How do I print from that list?
#        print(
#            'Your garage has a new car:\n', 
#            '\nMake: ', new_car.getMake(),
#            '\nModel: ', new_car.getModel(),
#            '\nColor: ', new_car.getColor(),
#            '\n: Fuel Type: ', new_car.getFuelType(),
#            '\n: Options: ', new_car.getOptions(),
#            '\n: Engine Size: ', new_car.getEngineSize(),
#            '\n: Number of Doors: ', new_car.getNumDoors()
# Print the Car
            print(new_car.getMake(), new_car.getModel(), new_car.getColor(), new_car.getFuelType(), new_car.getOptions())
            num_cars = num_cars + 1
            print(num_cars, 'car(s) in garage.\n')

        elif new_vehicle == 'truck':
            new_truck = Truck(
                input('Make? '),
                input('Model? '),
                input('Color? '),
                input('Fuel Type? '),
                input('Options? '),
                input('Cab Style? '),
                input('Bed Length? '))
            num_trucks = num_trucks + 1
# Print the Truck
            print(new_truck.getMake(), new_truck.getModel(), new_truck.getColor(), new_truck.getFuelType(), new_truck.getOptions())
            print(num_trucks, 'truck(s) in garage.\n')

        else:
            print("Please check entry for typo: ", new_vehicle)

    return num_cars, num_trucks
    
# call function and store product
add_vehicle_menu()

# Your program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15 %
if num_cars == 0:
    print('\nPlease add at least one car. Taking you back to main menu...')
    add_vehicle_menu()
# (product stored as global variables.)

if num_trucks == 0:
    print('\nPlease add at least one truck. Taking you back to main menu...')
    add_vehicle_menu()
# (product stored as global variables.)

# print('\nFinished adding vehicles. Your garage has the following:\n', num_cars, 'total cars\n', num_trucks, 'total trucks')

# Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%

# The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to both cars # and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
# 
# list = []
# list.append( Vehicle('airbags'))
#print(new_car.options[0])
#print(list[0].options)
    #options_list = ['airbags', 'bluetooth', 'cooler', 'dustcover', 'exhaust kit', 'flame stickers', 'grill customization', 'heated seats']

# 3. When the user has finished adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes and options as specified by the user. -10 %

