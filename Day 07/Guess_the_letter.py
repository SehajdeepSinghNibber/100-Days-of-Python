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
chosen_mammal=random.choice(mammals).lower()
chosen_letter=input("Please choose a letter:").lower()
if chosen_letter in chosen_mammal:
    print("True")
else:
    print("False")