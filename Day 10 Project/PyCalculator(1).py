
art='''╭━━━╮╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭╮
┃╭━╮┃╱╱╱┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃┃╱╱╭╯╰╮
┃╰━╯┣╮╱╭┫┃╱╰╋━━┫┃╭━━┳╮╭┫┃╭━┻╮╭╋━━┳━╮
┃╭━━┫┃╱┃┃┃╱╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃┃┃╭╮┃╭╯
┃┃╱╱┃╰━╯┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰┫╰╯┃┃
╰╯╱╱╰━╮╭┻━━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━┻━━┻╯
╱╱╱╱╭━╯┃
╱╱╱╱╰━━╯
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operation={"+":add,
           "-":subtract,
           "*":multiply,
           "/":divide}
print(art)
def calculator():
    print("Welcome to PyCalculator!")
    while True:
        first = float(input("Enter your first number:"))
        while True:
            operator = input(f"Choose and operator from {list(operation.keys())}:")
            second = float(input("Enter your next number:"))
            result = operation[operator](first, second)
            print(f"{first} {operator} {second} = {result}")
            should_continue = input(
                f"Do yo want to continue calculation with {result}? Type \"Y\" for yes and \"n\" for no(By default \"No\"):")
            if should_continue.upper() == "Y":
                first = result
            else:
                should_continue2 = input(
                    f"\nDo yo want to continue calculation with? Type \"Y\" for yes and \"n\" for no(By default \"Yes\"):")
                if should_continue2.upper() == "N":
                    print("PyCalculator Closing.")
                    break

calculator()

