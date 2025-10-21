alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
art = r'''
░█████╗░░█████╗░███████╗░██████╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝

░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
'''

while True:
    print(art)
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt the text. (Default is 'encode')\n")
    text = input("Type the message:\n")
    shift = int(input("Type the shift number:\n"))


    def caeser(original_text, shift_amount, encode_or_decode):
        cypher_text = ""
        if encode_or_decode.lower() == "decode":
            shift_amount *= -1
        for letters in original_text:
            if letters in alphabets:
                shifted_position = (alphabets.index(letters) + shift_amount) % 26
                cypher_text += alphabets[shifted_position]
            else:
                cypher_text+=letters
        print(cypher_text.title())


    caeser(text.lower(), shift, direction.lower())
    while True:
        resume = input("Do you wanna continue?\nType 'Y' for Yes and 'N' for No:\n")
        if resume.lower() == 'y':
            break
        elif resume.lower() != 'y' and resume != 'n':  #
            print("Please enter either 'y' or 'n' only.")
        else:
            break
    if resume == "n":
        print("Goodbye")
        break






