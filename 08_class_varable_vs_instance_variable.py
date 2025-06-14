class School:
    school_name = "Ostad High School" # class variable 

    def __init__(self, name):
        self.student_name = name 

s1 = School("Tarek")
s2 = School("Rahim")
s3 = School("sadia")
print(s1.school_name)
print(s1.student_name)
# --------------------------
print(s2.school_name)
print(s2.student_name)
# ---------------------------

s3.school_name = "X Y Z High school" #evabe change kora o jabe class variable(not permanent just once)
# School.school_name = "XYZ"   # -->evabe likhle puro class permanently change hoye jabe
print(s3.school_name)
print(s3.student_name)
# -------------------------------
print(s1.school_name)
print(s1.student_name)

# thats means school variable ta prottekta object er jonno same thakbe





# Example 2:

# class School:
#     school_name = "Ghoshnagar govt. primary school"

#     def __init__(self, name):
#         self.name = name
    
# stu1 = School("Tarek")
# stu2 = School("Sadia")

# print(stu1.school_name)
# print(stu1.name)

# # stu2.school_name = "BCPSC"
# School.school_name = "BCPSC"

# print(stu2.school_name)
# print(stu2.name)
        
# print(stu1.school_name)
# print(stu1.name)