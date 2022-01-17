
import unittest
from game_logic.game import Game
from game_logic.position import Position
import copy
class TestEvaluate(unittest.TestCase):
    
    def setUp(self):
        self.game = Game(1)
        self.board = self.game.board
        

    def test_totalnumberofmoves(self):
        self.count = 0
        for piece in self.board:
            possible_moves = piece.possible_moves_board()
            for moves in possible_moves:
                temp_game.board_move(try_move, piece)
                self.count += 1
        self.assertEqual(self.count,40)

        
        


if __name__ == "__main__":
    unittest.main()
