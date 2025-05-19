print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
tip_amount= float( bill / tip)
final_bill = ((bill + tip_amount) / people)
#rounding to the two digit
rounded_bill = round(final_bill, 2)
print("each person should pay: $  " + str(rounded_bill))