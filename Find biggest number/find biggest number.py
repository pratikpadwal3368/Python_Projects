numbers=[4,5,6,3,1,77,-3,-5,-6,-20,4,7,-200,5,7,]

biggest_number = numbers[0]

for number in numbers:
        if number > biggest_number:
               biggest_number = number

print(biggest_number)