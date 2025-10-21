import art
print(art.art)
print("Welcome to prime number checker!")
while True:
    number_to_be_checked=int(input("Please Enter the number you want to check: "))

    def prime(num):
        if num <= 1:
            print(f"{num} is not a Prime Number!")
            return
        if num == 2:
            print(f"{num} is a Prime Number!")
            return
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a Prime Number!")
                return
        print(f"{num} is a Prime Number!")

 
    prime(number_to_be_checked)
    should_continue=input("Do you want to continue checking for the same? (Y/N)").upper
    if should_continue in ["Y", "N"]:
        break
    print("Invalid input! Please enter 'Y' or 'N'.")
    if should_continue == "N":
        print("Thanks for playing!")
        break
    while True:
        should_continue = input("Do you want a new match? (Y/N): ").upper()
        if should_continue in ["Y", "N"]:
            break
        print("Invalid input! Please enter 'Y' or 'N'.")
    if should_continue == "N":
        print("Thanks for playing!")
        break