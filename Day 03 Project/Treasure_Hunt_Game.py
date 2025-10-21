print("Welcome to the Treasure Hunting Game!")
print(r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

Step1 = input("Would you rather go left or right:\n")

if Step1.lower() == "right":
    Step2 = input("There is a river! Would you like to swim or wait for a boat?\n")

    if Step2.lower() == "wait":
        print("A boat arrived! You safely cross the river.")
        Step3=input("Which room will you choose Red, Yellow or Blue: ")
        if Step3.lower() == "blue":
         print("A Wild Crocodile ate you!")
         print("Game Over")
        elif Step3.lower() == "red":
         print("You got burned by fire!")
         print("Game Over")
        elif Step3.lower() == "yellow":
         print("YOU FOUND THE TREASURE CHEST!!!")
         print("🎉 You Win! 🎉")
    elif Step2.lower() == "swim":
        print("Crocodile ate you!")
        print("Game Over")
    else:
        print("Invalid choice. Game Over.")

elif Step1.lower() == "left":
    print("OH NO, YOU FELL INTO A POTHOLE!!!")
    print("Game Over")
else:
    print("You stood still and got lost in the forest. Game Over!.")
