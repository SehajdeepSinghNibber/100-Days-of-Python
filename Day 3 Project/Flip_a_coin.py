import random
from random import randint, choice

print("Welcome to Flip A Coin Game!")
    ran = randint(1, 2)
    if ran == 1:
        coin = "Heads"
    else:
        coin = "Tails"

    print("Please choose heads or tails")
    choice = int(input("Press '1' for Heads and '2' for Tails"))
    if choice != ran:
        print(f"Sorry you lost!\nIt's {coin}")
    else:
        print(f"Congratulations you have Won!\nIt's {coin}")


