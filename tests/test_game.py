
import unittest
from game_logic.game import Game
from game_logic.position import Position

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game(1)
        self.board = self.game.board
        
    def test_print(self):
        pass

    def test_board_iterator(self):
        self.assertEqual(len(self.board.piece_positions), 8*4)

    def test_passant(self):
        pos = Position(1,1, self.board.size)
        pawn_white = self.board[pos]
        new_pos = Position(3,1, self.board.size)
        self.game.event_handler(new_pos, pawn_white)
        
        pos = Position(6,2, self.board.size)
        pawn_black = self.board[pos]
        new_pos_black = Position(4,2, self.board.size)        
        self.game.event_handler(new_pos_black, pawn_black)


        pos = Position(1, 2, self.board.size)
        pawn_white_sec = self.board[pos]

        new_pos_sec = Position(2,2, self.board.size)
        self.game.event_handler(new_pos_sec, pawn_white_sec)

        
        
        self.game.event_handler(Position(3,2, self.board.size), pawn_black)
        
        pos = Position(1, 0, self.board.size)
        pawn_white_sec = self.board[pos]
        
        new_pos_sec = Position(2,0, self.board.size)
        self.game.event_handler(new_pos_sec, pawn_white_sec)
        
        
        self.game.event_handler(Position(2,1, self.board.size), pawn_black)
        pos = Position(1,1, self.board.size)
        pawn_destroyed = self.board[pos]
        self.assertTrue(pawn_destroyed == None)
    
    def test_getboardstate(self):
        """Get the current boardstate"""
        print(self.game.get_board())
        
        
    
        
        


if __name__ == "__main__":
    unittest.main()
