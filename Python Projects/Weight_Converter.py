print("Welcome to weight converter!")

while True:
    weight = float(input("Enter your weight: "))
    unit = input('Kilogram or Pound ("K" or "L"): ').strip().upper()

    if unit == "K":
        weight = weight * 2.205
        weight = round(weight, 2)
        print(f"Your weight is {weight} Pounds")
    elif unit == "L":
        weight = weight / 2.205
        weight = round(weight, 2)
        print(f"Your weight is {weight} Kilograms")
    else:
        print("Please enter valid units (\"K\" or \"L\")")
        continue
    while True:
        To_continue = input('Do you want more conversions? Type ("Y" or "N"): ').strip().upper()
        if To_continue == "Y":
            break
        elif To_continue == "N":
            print("Thank you for using the converter!")
            exit()
        else:
            print("Please enter a valid input (\"Y\" or \"N\")")
