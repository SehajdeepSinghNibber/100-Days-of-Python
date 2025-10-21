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
winner=max(bid, key=bid.get)
print(f"The winning bid is by {winner} with a bid of ${bid[winner]}")

