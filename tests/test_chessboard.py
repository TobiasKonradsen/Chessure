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
class MockClass:
    acii = 'M'
    
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
    
    def test_iterator(self):
        r, c = 2, 3
        pos = Position(r, c, self.chessboard.size)
        self.chessboard[pos] = MockClass()
        stufflist = []
        for stuff in self.chessboard:
            stufflist.append(stuff)
        self.assertEqual(len(stufflist), 1)
        self.assertTrue(isinstance(stuff, MockClass))

    def test_internal_bookkeeping(self):
        r, c = 2, 3
        pos = Position(r, c, self.chessboard.size)
        self.chessboard[pos] = MockClass()
        
        self.assertEqual(len(self.chessboard.piece_positions),1)
        
        self.chessboard[pos] = None
        
        self.assertEqual(len(self.chessboard.piece_positions),0)
    def test_internal_bookkeeping_ver2(self):
        r, c = 2, 3
        pos = Position(r, c, self.chessboard.size)
        self.chessboard[pos] = MockClass()
        
        r, c = 3, 3
        pos1 = Position(r, c, self.chessboard.size)
        self.chessboard[pos1] = MockClass()
        
        self.assertEqual(len(self.chessboard.piece_positions),2)
        
        self.chessboard[pos1] = None
        self.chessboard[pos1] = None ## Test already setting None to None Value
        
        self.assertEqual(len(self.chessboard.piece_positions),1) 
        
        self.chessboard[pos] = None
        self.assertEqual(len(self.chessboard.piece_positions),0)
        
        


if __name__ == "__main__":
    unittest.main()
