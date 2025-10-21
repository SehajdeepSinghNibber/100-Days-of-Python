import random

# Random float between 1 and 10
random_float = random.uniform(1, 10)
print(random_float)

# Option 1: Use randint to get a random int between 1 and 10
ranint = random.randint(1, 10)
print(ranint)

# Option 2: Use choice with a range
rantint = random.choice(range(1, 11))  # 1 to 10 inclusive
print(rantint)
