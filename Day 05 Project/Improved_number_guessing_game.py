import random
print("Welcome To The Number Guessing Game!")
int_random=random.randint(1,100)


while(True):
    Guessed_number = int(input("Please enter a number between 1 to 100\n"))
    if Guessed_number>=100 or Guessed_number<=0:
        print("Please enter number between 1 to 100 only")
    if int_random == Guessed_number:
        print("Congratulations you found the right number!\nBingo!")
        break
    elif int_random < Guessed_number:
        print("The number you guessed is wrong, you chose a smaller number")
    elif int_random > Guessed_number:
        print("The number you guessed is wrong, you chose a greater number")
