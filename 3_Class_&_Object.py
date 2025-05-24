 
#car class banabo, setar kichu object banabo 
#Brand, Model

class car:
    def __init__(self): # self ei var class er object ke indicate kore
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