enemies=1

def increase_enemies():
    enemies=2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def increase_enemies_2():
    global enemies
    enemies+=2
    print(f"enemies inside function: {enemies}")
increase_enemies_2()
