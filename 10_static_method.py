# etia ashole code gulo organize kore.
class School:
    school_name = "ABC school"

    #decorator er kotha mone ache? function decorator
    @staticmethod # eta te kono "self" or "cls" er proyojon pore na ba use korte pari na. eta kind of choto ekta helper function etar kono class ba instance er data er proyojon pore na eta sotontro hoye thake amar jkn proyojon pore tkn class er nam dhore call kori arki. and class variable and instance variable ke access korte pare na. small kichu kajer jonno amra eita use kori.
    def calculate_grade(marks):
        if marks >= 90:
            return 'A+'
        else:
            return "F"

print(School.calculate_grade(94))



# example 02:

# class Math:
#     @staticmethod
#     def add(x, y):
#         return x + y
    
# m = Math()
# print(m.add(2,3))