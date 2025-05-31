# for tight security
# je keu just seen korte parbe but edit korte parbe na 

class Employee:
    company_name = "Developers 7"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    @property  # decorator
    def _salary(self): # 1
        return self._salary

ob1 = Employee("Rahim", 50000)
print(ob1._salary)

ob1._salary = 700000
print(ob1._salary) # change hobe na ba keu korte parbe na ejonno error ashbe output e. je keu just dekhte parbe but ei property keu e change korte parbe na.


#ekhon dhoro ami admin :
#ami chai ami change korbo tahole ki korte hobe next file e dekhbo cholo ---->