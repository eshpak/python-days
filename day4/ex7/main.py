import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
n = random.randrange(0, len(names))

print(f"{names[n]} is going to buy the meal today!")