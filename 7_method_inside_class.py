
class car:
    # Default value constructor:
    def __init__(self, brand = "Honda", model = "Civic"):
        self.brand = brand 
        self.model = model
    # _________________________________

    def display_info(self):    # Instance method (instance variable)
        print(f"Car Brand: {self.brand}\n Car Model: {self.model}")
        car1.display_info()
    # __________________________________

#first car
car1 = car() # object 
print(car1.brand)
print(car1.model)

