class School:
    school_name = "Ostad High School" # class variable 

    def __init__(self, name):
        self.student_name = name 

sc1 = School("Tarek")
sc2 = School("Rahim")
sc3 = School("sadia")
print(sc1.school_name)
print(sc1.student_name)
# --------------------------
print(sc2.school_name)
print(sc2.student_name)

sc3.school_name = "XYZ" #evabe change kora o jabe class variable(not permanent just once)
# School.school_name = "XYZ"   # -->evabe likhle puro class permanently change hoye jabe
print(sc3.school_name)
print(sc3.student_name)


# thats means school variable ta prottekta object er jonno same thakbe