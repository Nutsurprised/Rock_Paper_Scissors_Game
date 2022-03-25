#Import packages to extend Python ( just like we extend Sublime, Atom or , VScode)
#Step 2: part 1
from random import randint


#step 1
# [] => This is an Array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
#
#
#
choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, scissors: ")

print("user choice" + player_choice)

##Step 4, we are at the 3rd iteration of this game, 3 lives total. 

player_lives = 3
computer_lives = 3
total_lives = 3

#step 2 part 2
computer_choice = choices [randint(0,2)]

print("computer_choice: " + computer_choice)

#Step 3: creating out first condtional, by comparing player choice and computer choice

# if or while
# you can use () to specificy your arguments or, just use : 

if computer_choice == player_choice:
	print("tie")
#Nested conditional using elif
elif computer_choice == "rock":
	if player_choice == "scissors":
		print("you lose!")
		#step 4: way #1) verbose way 
		#player_lives = player_lives - 1
		#step 4: way #2) simplified
		player_lives -= 1
	else:
		print("you win!")
		computer_lives -= 1

elif computer_choice == "paper":
	if player_choice == "scissors": 
		print("you win!")
		computer_lives -= 1
	else:
		print("you lose!")
		player_lives -= 1

elif computer_choice == "scissors":
	if player_choice == "paper":
		print("you lose!")
		player_lives -= 1
	else:
		print("you lose!")
		computer_lives -= 1

#Step 4: Prints out how many lives
print("Player Lives:", player_lives)
print("Computer Lives", computer_lives)


