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
