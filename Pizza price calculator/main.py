print("Welcome to the Pizza Shop!")
size = input("What size pizza do you want? S, M or L: \n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
extra_cheese = input("Do you want extra cheese? Y or N: \n")

bill = 0

# to choose pizza size

if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 20
else:
    print("print enter valid input")

# to add pepperoni choice

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#to add cheese

if extra_cheese == "Y":
    bill += 2

print(f"your final bill is $ {bill}.")