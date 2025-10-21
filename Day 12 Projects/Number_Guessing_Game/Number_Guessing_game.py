import art
import random
print(art.art)
print("Welcome To The Number Guessing Game!")
while True:
    int_random=random.randint(1,100)
    level=input("Which Level do you want to play:\n(E) for Easy\n(M) for Medium\n(H) for Hard\nBy Default Hard mode will be selected: ").upper()
    if level=="E":
        tries=15
        print("Welcome to difficulty mode: Easy")
    elif level=="M":
        tries=10
        print("Welcome to difficulty mode: Medium")
    else:
        tries=5
        print("Welcome to difficulty mode: Hard")
    def guess(tries_left):
        while tries_left > 0:
            print(f"You have {tries_left} tries left.")
            guessed_input = input("Please enter a number between 1 and 100:\n")

            if not guessed_input.isdigit():
                print("Invalid input! Please enter a number.")
                continue

            guessed_number = int(guessed_input)

            if guessed_number < 1 or guessed_number > 100:
                print("Please enter a number between 1 and 100 only.")
                continue

            if guessed_number == int_random:
                print("Congratulations! You found the right number!\nBingo!")
                return
            elif guessed_number < int_random:
                print("Too Low.")
            else:
                print("Too High.")
            
            tries_left -= 1

        print("GAME OVER! You've used all your tries.")
        print(f"The correct number was: {int_random}")
    
    guess(tries)
    should_continue = input("Do you want a new game? (Y/N). By default \"Y\" is taken: ").upper()
    print("Invalid input! Please enter 'Y' or 'N'.")
    if should_continue == "N":
        print("Thanks for playing!")
        break
    

