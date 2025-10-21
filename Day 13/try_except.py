try:
    age=int(input("Please enter your age "))
except ValueError:
    print("You have typed an invalid number. Please try again with a numeric response like 15.")
    age=int(input("Please enter your age "))
if age>=65:
    print("You are too old and advised not to drive.")
elif age>=18:
    print("You can drive!")
else:
    print("Sorry but you are not allowed to drive.")