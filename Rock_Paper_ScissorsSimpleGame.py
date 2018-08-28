#let's write a game. I used imported random because for single user playing with a computer.

import random

print("PLAY WITH BELOW INPUTS BY TYPING THEM. GOOD LUCK!")
print("rock...")
print("paper...")
print("scissors...")

player = input("Player, make your move: ").lower() #lowe() for case sensitivity
#print("****NO CHEATING!\n" * 40) #it will print this on window to avoid player2 from seeing player1's move, This with last code
#player2 = input("Player2, make your move: ") for code 2

    # Code 1 starts here
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
elif rand_num == 2:
    computer = "scissors"
print(f"Computer plays: {computer}")
    
if player == computer:
    print("It's a tie")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    #elif computer == "paper": 
    else: #it's totally cool to use the above line no offense
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    #elif computer == "scissors":
    else:
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    #elif computer == "rock":
    else:
        print("computer wins!")
else:
    print("Please enter a valid move!")
    
    #The above gaming code in a different common way

#if player1 == "rock" and player2 == "scissors":
#    print("player1 wins!")
#elif player1 == "rock" and player2 == "paper":
#    print("player2 wins!")
#elif player1 == "paper" and player2 == "rock":
#    print("player1 wins!")
#elif player1 == "paper" and player2 == "scissors":
#    print("player2 wins!")
#elif player1 == "scissors" and player2 == "rock":
#    print("player2 wins")
#elif player1 == "scossors" and player2 == "paper":
#    print("player1 wins!")
#elif player1 == player2:
#    print("It's a tie")
#else:
#    print("something went wrong play again!")
