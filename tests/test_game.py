
import unittest
from game_logic.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(1) ## 7, 7 as the chessboard is zero indexed
    def test_print(self):
        print(self.game)

    
        
        


if __name__ == "__main__":
    unittest.main()
