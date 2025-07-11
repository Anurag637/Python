# Creating A game called Stone Paper Scissor 
# stone
# Paper
# Scissor

import random

L = ["stone", "paper", "scissor"]
user_input = input("Enter stone, paper or scissor: ").lower()
if user_input not in L:
    print("Invalid input! Please enter stone, paper or scissor.")
else:
    computer_input = random.choice(L)
    print("Computer chose:", computer_input)
    
    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "stone" and computer_input == "scissor") or \
         (user_input == "paper" and computer_input == "stone") or \
         (user_input == "scissor" and computer_input == "paper"):
        print("You win!")
    else:
        print("You lose!")