# for tight security
# je keu just seen korte parbe but edit korte parbe na 

class Employee:
    company_name = "Developers 7"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    @property  # decorator
    def get_salary(self): # 1
        return self._salary

ob1 = Employee("Rahim", 50000)
print(ob1._salary)
print(ob1.get_salary)  # get salary function but ekhane variable er moto kaj korteche .property decorator use korar jonno 
ob1._salary = 700000
print(ob1._salary)

# ekhon jodi ami chai je keu setake change korate parbe na tahole ekta kaj korte hobe seta holo same name rakhte hobe "_salary" hobe "get salary" er jaygay upore jekhane # 1 diye indicate kora ache. cholo next file e dekhi baper ta 

