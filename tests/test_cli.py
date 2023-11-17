import unittest
from unittest.mock import patch
from io import StringIO
import src.cli

class TestCLI(unittest.TestCase):
    def test_game_flow(self):
        user_inputs = ['rock', 'invalid', 'paper', 'scissors', 'q']
        expected_outputs = [
            "Welcome to Rock, Paper, Scissors!",
            "Invalid choice. Please choose again.",
            "Game Over"
        ]

        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                src.cli.main()

                output = mock_stdout.getvalue()
                # Check for the presence of expected outputs
                for expected_output in expected_outputs:
                    self.assertIn(expected_output, output)
                # Check the game prompts for inputs
                self.assertEqual(output.count("Choose rock, paper, or scissors (or 'q' to quit): "), 5)

if __name__ == '__main__':
    unittest.main()
