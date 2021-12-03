
import unittest
from pieces.init_piece import InitPiece
from game_logic.position import Position
from game_logic.team import Team
from game_logic.exceptions import IllegalMoveError


class FakeInitPiece(InitPiece):
    def __init__(self, init_pos, team):
        super().__init__(init_pos, team)
    
    def possible_moves(self):
        raise NotImplementedError('This piece should not be able to move')
    


class TestInitPieces(unittest.TestCase):
    
    def setUp(self):
        self.position = Position()
        self.team = Team()
        self.piece = FakeInitPiece(self.position, self.team)
    
    def test_initialisation(self):
        """Test the constructor."""
        self.assertEqual(self.position, self.piece._pos)
        self.assertEqual(self.team, self.piece._team)

    def test_get_possible_moves(self):
        """Test the possible moves."""
        with self.assertRaises(NotImplementedError):
            self.piece.possible_moves()
    
    def test_get_position(self):
        """ Test for the getting the position of the piece"""
        self.assertEqual(self.position, self.piece.get_position())
        
    def test_set_position(self):
        """ Test for the setting the position of the piece"""
        new_position = Position()
        self.piece.set_position(new_position)
        self.assertEqual(new_position, self.piece._pos)
    
    def test_move_piece(self):
        """ Test for the movement of the piece"""
        with self.assertRaises(IllegalMoveError):
            self.piece.move(Position())


if __name__ == "__main__":
    unittest.main()
    