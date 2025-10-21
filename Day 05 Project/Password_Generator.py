import random
print("Welcome To The PyPassword Generator!")
alphabets=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","q","w","e","r","t","y","u","I","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m")
Numbers=("1","2","3","4","5","6","7","8","9","0")
Symbols=("(",")","!","@","#","$","^","&","*","+","-")
number_of_numbers=int(input("How many numbers would you like?\t"))
number_of_symbols=int(input("How many symbols would you like?\t"))
number_of_alphabets=int(input("How many alphabets would you like?\t"))

password=""
for char in range(0,number_of_numbers):
    random_number=random.choice(Numbers)
    password+=random_number
for char in range(0, number_of_symbols):
    random_number = random.choice(Symbols)
    password += random_number
for char in range(0, number_of_alphabets):
    random_number = random.choice(alphabets)
    password += random_number
print(f"Your Password is: {password}")
