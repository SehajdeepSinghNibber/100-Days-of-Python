import random
print("Welcome to the hangman game!")
country = ["India", "Australia", "South Africa","Egypt","America","Canada","Argentina","Brazil","Russia","France","England","Norway","Denmark","Pakistan","Bangladesh","Sri Lanka","Mexico","UAE","Japan","South Korea","North Korea","China"]
chosen_country = random.choice(country).lower()

display = ""
for letters in chosen_country:
    if letters==" ":
       display += " "
    else:
        display+="_"
print(display)
for i in range(10):
    l = input("Please enter a letter from the country's name you guessed: ").lower()
    new_display=""
    for number in range(len(chosen_country)):
        if chosen_country[number]==l:
            new_display+=l
        else:
            new_display+=display[number]
    print(new_display)
    display = new_display
    if display == chosen_country:
        print(f"You did it!!\nThe correct name was: {chosen_country.title()}")
        break
if display!=chosen_country:
        print(f"You lost it!!\nThe correct name was: {chosen_country.title()}")






