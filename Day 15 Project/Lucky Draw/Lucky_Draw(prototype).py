import random

print("Welcome to PyLottery!!")
while True:
    while True:
        Participants=int(input("Please enter the number of Lotteries you want to buy: "))
        Winning_Lottery=random.randint(1000,9999)
        Lotteries_bought=[]
        if Participants > 9000:
            print("Sorry you can't buy more than 9000 lotteries")
        else:
            break
    for _ in range(Participants):
        ticket=random.randint(1000,9999)
        while ticket in Lotteries_bought:
            ticket=random.randint(1000,9999)
        Lotteries_bought.append(ticket)
    print("Your Lotteries numbers are",end=" ")
    print(*Lotteries_bought,sep=",")
    if Winning_Lottery in Lotteries_bought:
        print(f"Congratulations you have won a lottery!!\nWinning Lottery Number was {Winning_Lottery}")
    else:
        print(f"Better luck next time!\nWinning Lottery was {Winning_Lottery}")
    while True:
        play_again = input('Do you want to enter another Lottery Contest? Type "Y" for Yes and "N" for No: ').upper()
        if play_again == "Y":
            print("\n"*1000)
            break
        elif play_again == "N":
            print("Thanks for playing PyLottery! Goodbye.")
            exit()
        else:
            print('Invalid input. Please enter only "Y" or "N".')