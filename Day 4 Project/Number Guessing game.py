import random
print("Welcome To The Number Guessing Game!")
int_random=random.randint(1,100)
Guessed_number=int(input("Please enter a number between 1 to 100\n"))

if int_random==Guessed_number:
    print("Congratulations you found the right number!\nBingo!")
elif int_random>Guessed_number and int_random<100 and int_random>=0:
    print("The number you guessed is wrong, you chose a greater number")
elif int_random<Guessed_number and int_random>=0 and int_random<100:
    print("The number you guessed is wrong, you chose a smaller number")
else:
    print("Please enter a number between 1 to 100 only)")