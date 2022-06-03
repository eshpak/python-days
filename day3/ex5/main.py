print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = casefold(name1 + name2)
words = ['true', 'love']
rawRes = [0, 0]

for i in range(2):
    letters = list(words[i])
    for letter in letters:
        rawRes[i] += name.count(letter)

res = int(''.join(str(x) for x in rawRes))

if res < 10 or res > 90:
    print(f"Your score is {res}, you go together like coke and mentos.")
elif res > 40 and res < 50:
    print(f"Your score is {res}, you are alright together.")
else:
    print(f"Your score is {res}.")