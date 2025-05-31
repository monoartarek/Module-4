
class Car:
    # Default value constructor:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
    # _________________________________

    def display_info(self):    # Instance method (instance variable)
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")
        
    # __________________________________

car1 = Car()
car2 = Car()
car1.display_info() #for print the method inside class
