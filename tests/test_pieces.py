
import unittest
from game_logic.position import Position
from game_logic.team import White, Black
from pieces.pieces import Pawn, King, Knight, Rook, Bishop, Queen
from game_logic.moves import Moves
from board.chessboard import BoardSize
from board.chessboard import ChessBoard


class TestPieces(unittest.TestCase):
    def setUp(self):
        self.board = ChessBoard(8,8)
        self.boardsize = self.board.size
    def test_pawn(self):
        """ Test for the pawn piece """
        
        init_pos = Position(0, 0, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.board)
        self.assertEqual(len(pawn.possible_moves()), len(Moves([])))

        init_pos = Position(4, 4, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.board)
        
        self.assertEqual(len(pawn.possible_moves()), 2)
        
        init_pos = Position(4, 4, self.boardsize)
        pawn = Pawn(init_pos, Black(),  self.board)
        pawn.first_move = False
        self.assertEqual(len(pawn.possible_moves()), 1)
        

    def test_king(self):
        """ Test for the king piece """
        init_pos = Position(0, 0, self.boardsize)
        king = King(init_pos, Black(),  self.board)

        self.assertEqual(len(king.possible_moves()), 3)

        init_pos = Position(4, 4, self.boardsize)
        king = King(init_pos, Black(),  self.board)
        
        self.assertEqual(len(king.possible_moves()), 8)
        
    def test_knight(self):
        """ Test for the knight piece """
        init_pos = Position(0, 0, self.boardsize)
        knight = Knight(init_pos, Black(),  self.board)
        self.assertEqual(len(knight.possible_moves()), 2)
        
        init_pos = Position(4, 4, self.boardsize)
        knight = Knight(init_pos, Black(),  self.board)
        
        self.assertEqual(len(knight.possible_moves()), 8)
    
    def test_rook(self):
        """ Test for the rook piece """
        init_pos = Position(0, 0, self.boardsize)
        rook = Rook(init_pos, Black(),  self.board)
        self.assertEqual(len(rook.possible_moves()), 7*2)
        
        init_pos = Position(4, 4, self.boardsize)
        rook = Rook(init_pos, Black(),  self.board)
        
        self.assertEqual(len(rook.possible_moves()), 7*2)
    
    
    def test_bishop(self):
        """ Test for the bishop piece """
        init_pos = Position(0, 0, self.boardsize)
        bishop = Bishop(init_pos, Black(),  self.board)

        self.assertEqual(len(bishop.possible_moves()), 7)
        
        init_pos = Position(4, 4, self.boardsize)
        bishop = Bishop(init_pos, Black(),  self.board)

        self.assertEqual(len(bishop.possible_moves()), 6+7)
        
    def test_queen(self):
        """ Test for the knight piece """
        init_pos = Position(0, 0, self.boardsize)
        queen = Queen(init_pos, Black(),  self.board)
        self.assertEqual(len(queen.possible_moves()), 7 + 7*2)
        
        init_pos = Position(4, 4, self.boardsize)
        queen = Queen(init_pos, Black(),  self.board)
        
        self.assertEqual(len(queen.possible_moves()), 6+7 + 7*2)
        
    def test_queen_move_in_possible_moves(self):
        init_pos = Position(4, 4, self.boardsize)
        queen = Queen(init_pos, Black(),  self.board)
        move = Position(5, 5, self.boardsize)
        self.assertTrue(move in queen.possible_moves())
        


if __name__ == "__main__":
    unittest.main()
