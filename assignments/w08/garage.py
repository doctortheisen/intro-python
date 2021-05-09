# garage.py
#
# usage:    create a virtual garage from menu system
#
#
# 1. Object Oriented Programming and Inheritance - 30%
# 
# Create a Vehicle class with the attributes and functions detailed in the class diagram. - 10%
class Vehicle:
    """A simple class for vehicles in a garage."""

    def __init__(self, make, model, color, fuelType, options):
        """Initialize make, model, color, fuelType, options attributes"""
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def getMake(self):
        """Return vehicle make"""
        return self.make
    
    def getModel(self):
        """Return vehicle model"""
        return self.model
    
    def getColor(self):
        """Return vehicle color"""
        return self.color

    def getFuelType(self):
        """Return vehicle fuelType"""
        return self.fuelType

    def getOptions(self):
        """Return vehicle options"""
        return self.options

# Create a Car class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
class Car(Vehicle):
    """Represent vehicle aspects specific to a car"""

    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        """Initialize attributes of parent class (vehicle), then car"""

        super().__init__(make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors
        
    def getEngineSize(self):
        """Return the engine size"""
        #printed_engine_size = f"{self.engineSize}"
        #return printed_engine_size.title()
        return self.engineSize
    
    def getNumDoors(self):
        """Return number of car doors"""
        #printed_num_doors = f"{self.numDoors}"
        #return printed_num_doors.title()
        return self.numDoors

# Create a Pickup class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
class Truck(Vehicle):
    """Represent vehicle aspects specific to a truck"""

    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        """Initialize attributes of parent class (vehicle), then truck"""

        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength
    
    def getCabStyle(self):
        """Return cab style"""
        #printed_cab_style = f"{self.cabStyle}"
        #return printed_cab_style.title()
        return self.cabStyle

    def getBedLength(self):
        """Return bed length"""
        #printed_bed_length = f"{self.bedLength}"
        #return printed_bed_length.title()
        return self.bedLength


# Car test
#new_car = Car('toyota', 'camry', 'gray', 'unleaded', options_list[0].options, '4-cylinder', 4)
#print(new_car.getMake(), new_car.getModel(), new_car.getColor(), new_car.getFuelType(), new_car.getOptions())
#print(new_car.getVehicleAttributes(), new_car.getEngineSize(), new_car.getNumDoors())
#
# Truck test
#new_truck = Truck('toyota', 'tacoma', 'green', 'unleaded', 'power mirrors', 'supercab', 'short')
#print(new_truck.getVehicleAttributes(), new_truck.getCabStyle(), new_truck.getBedLength())

# 2. Demonstrate usage of previously studied programming constructs (functions, conditionals, loops)  - 60%
# Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%
# 
# Your program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15 %
# 
# Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%
# 
# The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to both cars # and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
# 
list = []
list.append( Vehicle.options('airbags'))
#print(new_car.options[0])
#print(list[0].options)
    #options_list = ['airbags', 'bluetooth', 'cooler', 'dustcover', 'exhaust kit', 'flame stickers', 'grill customization', 'heated seats']

# 3. When the user has finished adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes and options as specified by the user. -10 %
#