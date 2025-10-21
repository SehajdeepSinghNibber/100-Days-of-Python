import Logo
print(Logo.logo)
print("Welcome to the Silent Auction!")
bid={}
while True:
    name=input("What is your name?:")
    price=int(input("What is your bid?:$"))
    bid[name]=price
    Should_Continue=input("Are there any other bidders? Type 'Yes' or 'No' (Default is 'No')")
    print("\n"*100)
    if Should_Continue.title()!="Yes":
        break

def find_the_highest_bidder(bidding_dictionary):
    high_bid=0
    winner=""
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>high_bid:
            high_bid=bid_amount
            winner=bidder
    print(f"The winning bid is by {winner} with a bid of ${bid[winner]}")

find_the_highest_bidder(bid)