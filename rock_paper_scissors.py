import random


def login_account():
	username = input("Enter your username: ")                      #input login details
	password = input("Enter your password: ")
	
	file = open("Login.txt","r")
	data=file.read()
	if(username in data and password in data):                     #verifying login details
	    print("Successful login")
	    print()
	else:
	    print('Incorrect')
	    exit()

def create_account():

	username=input("Please enter a username: ")                       #input account details
	password=input("Create password: ")
	file = open("Login.txt","a")
	file.write (username)
	file.write (" , ")
	file.write (password)                                            #writing in database
	file.write("\n")
	file.close()
	print ("Your details have been saved. Please log in to continue playing")
	login_account()


print("---------------------------------------------")
print ("To begin, enter the following information: ")
print("---------------------------------------------")

ch=input("choose login or signup: ")
if (ch=="login"):
	login_account()
elif(ch=="signup"):
	create_account()
else:
	print("Enter correct choice")
	exit()
	

print ("Access Granted")
print("---------------------------------------------")
print("**********    ***********    ************")
print("*        *    *         *    *")
print("*        *    *         *    *")
print("**********    *         *    *")
print("**            ***********    ************")
print("* *	     *                         *")
print("*  *          *                         *")
print("*   *         *                         *")
print("*     *OCK    *APER          ************CISSORS")
print("----------------------------------------------")
print("---------------------------------------------")
print("1. To see a list of rules...type *rules*")
print("---------------------------------------------")
print("2. To play the game....type *start*")
print("---------------------------------------------")
print("3. At any point type *exit* to leave the game")
print("---------------------------------------------")
print("CAN YOU BEAT THE COMPUTER...?")
print("Good luck..!!!")
print()

def game_rules():
	print("Rules of the game are:")
	print("---------------------------------------------")
	print("Life rules: ")
	print("    1. If you win..you get an extra life")
	print("    2. If you lose..you lose a life")
	print("    3. If you draw... the lives stay the same")
	print("    4. The computer has lives as well")
	print("    5. To check number of remaining lives at any point in the game, type *check*") 
	print("---------------------------------------------")
	print("Make sure you don't use any CAPITAL while entering your choice")
	print("---------------------------------------------")	


def start_game():

	print()
	user_lives=5
	comp_lives=5
	avl_list=["rock","paper","scissors"]
	
	def display():                              #creating function within a function
		print()
		print("GAME OVER")
		print("FINAL RESULT")
		print("your score: ",user_lives)
		print("computer score: ",comp_lives)
		if(user_lives > comp_lives):
			print("YOU WON..!!")
		elif(user_lives==comp_lives):
			print("It's a TIE...!!")
		elif(user_lives < comp_lives):
			print("YOU LOSE....Better luck next time..!!")               #display function ended
		print()


	while(user_lives != 0 or comp_lives != 0):                     

		choice2=input("rock,paper or scissors..??")
		catch=random.choice(avl_list)

		if(catch==choice2):	
			print("you drew")

		elif(choice2=="rock" and catch=="paper"):
			print("you lose")
			user_lives=user_lives-1
			comp_lives=comp_lives+1

		elif(choice2=="rock" and catch=="scissors"):
			print("you won")
			user_lives=user_lives+1
			comp_lives=comp_lives-1

		elif(choice2=="paper" and catch=="rock"):
			print("you won")
			user_lives=user_lives+1
			comp_lives=comp_lives-1

		elif(choice2=="paper" and catch=="scissors"):
			print("you lose")
			user_lives=user_lives-1
			comp_lives=comp_lives+1

		elif(choice2=="scissors" and catch=="rock"):
			print("you lose")
			user_lives=user_lives-1
			comp_lives=comp_lives+1

		elif(choice2=="scissors" and catch=="paper"):
			print("you won")
			user_lives=user_lives+1
			comp_lives=comp_lives-1

		elif(choice2=="exit"):
			print()
			display()
			exit()
		
		elif(choice2=="check"):
			print ("user lives = ",user_lives)
			print("computer lives = ",comp_lives)

		else:
			print("Enter valid choice")

		if(user_lives==0 or comp_lives==0):
			display()
			break



choice=input("Enter your choice: ")
if(choice== "rules"):
	game_rules()
	pc=input("Do you want to start playing? Type yes/no ")
	if(pc=="yes"):
		start_game()
	elif(pc=="no"):
		exit()
	
elif(choice=="start"):
	start_game()		
	
elif(choice=="exit"):
	exit()
else:
	print("INVALID CHOICE")
