import random
mammals = [
    "Human",
    "Elephant",
    "Tiger",
    "Lion",
    "Dog",
    "Cat",
    "Whale",
    "Dolphin",
    "Bat",
    "Kangaroo",
    "Monkey",
    "Giraffe",
    "Horse",
    "Cow",
    "Sheep",
    "Goat",
    "Pig",
    "Rabbit",
    "Bear",
    "Leopard"
]
chosen_word=random.choice(mammals).lower()
guess = input("Guess a letter: ").lower()
print(guess)
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")