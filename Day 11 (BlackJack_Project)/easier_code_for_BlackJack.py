import random
import BlackJack_art

print(BlackJack_art.Logo)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to Blackjack!\n\n")

You_Won = 0
Opponent_won = 0

while True:
    Your_cards = []
    opponent_cards = []
    for _ in range(2):
        Your_cards.append(random.choice(cards))
        opponent_cards.append(random.choice(cards))
    Sum_your_cards = sum(Your_cards)
    Sum_opponent_cards = sum(opponent_cards)

    if Sum_your_cards-10>=21:
        Your_cards.append(11)
        Your_cards.remove(1)
    if Sum_opponent_cards-10>=21:
        opponent_cards.append(11)
        opponent_cards.remove(1)
    print(f"Your score={You_Won}")
    print(f"Opponent's score={Opponent_won}")

    print(f"\nYour cards: {Your_cards} (Total: {Sum_your_cards})")
    print(f"One of opponent's cards: {opponent_cards[0]}")

    while Sum_your_cards < 21:
        while True:
            ask = input("Do you want more cards? (Y/N): ").upper()
            if ask in ["Y", "N"]:
                break
            print("Invalid input! Please enter 'Y' or 'N'.")
        if ask == "Y":
            Your_cards.append(random.choice(cards))
            Sum_your_cards = sum(Your_cards)
            print(f"Your cards: {Your_cards} (Total: {Sum_your_cards})")
        else:
            break

    if Sum_your_cards == 21:
        print("Blackjack! You Won!")
        You_Won+=1
    elif Sum_your_cards > 21:
        print("You Lost!")
        Opponent_won+=1
    else:
        while Sum_opponent_cards < 17:
            opponent_cards.append(random.choice(cards))
            Sum_opponent_cards = sum(opponent_cards)
        print(f"Opponent's cards: {opponent_cards} (Total: {Sum_opponent_cards})")
        if Sum_opponent_cards > 21:
            print("Opponent bust! You Won!")
            You_Won+=1
        elif Sum_your_cards > Sum_opponent_cards:
            print("You Won!")
            You_Won+=1
        elif Sum_your_cards == Sum_opponent_cards:
            print("It's a draw!")
        else:
            print("You Lost!")
            Opponent_won+=1

    while True:
        should_continue = input("Do you want a new match? (Y/N): ").upper()
        if should_continue in ["Y", "N"]:
            break
        print("Invalid input! Please enter 'Y' or 'N'.")
    if should_continue == "N":
        print("Thanks for playing!")
        break