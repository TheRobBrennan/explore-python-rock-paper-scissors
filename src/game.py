import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def play(self, player_choice, computer_choice):
        if player_choice not in self.choices:
            raise ValueError("Invalid choice")
        if player_choice == computer_choice:
            return "Draw"
        if (player_choice == "rock" and computer_choice == "scissors") or \
           (player_choice == "paper" and computer_choice == "rock") or \
           (player_choice == "scissors" and computer_choice == "paper"):
            return "Player wins"
        return "Computer wins"

    def get_computer_choice(self):
        return random.choice(self.choices)
