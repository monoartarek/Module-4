#access control krobe
#ager code gulote dekhlam je keu jokhon tokhon jekono class ba object ke access korte parteche call korte partice but ekhon amra ei access ta control korbo ke access korte parbe ke parbe na sei control ta amra korbo.ekta company te jokhon kaj korbo tkn egula hide korar proyojon hoy onno sob employee theke karon tokhon eksathe kaj korte hoy. 

class Employee:
    company_name = "Ostad company"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary #ami salary ta sobayke access korte dibo na ejonno salary er age ekta "_salary" underscore dite hobe.but er poreo eita private hobe na properly thats why ekta method use korte hobe jar nam getter method 
        #_salary with a single underscore means it is protected, not fully private. It's a convention that it shouldn't be accessed directly from outside the class.
    def get_salary(self, password):
        if password == "admin":
             print(self._salary)

        else:
            print("Invalid Access!!!!")
        
    def set_salary(self, password, salary):
        if password == "admin":
            self._salary = salary
            print(f"New salary: {self._salary}")

        else:
            print("Invalid Access!!!")



ob1 = Employee("Rahim", 50000)
ob2 = Employee("Karim", 60000)

ob1.get_salary("admin")
ob1.set_salary("admin", 70000) #password wrong dile show korte na invalid access dekhabe
print(ob1._salary)
