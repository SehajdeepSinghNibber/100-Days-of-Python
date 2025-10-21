import art
import numbers
import alphabets
import os
while True:
    print(art.art)
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt the text. (Default is 'encode')\n")
    text = input("Type the message:\n")
    shift = int(input("Type the shift number:\n"))


    def ceaser(original_text, shift_amount, encode_or_decode):
        cypher_text = ""
        if encode_or_decode.lower() == "decode":
            shift_amount *= -1
        for letters in original_text:
            if letters in alphabets.alphabets:
                shifted_position = (alphabets.alphabets.index(letters) + shift_amount) % 26
                cypher_text += alphabets.alphabets[shifted_position]
            elif letters in numbers.numbers:
                shifted_position =(numbers.numbers.index(letters) + shift_amount) % 10
                cypher_text += numbers.numbers[shifted_position]
            else:
                cypher_text+=letters
        print(cypher_text.title())

    ceaser(text.lower(), shift, direction.lower())
    while True:
        resume = input("Do you wanna continue?\nType 'Y' for Yes and 'N' for No:\n")
        if resume.lower() == 'y':
            os.system("cls" if os.name == "nt" else "clear")
            break
        elif resume.lower() != 'y' and resume != 'n':  #
            print("Please enter either 'y' or 'n' only.")
        else:
            break
    if resume == "n":
        os.system("cls" if os.name == "nt" else "clear")
        print("Goodbye!!")
        break






