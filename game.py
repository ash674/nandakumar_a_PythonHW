from random import randint

choices = ["rock","paper","scissors"]

computer = choices[randint(0,2)]

# set up the game loop so that we dont have to restart all the time
player = False

while player == False:
    
	print("--------------------------------------------------")
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
	    else:
	     	print("You win!!!!",player,"smashes",computer,"\n")
	elif player.lower() == "paper":
	    if computer == "scissors":
	    	print("You lose !!",computer,"cuts",player,"\n")
	    else:
	     	print("You win!!!!",player,"covers",computer,"\n")
	elif player.lower() == "scissors":
	    if computer == "rock":
	    	print("You lose !!",computer,"smashes",player,"\n")
	    else:
	     	print("You win!!!!",player,"cuts",computer,"\n")

	else:
		print("Thats not a valid choice,try again")     	    	    	   	

	player = False
   	computer = choices[randint(0,2)]			

    			




	   	





