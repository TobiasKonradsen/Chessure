
import unittest
from game_logic.position import Position
from game_logic.team import White, Black
from pieces.pieces import Pawn, King, Knight
from game_logic.moves import Moves
from board.chessboard import BoardSize


class TestPieces(unittest.TestCase):
    def setUp(self):
        self.boardsize = BoardSize(8, 8)

    def test_pawn(self):
        """ Test for the pawn piece """
        init_pos = Position(0, 0, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.boardsize)
        self.assertEqual(len(pawn.possible_moves()), len(Moves([])))

        init_pos = Position(4, 4, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.boardsize)
        #print(pawn.possible_moves())
        self.assertEqual(len(pawn.possible_moves()), 4)
        
        init_pos = Position(4, 4, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.boardsize)
        pawn.first_move = False
        self.assertEqual(len(pawn.possible_moves()), 3)
        

    def test_king(self):
        """ Test for the king piece """
        init_pos = Position(0, 0, self.boardsize)
        king = King(init_pos, Black(),  self.boardsize)

        self.assertEqual(len(king.possible_moves()), 3)

        init_pos = Position(4, 4, self.boardsize)
        king = King(init_pos, Black(),  self.boardsize)
        
        self.assertEqual(len(king.possible_moves()), 8)
        
    def test_knight(self):
        """ Test for the knight piece """
        init_pos = Position(0, 0, self.boardsize)
        knight = Knight(init_pos, Black(),  self.boardsize)
        self.assertEqual(len(knight.possible_moves()), 2)
        
        init_pos = Position(4, 4, self.boardsize)
        knight = Knight(init_pos, Black(),  self.boardsize)
        
        self.assertEqual(len(knight.possible_moves()), 8)
        
        


if __name__ == "__main__":
    unittest.main()
