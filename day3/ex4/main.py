print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")

price = 15

if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25

if pepperoni == "Y":
    if size != "S":
        price += 3
    else:
        price += 2

if cheese == "Y":
    price += 1


print(f"Your final bill is: ${price}.")
