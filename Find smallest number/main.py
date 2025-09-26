numbers=[4,5,6,3,1,77,-3,-5,-6,-20,4,7,-200,5,7,]

smallest_number = numbers[0]

for number in numbers:
        if number < smallest_number:
               smallest_number = number

print(smallest_number)
