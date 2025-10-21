enemies=1

def increase_enemies():
    #local scope
    enemies=2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Scope
player_health=10

def drink_potion():
    print(player_health)

drink_potion()
print(player_health)