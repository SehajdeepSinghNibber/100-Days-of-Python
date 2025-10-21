import random
print("Welcome to the hangman game!")
player = ["Virat Kohli", "MS Dhoni", "Jaspreet Bumrah","Hardik Pandya","Adam Zampa","Arshdeep Singh"]
chosen_player = random.choice(player).lower()

display = ""
for letters in chosen_player:
    if letters==" ":
       display += " "
    else:
        display+="_"
print(display)
for i in range(12):
    l = input("Please enter a letter from the player's name you guessed: ").lower()
    new_display=""
    for number in range(len(chosen_player)):
        if chosen_player[number]==l:
            new_display+=l
        else:
            new_display+=display[number]
    print(new_display)
    display = new_display
    if display == chosen_player:
        print(f"You did it!!\nThe correct name was: {chosen_player.title()}")
        break
if display!=chosen_player:
        print(f"You lost it!!\nThe correct name was: {chosen_player.title()}")






