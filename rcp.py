#import random module
import random
#print the game rule
#below output will shows the rule for the games
print("Winning Rules for Rock,Paper, Scissor are: \n"
      + "Rock vs paper -> Paper wins \n"
      + "Rock vs scissor -> Rock wins \n"
      + "Paper vs scissor -> Scissor wins")

#to create a loop, item while become true depend user input

while True:
    
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor\n")

    #take input from user

    choice = int(input("Enter your choice :"))

    #using OR to indicate if any one ofthe condition is true
    #then, it will return True value

    #to control user input between 1 to 3 only 
    while choice > 3 or choice < 1:
        choice = int(input("Please enter a valid choice"))
    
        

    #looping through choice number until it correspond to the value
    if choice == 1:
            choice_name ="Rock"
    elif choice == 2:
        choice_name ="Paper"
    else: choice_name = "Scissor"

    #print user choice
    print("User choice is \n", choice_name)
    print("Now, it's computers turn....")

    #computer chooses random number between 1,2,3 using randint method
    #of random module
    comp_choice = random.randint(1, 3)

    #looping until comp_choice produce value
    #that equal to valid choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)


    #looping througn computer choice until it corresponds the value
    if comp_choice == 1:
        comp_choice_name = "rock"
    elif comp_choice == 2:
        comp_choice_name = "paper"
    else: comp_choice_name ="scissor"
    print("Computer choice is \n", comp_choice_name)

    #we need the results (win,draw)
    if choice == comp_choice:
        print("The result is DRAW", end="")
        result = "DRAW"
    #condition for winning
    #paper condition
    if choice == 1 and comp_choice ==2:
        print("paper wins =>", end ="")
        result= "paper"
    elif choice == 2 and comp_choice == 1:
        print("paper wins =>", end = "")
        result = "Paper"

    #rockcondition
    if choice == 1 and comp_choice == 3:
        print("rock wins =>", end ="")
        result= "rock"
    elif choice == 3 and comp_choice == 1:
        print("rock wins =>", end = "")
        result = "Rock"

    #scissorcondition
    if choice == 2 and comp_choice == 3:
        print("scissor wins =>", end ="")
        result= "scissor"
    elif choice == 2 and comp_choice == 3:
        print("scissor wins =>", end = "")
        result = "Scissor"

    #print eithercomputer or user winning
    #compare result either DRAW or WIN
    if result == "DRAW":
        print("<<<<<<<It's a TIE>>>>>>>")
    if result == "choice_name":
        print("<<<<<<<USER WIN!>>>>>>>>")
    else: 
        print("<<<<<<COMPUTER IS THE CHAMPS!>>>>>>")
        print(" Do you want to play again? (Y/N)")

    #decide to continue the game based on user input of yes or no
    ans = input().lower
    if ans == "N":
        break
        
    #this will break the loop
    #print thank you for playing
         
print("THANK YOU FOR PLAYING ROCK, PAPER, SCISSOR")




    