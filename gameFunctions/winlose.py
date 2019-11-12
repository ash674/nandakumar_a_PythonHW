from random import randint
from gameFunctions import gameVars
# define a function that takes an argument

def winorlose(status):
	print("******************")
	print("You",status, "!Would you like to play again")

	choice = input("Y / N")
	print(choice)
	
	if (choice is "N") or (choice is "n"):
		print("you choose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		#reset the game so that we start all over again
		
					
		gameVars.player_lives= 5
		gameVars.computer_lives= 5
		gameVars.total_lives= 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

	else:

	# use recursion to call winorlose agin until we get the right input
	# recursion is just a fancy way to describe calling a fucntion from within itself
		winorlose(status)  	