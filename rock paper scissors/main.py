import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (___)
---.__(___)
'''

choice_list = ["rock","paper","scissors"]
user_choice = input("what do you choose ? type your choice- rock,paper or scissors \n").lower()
game_image = {
    "rock" : rock,
    "paper" : paper,
    "scissors" : scissors,
}

computer_choice = random.choice(choice_list)

if user_choice not in choice_list:
        print("invalid choice. please type rock,paper or scissors")
        exit()

print("you choose " + user_choice)
print(game_image[user_choice])
print("computer choose " + computer_choice )
print(game_image[computer_choice])

if user_choice == computer_choice:
    print("Its tie")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You Win!")
else:
    print("You loose")
