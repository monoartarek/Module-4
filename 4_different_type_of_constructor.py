#__init__ thakle Constructor – initializes brand and model
#car class banabo, setar kichu object banabo 
#Brand, Model

#__init__()   --> Dunder method bole (double underscore method) and etake constructor o bole , ei constructor konokicu return kroe na (no return)
# constructor are 3 types:
# 1. Default constructor 
# 2. parameterized constructor 
# 3. Default value constructor 

#amra normally jake function boli, seta ke class er moddhe banale amra take method boli     
class car:
    #default constructor example:
    def __init__(self): # self ei var class er object ke indicate kore, eita ekta default constructor coz eitate kono parameter nai 
        self.brand = ""
        self.model = ""

#first car
car1 = car()#object 
car1.brand = "Toyota" #value assign and modify
car1.model = "corolla" #value assign and modify

print(car1.brand)
print(car1.model)


#second car
car2 = car()
car2.brand = "Honda" #value assign and modify
car2.model = "Civic" #value assign and modify
print(car2.brand, car2.model)