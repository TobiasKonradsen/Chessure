

import unittest
from game_logic.position import Position
from game_logic.team import White, Black
from pieces.pieces import Pawn, King
from game_logic.moves import Moves
from board.chessboard import BoardSize


class TestPieces(unittest.TestCase):
    def setUp(self):
        self.boardsize = BoardSize(8, 8)

    def test_get_possible_moves_pawn(self):
        """Test the possible moves."""
        init_pos = Position(0, 0, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.boardsize)
        self.assertEqual(pawn.possible_moves(), Moves())

        init_pos = Position(4, 4, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.boardsize)
        self.assertEqual(len(pawn.possible_moves()), 3)

    def test_get_possible_moves_king(self):
        """Test the possible moves."""
        init_pos = Position(0, 0, self.boardsize)
        king = King(init_pos, Black(),  self.boardsize)
        pos_moves = Moves([
            Position(0, 1, self.boardsize),
            Position(1, 1, self.boardsize),
            Position(1, 0, self.boardsize)])
        self.assertEqual(len(king.possible_moves()), len(pos_moves))

        init_pos = Position(4, 4, self.boardsize)
        pawn = King(init_pos, Black(),  self.boardsize)
        self.assertEqual(len(pawn.possible_moves()), 8)


if __name__ == "__main__":
    unittest.main()
