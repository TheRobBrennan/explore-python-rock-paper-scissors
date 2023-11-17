import unittest
from unittest.mock import patch
from io import StringIO
import src.cli
import runpy

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

    def test_main_execution(self):
        # Prepare to capture output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Mock inputs to exit immediately
            with patch('builtins.input', return_value='q'):
                # Execute the CLI script as if it were being run directly
                runpy.run_module('src.cli', run_name="__main__")

                output = mock_stdout.getvalue()
                # Assert that the script executed (e.g., by checking for the welcome message)
                self.assertIn("Welcome to Rock, Paper, Scissors!", output)

if __name__ == '__main__':
    unittest.main()
