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

    def getVehicleAttributes(self):
        """Print vehicle attributes"""
        printed_vehicle_attributes = f"{self.make} {self.model} {self.color} {self.fuelType} {self.options}"
        return printed_vehicle_attributes.title()

# Create a Car class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
    def Car(self, engineSize, numDoors):
        """Attributes of car"""
        self.engineSize = engineSize
        self.numDoors = numDoors
        
    def getEngineSize(self):
        """Return the engine size"""
        printed_engine_size = f"{self.engineSize}"
        return printed_engine_size.title()
    
    def getNumDoors(self):
        """Return number of car doors"""
        printed_num_doors = f"{self.numDoors}"
        return printed_num_doors.title()

# Create a Pickup class as a child of the Vehicle class with the attributes and functions detailed in the class diagram. - 10%
    def truck(self, cabStyle, bedLength):
        self.cabStyle = cabStyle
        self.bedLength = bedLength
    
    def getCabStyle(self):
        """Return cab style"""
        printed_cab_style = f"{self.cabStyle}"
        return printed_cab_style.title()

    def getBedLength(self):
        """Return bed length"""
        printed_bed_length = f"{self.bedLength}"
        return printed_bed_length.title()

new_vehicle = Vehicle('toyota', 'tacoma', 'green', 'unleaded', 'power mirrors')
print(new_vehicle.getVehicleAttributes())
# 2. Demonstrate usage of previously studied programming constructs (functions, conditionals, loops)  - 60%
# Using a function, display a menu prompting the user to add a Car or a Pickup to their virtual garage. - 15%
# 
# Your program must allow the user to have multiple vehicles in their virtual garage and must have at least one Car and one Pickup. - 15 %
# 
# Your program will prompt the user to define the attributes of the vehicles in their garage. - 10%
# 
# The options attribute will be defined as a python list chosen by the user when presented with a menu of programmer chosen vehicle options that can apply to both cars # and pickup trucks (i.e. power mirrors, power locks, remote start, backup camera, bluetooth, cruise control, etc) - 20%
#
# 3. When the user has finished adding and defining vehicles for their garage the program will output the vehicles with their accompanying attributes and options as specified by the user. -10 %
#