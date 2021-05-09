# garage.py
#
# usage:    create a virtual garage from menu system
#
from vehicle import Vehicle, Car, Truck
#
# Car test
#new_car = Car('toyota', 'camry', 'gray', 'unleaded', options_list[0].options, '4-cylinder', 4)
#print(new_car.getMake(), new_car.getModel(), new_car.getColor(), new_car.getFuelType(), new_car.getOptions())
#
# Truck test
#new_truck = Truck('toyota', 'tacoma', 'green', 'unleaded', 'power mirrors', 'supercab', 'short')
#print(new_truck.getMake(), new_truck.getModel(), new_truck.getColor(), new_truck.getFuelType(), new_truck.getOptions())

# 2. Demonstrate usage of previously studied programming constructs (functions, conditionals, loops)  - 60%
# Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%
num_cars = 0
num_trucks = 0

# Add car menu
def add_car():
#    cars = {}
    adding_car_state = True

    while adding_car_state:
        new_car = Car(input('Make? '), input('Model? '), input('Color? '), input('Fuel Type? '), input('Options? '), input('Engine Size? '), input('Number of Doors? '))
    
#        print(
#            'Your garage has a new car:\n', 
#            '\nMake: ', new_car.getMake(),
#            '\nModel: ', new_car.getModel(),
#            '\nColor: ', new_car.getColor(),
#            '\n: Fuel Type: ', new_car.getFuelType(),
#            '\n: Options: ', new_car.getOptions(),
#            '\n: Engine Size: ', new_car.getEngineSize(),
#            '\n: Number of Doors: ', new_car.getNumDoors()
#            )
#    cars[] = new_car
    adding_car_state = False
    return new_car

# Add truck menu
def add_truck():
    adding_truck_state = True

    while adding_truck_state:
    
        new_truck = Truck(input('Make? '), input('Model? '), input('Color? '), input('Fuel Type? '), input('Options? '), input('Cab Style? '), input('Bed Length? '))
    
#    print(
#        'Your garage has a new car:\n', 
#        '\nMake: ', new_truck.getMake(),
#        '\nModel: ', new_truck.getModel(),
#        '\nColor: ', new_truck.getColor(),
#        '\n: Fuel Type: ', new_truck.getFuelType(),
#        '\n: Options: ', new_truck.getOptions(),
#        '\n: Engine Size: ', new_truck.getCabStyle(),
#        '\n: Number of Doors: ', new_truck.getBedLength()
#        )
        another_truck = input('\nAdd another truck? yes or no: ') 
        if  another_truck == 'no':
            adding_truck_state = False
        #elif another_truck == 'yes':
        #    adding_truck_state = 
    return new_truck

# Add vehicles menu
def add_vehicle_menu():
    global num_cars
    global num_trucks
    while(True):
        new_vehicle = input('What vehicle do you want to add to your garage? (Type car, truck, or exit)\n').lower()
            # exit loop if user inputs exit request
        if new_vehicle == 'exit':
            break
        elif new_vehicle == 'car':
            add_car()
            num_cars = num_cars + 1
            print(num_cars, 'car(s) in garage.\n')
        elif new_vehicle == 'truck':
            add_truck()
            num_trucks = num_trucks + 1
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