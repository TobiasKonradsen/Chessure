import unittest
from board.chessboard import BoardSize, ChessBoard


class TestBoardSize(unittest.TestCase):
    """Test the functionality of the board size."""

    def setUp(self):
        self.rows = 4
        self.cols = 4
        self.boardsize = BoardSize(self.rows, self.cols)

    def test_initialisation(self):
        """Test the constructor."""
        self.assertEqual(self.boardsize.rows, self.rows)
        self.assertEqual(self.boardsize.cols, self.cols)
        self.assertEqual(self.boardsize, self.rows*self.cols)


class TestChessBoard(unittest.TestCase):
    """Test the functionality of the chessboard."""

    def setUp(self):
        self.rows = 4
        self.cols = 4
        self.chessboard = ChessBoard(self.rows, self.cols)

    def test_initialisation(self):
        """Test the constructor."""
        self.assertIsInstance(self.chessboard, list)
        self.assertEqual(len(self.chessboard), self.rows*self.cols)

    def test_indexing(self):
        """Test whether we can index the board correctly."""
        r, c, = 2, 3
        self.assertEqual(self.chessboard(r, c), r*self.cols + c)


if __name__ == "__main__":
    unittest.main()
