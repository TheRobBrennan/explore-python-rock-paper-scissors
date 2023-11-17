import unittest
from unittest.mock import patch
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

    @patch('random.choice')
    def test_get_computer_choice(self, mock_choice):
        mock_choice.return_value = 'rock'
        self.assertEqual(self.game.get_computer_choice(), 'rock')
        mock_choice.return_value = 'paper'
        self.assertEqual(self.game.get_computer_choice(), 'paper')
        mock_choice.return_value = 'scissors'
        self.assertEqual(self.game.get_computer_choice(), 'scissors')

if __name__ == '__main__':
    unittest.main()
