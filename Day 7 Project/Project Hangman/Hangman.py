import Art
import Hangman_art
import Mammals
import random

while True:
    chosen_word = random.choice(Mammals.mammals).lower()
    print(Art.art)
    correct_letter = []
    lives = 6
    while True:
        placeholder = "_" * len(chosen_word)
        print("\n")
        print(placeholder)
        print(Hangman_art.stages[lives])
        while lives > 0:
            Guess = input("Guess the letter: ").lower()
            display = ""
        
            if Guess in correct_letter:
                print("You already guessed that letter!")
            else:
                if Guess in chosen_word:
                   correct_letter+=Guess
                else:
                   lives -= 1
        
            for letter in chosen_word:
               if letter in correct_letter:
                display += letter
               else:
                 display += "_"
        
            print("\n")
            print(display)
            print(Hangman_art.stages[lives])
            print(f"Lives remaining: {lives}")
        
            if "_" not in display:
                print("You Win!")
                break
    
        if lives == 0:
            print(f"You Lost! The word was {chosen_word}")
    
        To_continue = input('Do you wanna continue? Type "Y" for yes and "N" for No(By default "Y"): ')
        if To_continue.upper() == "N":
            break
