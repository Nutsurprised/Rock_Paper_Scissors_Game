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

#step 6, creating a boolean data types
# true or false are boolean data types
#essentially, booleans are equivalent toa n on or off switch, 1 or 0.

player_choice = False
# player_choice == False
while player_choice is False: # = True
	#you highlight everything below and tab
	#


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

	if player_lives == 0:
		print("you lose! Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "N" or choice =="n"
			print("You chose to quite! Better luck next time!")
			exit()
		elif choice == "Y" or choice == "y":
			player_lives = total_lives
			computer_lives = total_lives
		else:
			print("Make a valid choice - Y or N")
			choice = input("Y / N?")


	if computer_lives == 0:
		print("you win! Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "N" or choice =="n"
			print("You chose to quite! Better luck next time!")
			exit()
		elif choice == "Y" or choice == "y":
			player_lives = total_lives
			computer_lives = total_lives
		else:
			print("Make a valid choice - Y or N")
			choice = input("Y / N?")



	#Step 4: Prints out how many lives
	print("Player Lives:", player_lives)
	print("Computer Lives", computer_lives)

	#map the loop keep running, by setting player_choice back to False
	#unset, so that our loop condition will evalute to True
	player_choice = False


