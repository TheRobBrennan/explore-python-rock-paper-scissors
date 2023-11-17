# Welcome

The goal of this project is to scaffold a very quick and dirty Python project using suggested best practices from ChatGPT 4:

```sh
Welcome to Rock, Paper, Scissors!
Choose rock, paper, or scissors (or 'q' to quit): rock
Computer chose: rock
Draw
Score - Player: 0, Computer: 0
Choose rock, paper, or scissors (or 'q' to quit): paper
Computer chose: rock
Player wins
Score - Player: 1, Computer: 0
Choose rock, paper, or scissors (or 'q' to quit): paper
Computer chose: scissors
Computer wins
Score - Player: 1, Computer: 1
Choose rock, paper, or scissors (or 'q' to quit): rock
Computer chose: rock
Draw
Score - Player: 1, Computer: 1
Choose rock, paper, or scissors (or 'q' to quit): scissors
Computer chose: paper
Player wins
Score - Player: 2, Computer: 1
Choose rock, paper, or scissors (or 'q' to quit): q
Game Over

Final Score
-----------
Player  : 2
Computer: 1
```

## Getting started

### Prerequisites

Please make sure that you have the following installed on your development environment:

- [Node.js](https://nodejs.org/en)
- [Python](https://www.python.org)

This code base was initially developed and tested on:

- 2021 14" MacBook Pro
  - Apple M1 Max
  - 64 GB memory
  - 2 TB SSD
  - macOS Sonoma `14.1.1`
    - Node.js `v20.9.0`
    - npm `10.1.0`
    - Python `3.11.1`

### Scripts

This project includes several scripts to get you up and running with your local development environment using `npm` (e.g. `npm run setup`):

- `setup`

  - This script checks to see if a Python virtual environment has been created at `.venv` and installs dependencies from [requirements.txt](./requirements.txt)

- `start`

  - This script uses the Python virtual environment at `.venv` to run the application locally

- `test`

  - This script uses the Python virtual environment at `.venv` and runs the unit tests for our shot chart application

- `test:coverage`

  - This script uses the Python virtual environment at `.venv`, runs the unit tests for our shot chart application, and generates an HTML coverage report at [./htmlcov/index.html](./htmlcov/index.html) that will automatically open in the default web browser on macOS.

- `destroy`
  - This script removes the Python virtual environment at `.venv`

## The ChatGPT 4 Challenge

This project aims to see what advice ChatGPT 4 would give regarding creating and setting up a Python project using best practices with a simple game.

### Let's go

The initial prompt I supplied to ChatGPT 4 was:

```sh
Please write me a Rock, Paper, Scissors game in Python using best practices in Python development including:

- Project structure
- Names and locations of files
- Unit tests to verify functionality with 100% coverage
```

The response from ChatGPT 4:

````sh
Creating a Rock, Paper, Scissors game in Python with best practices involves several steps. I'll outline the project structure, file organization, and provide sample code along with unit tests to ensure 100% coverage.

### Project Structure

1. **Project Root Directory (e.g., `rock_paper_scissors`)**
   - `src/`: Contains the main Python code.
   - `tests/`: Contains unit tests.
   - `requirements.txt`: Lists Python dependencies (if any).
   - `README.md`: Project description and instructions.

2. **Source Directory (`src/`)**
   - `game.py`: Contains the main game logic.
   - `__init__.py`: An empty file to make `src` a Python package.

3. **Tests Directory (`tests/`)**
   - `test_game.py`: Contains unit tests for `game.py`.
   - `__init__.py`: An empty file to make `tests` a Python package.

### Sample Code

#### `src/game.py`

```python
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
        import random
        return random.choice(self.choices)
````

#### `tests/test_game.py`

```python
import unittest
from src.game import RockPaperScissors

class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.game = RockPaperScissors()

    def test_draw(self):
        for choice in self.game.choices:
            self.assertEqual(self.game.play(choice, choice), "Draw")

    def test_invalid_choice(self):
        with self.assertRaises(ValueError):
            self.game.play('invalid_choice', 'rock')

    def test_player_wins(self):
        self.assertEqual(self.game.play('rock', 'scissors'), "Player wins")
        self.assertEqual(self.game.play('paper', 'rock'), "Player wins")
        self.assertEqual(self.game.play('scissors', 'paper'), "Player wins")

    def test_computer_wins(self):
        self.assertEqual(self.game.play('rock', 'paper'), "Computer wins")
        self.assertEqual(self.game.play('paper', 'scissors'), "Computer wins")
        self.assertEqual(self.game.play('scissors', 'rock'), "Computer wins")

if __name__ == '__main__':
    unittest.main()
```

### Running the Tests

To run the tests and ensure 100% coverage, you can use a tool like `coverage.py`. Install it using `pip install coverage` and then run:

```bash
coverage run -m unittest discover -s tests
coverage report -m
```

This will execute all tests and report the coverage. The provided tests should cover all branches of the `play` method in `game.py`.

### Additional Notes

- You may want to add more sophisticated logic or features, like a user interface or a way to keep score.
- Ensure that your `README.md` includes instructions on how to run the game and the tests.
- Depending on the complexity of the project, you might want to set up a virtual environment and specify dependencies in `requirements.txt`. For this simple project, it's not strictly necessary.

```

```
