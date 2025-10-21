import random

choices = [
    '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
''',
    '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
''',
    '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
]

print("Welcome to the Rock, Paper, and Scissors game!")
user_choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
computer_choice = random.randint(0, 2)

print(f"\nYour choice:\n{choices[user_choice]}")
print(f"Computer's choice:\n{choices[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice - computer_choice) % 3 == 1:
    print("You won the game, congrats!")
else:
    print("You lost!")
