import random
print("Welcome To The PyPassword Generator!")
digits=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","q","w","e","r","t","y","u","I","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0","(",")","!","@","#","$","^","&","*","+","-")
number_of_digits=int(input("How many digits would you like?\t"))

while True:
    password=""
    for char in range(0, number_of_digits):
        random_number = random.choice(digits)
        password += random_number
    new_password = list(password)
    random.shuffle(new_password)
    final_password = ''.join(new_password)
    print(f"Your Password is: {final_password}")
    like_it = input("Do you like it?\n Yes/No?")

    if like_it.lower() == "yes":
        break





