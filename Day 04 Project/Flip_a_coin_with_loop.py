import random
from random import randint, choice

print("Welcome to Flip A Coin Game!")
coin = ""
you_won=0
computer_won=0
while True:
    ran = randint(1, 2)
    if ran == 1:
        coin = "Heads"
    else:
        coin = "Tails"

    print("Please choose heads or tails")
    choice = int(input("Press '1' for Heads and '2' for Tails"))
    if choice != ran:
        print(f"Sorry you lost!\nIt's {coin}")
        computer_won += 1
        print(f"Your score = {you_won}")
        print(f"Computer's score = {computer_won}")

    else:
        print(f"Congratulations you have Won!\nIt's {coin}")
        you_won += 1
        print(f"Your score = {you_won}")
        print(f"Computer's score = {computer_won}")
    conti=input("Do you wanna continue?\nType 'Y' for Yes and 'N' for no: ")
    if conti.lower()!='y':
        print("Only 'Y' and 'N' are valid")
    if conti.lower() == 'n':
        break


