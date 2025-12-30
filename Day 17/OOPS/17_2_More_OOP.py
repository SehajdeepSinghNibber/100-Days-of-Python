class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("hi", self.name, "your avg score is:", total / 3)


s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()
s1.name="Ironman"
s1.get_avg()

'''Static Method'''

# class Student:
#     def greet (): ##no self
#         print("Hello World!!")

# s1 = Student()
# s1.greet()

'''Static Method, it is a decorator method'''

class Student:

    @staticmethod
    def greet ():
        print("Hello World!!")


s1 = Student()
s1.greet()

##del Keyword

class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Sehajdeep")
print(s1.name)
s1.name="Patrick"
print(s1.name)
# del s1.name #will provide error since it's deleted now
# print(s1.name)

#Private and Public

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account(12345,"abcde")
print(acc1.acc_no)
print(acc1.reset_pass())
# print(acc1.__acc_pass) #error since it's private

#Conceptuallt Private

class Person:
    __name = "Sehajdeep"  # private variable since started with__

    def __hello(self, name):  # private method
        print(f"Hello person! {name}")

    def greet(self):
        self.__hello(self.__name)

p1 = Person()

print(p1.greet())