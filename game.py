#Step 2: part 1
from random import randint


#step 1
choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, scissors: ")

print("user choice" + player_choice)

#step 2 part 2
computer_choice = choices [randint(0,2)]

print("computer_choice: " + computer_choice)

#Step 3: creating out first condtional, by comparing player choice and computer choice

# if or while
# you can use () to specificy your arguments or, just use : 

if computer_choice == player_choice:
	print("tie")

elif computer_choice == "rock":
	if player_choice == "scissors":
		print("you lose!")
	else:
		print("you win!")

elif computer_choice == "paper":
	if player_choice == "scissors": 
		print("you win!")
	else:
		print("you lose!")

elif computer_choice == "scissors":
	if player_choice == "paper":
		print("you lose!")
	else:
		print("you lose!")

