print("Welcome to Treasure hunt.")
print("Answer the questions correctly to find treasure.")

question1 = input("There are two doors in front of you. Which one will you open ? red or blue ? \n").lower()

if question1 == "blue":
    question2 = input("Correct answer, now you are at main intersection. Which road will you take ? left or right? \n").lower()

    if question2 == "left":
        question3 = input("Correct answer, now select the correct key to open a Treasure box. Which key will you select ? silver or golden ? \n").lower()

        if question3 == "silver":
            print("Congratulations, you have find the treasure")
        else:
            print("Wrong key, Game Over")

    else:
        print("Wrong road, Game over")

else:
    print ("Wrong door, Game Over")