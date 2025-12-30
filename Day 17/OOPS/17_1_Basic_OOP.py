class Student:
    name="Sehajdeep Singh"

s1=Student()
print(s1)
print(s1.name)
class Car:
    color="blue"
    company="Tesla"
c1=Car()
print(c1)
print(c1.color)
print(c1.company)

'''Constructor or __init__ function'''
'''Invoked at the moment of object creation'''
class Student:
    def __init__(self):
        print("Adding new student in database...")
    name="Sehajdeep"

s1=Student()

'''Constructor or __init__ function'''
'''Invoked at the moment of object creation'''
class Student:
    name="Sehajdeep"
    def __init__(self,fullname):
        self.name=fullname
        print(self)
        print("Adding new student in database...")

s1=Student("Karan")
print(s1.name)

class Student:
    def __init__(self):
        pass #default Constructor
    def __init__(self,name,marks):
        #paramerized Constructors
        self.name=name
        self.marks=marks

s1=Student("Karan",88)  
print(s1.name,s1.marks)
s2=Student("Arjun",79)
print(s2.name,s2.marks)