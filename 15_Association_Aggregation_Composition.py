# multiple class thakle tader moddhe relationship ke maintain kore egula.
# NO 1: Association:
# Student, laptop duita class banabo and egula ekjon arekjoner sathe interact korbe 

class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name 
        self.laptop_var = laptop_obj 

    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_var.brand}") #ekhane ami 2 ta class ke use korte partechi / 2 ta class interact hocche
lp1 = Laptop("Asus")
Student = Student("Rahim", lp1)
Student.show_laptop_info()

# ekhane amra 2 ta class ke interact korte parchi jake Association bole