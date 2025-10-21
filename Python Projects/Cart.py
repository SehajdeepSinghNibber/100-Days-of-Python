from prettytable import PrettyTable

foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of {food}: $"))
        food=food.title()
        foods.append(food)
        prices.append(price)
print("-----Your Cart-----")

Cart=PrettyTable()
Cart.add_column("S.No",list(range(1,len(foods)+1)))
Cart.add_column("Items",list(foods))
Cart.add_column("Price", [f"${round(p,2)}" for p in prices])
Cart.add_row(["Total", f"{len(foods)} items", f"${sum(prices):.2f}"])

Cart.align["Price"] = "r"
Cart.align["S.No"] = "l"
Cart.align["Items"] = "l"

print(Cart)