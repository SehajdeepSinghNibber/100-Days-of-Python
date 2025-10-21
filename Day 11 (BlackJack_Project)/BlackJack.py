import random
import BlackJack_art

print(BlackJack_art.Logo)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_total(hand):
    total = sum(hand)
    ace_count = hand.count(1)
    while ace_count > 0 and total + 10 <= 21:
        total += 10
        ace_count -= 1
    return total

print("Welcome to Blackjack!")
while True:
    Your_cards = []
    opponent_cards = []
    for _ in range(2):
        Your_cards.append(random.choice(cards))
        opponent_cards.append(random.choice(cards))
    Sum_your_cards = calculate_total(Your_cards)
    Sum_opponent_cards = calculate_total(opponent_cards)

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
            Sum_your_cards = calculate_total(Your_cards)
            print(f"Your cards: {Your_cards} (Total: {Sum_your_cards})")
        else:
            break

    if Sum_your_cards == 21:
        print("Blackjack! You Won!")
    elif Sum_your_cards > 21:
        print("You Lost!")
    else:
        while Sum_opponent_cards < 17:
            opponent_cards.append(random.choice(cards))
            Sum_opponent_cards = calculate_total(opponent_cards)
        print(f"Opponent's cards: {opponent_cards} (Total: {Sum_opponent_cards})")
        if Sum_opponent_cards > 21:
            print("Opponent bust! You Won!")
        elif Sum_your_cards > Sum_opponent_cards:
            print("You Won!")
        elif Sum_your_cards == Sum_opponent_cards:
            print("It's a draw!")
        else:
            print("You Lost!")

    while True:
        should_continue = input("Do you want a new match? (Y/N): ").upper()
        if should_continue in ["Y", "N"]:
            break
        print("Invalid input! Please enter 'Y' or 'N'.")
    if should_continue == "N":
        print("Thanks for playing!")
        break