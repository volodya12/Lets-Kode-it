# OOP - Udemy: Selenium WebDriver 4 With Python - Novice To Ninja [2024]
# Everything is an object inside python
# Class is Car       -is object
# def __init__(self): is blueprint/template of a Car - it defines object
# self - references all attributes to the Class
# Attributes/Properties of Car: Color, Make, Model, Mileage, Engine size, etc
# Methods/Operations: Drive, Start car, Stop car, brake, engine start, headlights on/off
# Methods sample: string.upper(), string.lower()   -python build-in methods
# inheritance = sharing methods across other Classes
# super() = it will inherit ALL methods/functions from other Class
# override = whatever is in Parent Class- method, Child Class can inherit and override same method

class Car:
    # define any variable before init, make it global,however its best to define inside __init__
    wheel = 4

    # init-initializes attributes of class- Car
    def __init__(self, color, make, year):
    # def __init__(self, color, make, year=2020): >can be defined inside init as default
        # define attributes
        self.color1 = color
        self.make1 = make
        self.year1 = year

    # Methods
    def startCar(self):
        print("Put the key into the car of", self.make1)
        print("Car STARTED")

    def myColor(self):
        print("The color of my car is", self.color1)

# inheritance from another class
class size(Car):
    def __init__(self, color, make, year):
        # super() means it will inherit ALL methods/functions from other Class
        super().__init__(color, make, year)
        # super().__init__(color, make, year, miles)  # may add additional attributes and define them
        print("inheriting methods: color, make, year")


    def startCar(self):
        # uses method's functions above + add more functionality
        super(size, self).startCar() # calls Method from Parent class, executes, then runs rest of code
        #     ^this is optional
        print("This method has been overridden from Parent Class") # override
        print("Car STOPPED")
        # it then executes method myColor

# these are instances of a Class
c1 = Car("red", "Honda", 2020)  # instance 1
# print(c1.color1)
# print(c1.make1)   >prints Honda
# print(c1.year1)   >prints 2020
c1.startCar()
c1.myColor()
w = c1.wheel=2     # changing variable here, but it wont change globally
print(w)

c2 = Car("blue", "Mazda", 2010) # instance 2
# print(c2.color1)
# print(c2.make1)   >prints Mazda
# print(c2.year1)   >prints 2010
c2.startCar()
c2.myColor()
print(Car.wheel)    # call variable like this, under Class

b = size("Orange", "BMW", 1010)
b.startCar()        # inherited from different Class - Car
b.myColor()         # inherited from different Class - Car
















