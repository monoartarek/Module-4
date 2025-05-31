#ekhon dhoro ami admin :
#ami chai ami change korbo tahole ki korte hobe next file e dekhbo cholo ---->

class Employee:
    company_name = "Developers 7"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    @property 
    def salary(self): # ekhane underscore bad dibo 
        return self._salary
    # -------------------if admin want to change the value(salary)--------------------------------------------------
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    # ---------------------------------------------------------------------

ob1 = Employee("Rahim", 50000)
print(ob1.salary) #underscore bad dibo

ob1.salary = 700000 #underscore bad dibo
print(ob1._salary) 


