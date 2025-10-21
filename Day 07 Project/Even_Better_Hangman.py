import random
Mammals = ["Baboon", "Monkey", "Gorilla", "Chimpanzee"]
Chosen_ape = random.choice(Mammals).lower()

stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

placeholder = ""
correct_letter = []
lives = 6

for letter in Chosen_ape:
    placeholder += "_"
print("\n")
print(placeholder)
print(stages[lives])
while lives>0:
    Guess=input("Guess the letter: ")
    display=""
    for letter in Chosen_ape:
        if Guess==letter:
            correct_letter.append(Guess)
            display+=letter
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"
    if Guess in correct_letter:
        print("You already guessed that letter!")
    if Guess not in Chosen_ape:
        lives=lives-1
    print("\n")
    print(display)
    print(stages[lives])
    print(f"Lives remaining: {lives}")

    if "_" not in display:
        print("You Win!")
        break

if lives == 0:
    print(stages[lives])
    print(f"You Lost! The word was {Chosen_ape}")


