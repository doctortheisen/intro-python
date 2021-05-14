#vehicle.py

"""Class module for Vehicle (Parent) and Car, Truck (Child)"""
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
        return self.engineSize
    
    def getNumDoors(self):
        """Return number of car doors"""
        return self.numDoors

#    def display(self):
#       print getMake(self)
#		print('{make} {model} {color} {fuelType} {options}'
#				 .format(make= self.make, model=round(self.model(), color= self.color, rate= round(self.rate, 5), time_period= self.time_period))


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
        return self.cabStyle

    def getBedLength(self):
        """Return bed length"""
        return self.bedLength