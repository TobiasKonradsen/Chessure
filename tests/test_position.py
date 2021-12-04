

import unittest
from game_logic.position import Position
from game_logic.exceptions import IllegalMoveError
from board.chessboard import BoardSize


class TestPosition(unittest.TestCase):

    def setUp(self):
        self.boardsize = BoardSize(8, 8)

    def test_position_add(self):
        """Test the possible moves."""
        pos = Position(0, 0, self.boardsize) + Position(1, 1, self.boardsize)
        self.assertEqual(pos.row, 1)
        self.assertEqual(pos.col, 1)

    def test_position_legal(self):
        """Test the possible moves."""
        pos = Position(0, 0, self.boardsize) + Position(1, 1, self.boardsize)
        self.assertTrue(pos.isLegal())

        pos = Position(0, 0, self.boardsize) + Position(-1, -1, self.boardsize)
        self.assertFalse(pos.isLegal())


if __name__ == "__main__":
    unittest.main()
