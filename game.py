from random import randint

choices = ["rock","paper","scissors"]

computer = choices[randint(0,2)]
#Set up some variables  for player and Ai lives
player_lives= 5
computer_lives=5


# set up the game loop so that we dont have to restart all the time
player = False

while player == False:
	
	print("--------------------------------------------------")
	print("Computer lives :",computer_lives,"/5\n")
	print("Player lives :",player_lives,"/5\n")
	player = input("Choose between rock , paper and scissors\n\n")
	print("------------------------------------------------")

	print("Computer chose",computer, "\n")               
	print("Player chose",player, "\n")
	if player.lower() =="quit":
		exit()
	elif computer == player:
		print ("Tie ! no one wins , play again")
	elif player.lower() == "rock":
	    if computer == "paper":
	    	print("You lose !!",computer,"Covers",player,"\n")
	    	player_lives = player_lives - 1
	    else:
	     	print("You win!!!!",player,"smashes",computer,"\n")
	     	computer_lives = computer_lives - 1
	elif player.lower() == "paper":
	    if computer == "scissors":
	    	print("You lose !!",computer,"cuts",player,"\n")
	    	player_lives = player_lives - 1
	    else:
	     	print("You win!!!!",player,"covers",computer,"\n")
	     	computer_lives = computer_lives - 1
	elif player.lower() == "scissors":
	    if computer == "rock":
	    	print("You lose !!",computer,"smashes",player,"\n")
	    	player_lives = player_lives - 1
	    else:
	     	print("You win!!!!",player,"cuts",computer,"\n")
	     	computer_lives = computer_lives - 1
	     	
	else:
		print("Thats not a valid choice,try again")     	    	    	   	
	if player_lives is 0:
		print("You Lose !!!!!!!! Would you like to try again\n")
		choice = input("Y/N")
		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()	
		elif (choice is "Y") or (choice is "y"):
			player_lives = 5
			computer_lives = 5
			player = False 
			computer = choices[randint(0,2)]
		else:	
			player = False
			computer = choices[randint(0,2)]		
	elif computer_lives is 0:
		print("Computer is out of live....YOU WON THE GAME... Would you like to try again\n")
		choice = input("Y/N")
		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()	
		elif (choice is "Y") or (choice is "y"):
			player_lives = 5
			computer_lives = 5
			player = False 
			computer = choices[randint(0,2)]
		
	else:	
		player = False
		computer = choices[randint(0,2)]
 



	   	





