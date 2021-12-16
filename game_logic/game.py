

from board.chessboard import ChessBoard
from game_logic.position import Position
from pieces.pieces import Pawn, King, Knight, Rook, Bishop, Queen
from game_logic.team import White, Black

class Game:
    def __init__(self, gametype):
        self.board = ChessBoard(8,8) # 8, 8 game
        
        # Set backline for white
        pieces = [Rook, Bishop, Knight, Queen, King, Bishop, Knight, Rook]
        for col, piece in zip(range(8), pieces):
            pos = Position(0, col)
            self.board[pos] = piece(pos, White(), self.board.size)
        
        # Set frontline for white
        for col in range(8):
            pos = Position(1, col)
            self.board[pos] = Pawn(pos, White(), self.board.size)
            
        # Set backline for black
        pieces = [Rook, Bishop, Knight, Queen, King, Bishop, Knight, Rook]
        for col, piece in zip(range(8), pieces):
            pos = Position(7, col)
            self.board[pos] = piece(pos, Black(), self.board.size)
        
        # Set frontline for white
        for col in range(0, 8):
            pos = Position(6, col)
            self.board[pos] = Pawn(pos, Black(), self.board.size) 
    
    def player_turn(self):
        
    
    
    def __repr__(self):
        return f"Board with positions {self.board}"
        