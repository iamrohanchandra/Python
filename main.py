import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(options)
    
    if player_choice not in options:
        return {"player": player_choice, "computer": computer_choice, "error": "Invalid input"}
    
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        return "You win!" if computer == "scissors" else "You lose."
    elif player == "scissors":
        return "You win!" if computer == "paper" else "You lose."
    elif player == "paper":
        return "You win!" if computer == "rock" else "You lose."

choices = get_choices()

if "error" in choices:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    result = check_win(choices["player"], choices["computer"])
    print(result)
