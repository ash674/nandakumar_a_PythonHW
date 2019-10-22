from random import randint

choices = ["rock","paper","scissors"]

computer = choices[randint(0,2)]

# set up the game loop so that we dont have to restart all the time
player = False

while player == False:

	player = input("Choose between rock , paper and scissors\n")


	print("Computer chose",computer, "\n")               
	print("Player chose",player, "\n")

	if player =="quit":
		exit()
	elif computer == player:
		print ("Tie ! no one wins , play again")

	player = False
	computer = choices[randint(0,2)]			







	   	





