import unittest
from board.chessboard import BoardSize, ChessBoard
from game_logic.position import Position


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
        pos = Position(r, c, self.chessboard.size)
        self.assertEqual(self.chessboard[pos], r*self.cols + c)
    
    def test_setting_values(self):
        """ Test the setting implementation of the board """
        r, c = 2, 3
        pos = Position(r, c, self.chessboard.size)
        self.chessboard[pos] = None
        self.assertEqual(self.chessboard[pos], None)
        
        self.chessboard[pos] = [None]*10
        self.assertEqual(self.chessboard[pos], [None]*10)
         


if __name__ == "__main__":
    unittest.main()
