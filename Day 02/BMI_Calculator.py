print("BMI Calculator")
height=float(input("Please enter your height in meters\n"))
weight=float(input("Please enter your weight in Kilograms\n"))

print("Your BMI is",(weight/(height**2)))

BMI=(weight/(height**2))

if(BMI>=18.5 and BMI<25):
    print("Your are healthy")
elif(BMI<18.5):
    print("You are underweight")
elif(BMI>=25 and BMI<=30):
    print("You are overweight")
else:
    print("You are obese")