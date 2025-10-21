print("Welcome to Python Pizza Deliveries")
size = input("What type of Pizza do you want? S, M or L: ").capitalize()
bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 25
else:
    print("Only 'S', 'M' and 'L' are valid choices.")
    exit()

pepperoni = input("Great choice! Would you like some Pepperoni on it? Type 'Y' for yes and 'N' for no: ").capitalize()
if pepperoni == "Y":
    bill += 5
elif pepperoni != "N":
    print("Only 'Y' and 'N' are valid choices.")
    exit()

cheese = input("How about some extra cheese? Type 'Y' for yes and 'N' for no: ").capitalize()
if cheese == "Y":
    bill += 2
elif cheese != "N":
    print("Only 'Y' and 'N' are valid choices.")
    exit()

print(f"Your total bill is ${bill}")
