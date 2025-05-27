 
#car class banabo, setar kichu object banabo 
#Brand, Model

class car: # A class is like a blueprint for creating objects.
    def __init__(self): # self ei var class er object ke indicate kore. __init__ is the constructor method that runs automatically when a new object of the class is created.

        self.brand = ""
        self.model = ""

#first car
car1 = car()#object. This creates an instance (object) of the class car, and calls the __init__ method to initialize it.
car1.brand = "Toyota" #value assign and modify
car1.model = "corolla" #value assign and modify

print(car1.brand)
print(car1.model)


#second car
car2 = car()
car2.brand = "Honda" #value assign and modify
car2.model = "Civic" #value assign and modify
print(car2.brand, car2.model)

# Optional Tip:
# By convention, class names in Python are written in PascalCase (starting with a capital letter), so Car would be more appropriate than car