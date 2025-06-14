 
#car class banabo, setar kichu object banabo 
#Brand, Model

#__init__()   --> Dunder method bole (double underscore method) and etake constructor o bole , ei constructor konokicu return kroe na (no return)
# constructor are 3 types:
# 1. Default constructor 
# 2. parameterized constructor 
# 3. Default value constructor 

#amra normally jake function boli, seta ke class er moddhe banale amra take method boli     
class car:
    #parameterized constructor:
    def __init__(self, brand, model): #class er nam e object create korle tokhon automatically sei class constructor ke call kore and kaj kore 
        self.brand = brand 
        self.model = model

#first car
car1 = car("Toyota", "Corolla")#object 
print(car1.brand)
print(car1.model)

#second car
car2 = car("Honda", "Civic")
print(car2.brand, car2.model)