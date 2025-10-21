import random
print("Welcome to the hangman game!")
country = ["India", "Australia", "South Africa","Egypt","America","Canada","Argentina","Brazil","Russia","France","England","Norway","Denmark","Pakistan","Bangladesh","Sri Lanka","Mexico","UAE","Japan","South Korea","North Korea","China"]
chosen_country = random.choice(country).lower()

placeholder = ""
correct_letter=[]
for letters in chosen_country:
    if letters==" ":
       placeholder += " "
    else:
        placeholder+="_"
print(placeholder)
for i in range(10):
    guess = input("Please enter a letter from the country's name you guessed: ").lower()
    display=""
    for alphabet in chosen_country:
        if alphabet==guess:
            correct_letter.append(guess)
            display+=alphabet
        elif alphabet in correct_letter:
            display+=alphabet
        elif alphabet==" ":
            display+=" "
        else:
            display+="_"

    print(display)
    if "_" not in display:
        print("You Win!")
        break
if "_" in display:
    print("You lost!")