import sys
import os

# Add the src directory to sys.path to allow for absolute imports
src_dir = os.path.dirname(os.path.abspath(__file__))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from game import RockPaperScissors

def main():
    game = RockPaperScissors()
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("Choose rock, paper, or scissors (or 'q' to quit): ", end='', flush=True)
        player_choice = input().lower()        

        if player_choice == 'q':
            break
        if player_choice not in game.choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = game.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = game.play(player_choice, computer_choice)
        if result == "Player wins":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1

        print(result)
        print(f"Score - Player: {player_score}, Computer: {computer_score}")

    print("Game Over")
    print(f"\nFinal Score\n-----------\nPlayer  : {player_score}\nComputer: {computer_score}\n")

if __name__ == "__main__":
    main()
