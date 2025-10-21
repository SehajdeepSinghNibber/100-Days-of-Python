import random
print("Welcome to the Rock,Paper and Scissor game!")
choice=int(input("What do you choose, choose 0 for rock,1 for paper and 2 for scissor\n"))
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissor = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
randomizer=random.randint(0,2)
if(choice==1 and randomizer==0):
    print(f"your choice={paper}")
    print(f"computer's choice={rock}")
    print("You won the game congrats!")
elif (choice == 1 and randomizer == 2):
    print(f"your choice={paper}")
    print(f"computer's choice={scissor}")
    print("You Lost!")
if(choice==2 and randomizer==1):
    print(f"your choice={scissor}")
    print(f"computer's choice={paper}")
    print("You won the game congrats!")
elif(choice == 2 and randomizer == 0):
    print(f"your choice={scissor}")
    print(f"computer's choice={rock}")
    print("You Lost!")
if(choice==0 and randomizer==2):
    print(f"your choice={rock}")
    print(f"computer's choice={scissor}")
    print("You won the game congrats!")
elif(choice == 0 and randomizer == 1):
    print(f"your choice={rock}")
    print(f"computer's choice={paper}")
    print("You Lost!")
if(choice==0 and randomizer==0):
    print(f"your choice={rock}")
    print(f"computer's choice={rock}")
    print("It's a draw!")
if(choice==1 and randomizer==1):
    print(f"your choice={paper}")
    print(f"computer's choice={paper}")
    print("It's a draw!")
if(choice==2 and randomizer==2):
    print(f"your choice={scissor}")
    print(f"computer's choice={scissor}")
    print("It's a draw!")