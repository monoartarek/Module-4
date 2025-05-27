class Employee:
    company_name = "Ostad Company"

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
    def display_info(self): # instnce Method
        print(f"Emp Name: {self.name}\nSalary: {self.salary}")
    #decorator er kotha mone ache? function decorator
    @classmethod
    def change_commpany_name(cls, name): # (eta ekta class method). aage object er jonno use kortm "self" and class er jonno amra use korbo "cls"
        cls.company_name = name 

ob1 = Employee("Rahim", 30000)
ob2 = Employee("Karim", 40000)
ob1.display_info()

# ob1.change_commpany_name("ABC complany") 
Employee.change_commpany_name("XYZ company")  #amra obossoi class ke call kore class variable change korbo object ke dhore korbo na  
# globaly sob jaygay company name change korte eita use korte hobe
print(ob1.company_name)
print(ob2.company_name)
