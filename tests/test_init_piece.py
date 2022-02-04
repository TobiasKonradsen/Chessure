
import unittest
from pieces.init_piece import InitPiece
from game_logic.position import Position
from game_logic.team import Team
from game_logic.exceptions import IllegalMoveError
from board.chessboard import BoardSize, ChessBoard

class FakeInitPiece(InitPiece):
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
    
    def possible_moves(self):
        raise NotImplementedError('This piece should not be able to move')
    


class TestInitPieces(unittest.TestCase):
    
    def setUp(self):
        self.position = Position()
        self.team = Team(1)
        self.board = ChessBoard(8, 8)
        self.piece = FakeInitPiece(self.position, self.team, self.board)
    
    def test_initialisation(self):
        """Test the constructor."""
        self.assertEqual(self.position, self.piece._pos)
        self.assertEqual(self.team, self.piece.team)

    def test_get_possible_moves(self):
        """Test the possible moves."""
        with self.assertRaises(NotImplementedError):
            self.piece.possible_moves()
    
    def test_get_position(self):
        """ Test for the getting the position of the piece"""
        self.assertEqual(self.position, self.piece.get_position())
        

    def test_move_piece(self):
        """ Test for the movement of the piece"""
        self.piece.possible_moves = lambda: []
            
        new_position = Position()
        self.piece.possible_moves = lambda: [new_position]
        self.piece.move(new_position)
        self.assertEqual(new_position, self.piece._pos)


if __name__ == "__main__":
    unittest.main()
    