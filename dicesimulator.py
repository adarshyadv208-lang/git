import math , random

# 1. simulate two six-sided dice rolls
roll1 = random.randint(1 , 6)
roll2 = random.randint(1 , 6)

# 2. Compute and print outcomes
print(f"Roll 1: {roll1} | Roll 2 : {roll2}")
total_sum = roll1 + roll2
print(f"Sum: {total_sum}")

#3. Calculate and print square roots
root_val = input(total_sum)
print(f"Squre Root: {root_val: .4f}")