# We will write a rock paper scissors game in class - Complete it in this file
import random

player_choice="rock"
computer_choice="paper"
#Create a function that gets the choices
def get_choices():
    options=["Rock","Paper","Scissors"]
    player_choice=input("Enter a choice (Rock, Paper, or Scissors):")
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}

    return choices

#Function to check for a winning
def check_win(player,computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player==computer:
        return "Its a tie"
    elif player=="rock":
        if computer=="scissors":
            return "Rock beats scissors, You Win!"
    else:
        return "Paper beats rock, You Lose :("

choices=get_choices()
print(choices)
result=check_win(choices["player"],choices["computer"])
print(result)