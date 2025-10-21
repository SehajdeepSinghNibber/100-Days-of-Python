print("Welcome to the tip calculator!")
input1=float(input("what is the total bill?$"))
input2=float(input("how much tip would you like to give? 10, 12 or 15\n"))
if(input2==10 or input2==12 or input2==15):
    input3 = float(input("how many people would you like to split the bill in?"))
    each_person = (input1 + (input1 * input2) / 100) / input3
    print("Each person should pay is $" + str(round(each_person, 2)))
else:
    print("You have given incorrect data for tip, it should be either 10, 12 or percent")


