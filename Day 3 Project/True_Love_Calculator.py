print("Welcome to the Love Calculator!")
name1 = input("Enter your name: \n")
name2 = input("Enter their name: \n")

combined_names = (name1 + name2).lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true_score = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love_score = l + o + v + e

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 <= total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
