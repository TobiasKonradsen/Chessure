

from board.chessboard import ChessBoard
from game_logic.position import Position
from pieces.pieces import Pawn, King, Knight, Rook, Bishop, Queen
from game_logic.team import White, Black
from game_logic.moves import Moves
from pieces.init_piece import InitPiece

class Game:
    def __init__(self, gametype):
        self.board = ChessBoard(8,8) # 8, 8 game
        for col in range(8):
            for row in range(8):
                pos = Position(row, col)
                self.board[pos] = None
        # Set backline for white
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece in zip(range(8), pieces):
            pos = Position(0, col)
            self.board[pos] = piece(pos, White(), self.board)
        
        # Set frontline for white
        for col in range(8):
            pos = Position(1, col)
            self.board[pos] = Pawn(pos, White(), self.board)
            
        # Set backline for black
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece in zip(range(8), pieces):
            pos = Position(7, col)
            self.board[pos] = piece(pos, Black(), self.board)
        
        # Set frontline for white
        for col in range(0, 8):
            pos = Position(6, col)
            self.board[pos] = Pawn(pos, Black(), self.board) 
    
    def move_piece(self, piece, try_move):
        
        prevpos = piece.get_position()
        piece.move(try_move)
        self.board[prevpos] = None
        self.board[try_move] = piece
    
    def capture(self, try_move, piece_on_position, piece):
        
        if piece_on_position != None and piece_on_position.team != piece.team:
            self.board[try_move] = None
        
    def capture_passant(self, try_move, piece_on_position, piece):
        if isinstance(piece, Pawn):
            passant_check, position = piece.check_passant(try_move)
            if passant_check:
                self.board[position] = None
                
    def castling(self, try_move, piece):
        if isinstance(piece, King):
            castle_check, castle, direction_pos = piece.castling_check(try_move)
            if castle_check:
                self.move_piece(castle, try_move + direction_pos)

    def board_move_check(self, try_move, piece):
        ## First check if occupied with a same-colored piece.
        possible_moves = piece.possible_moves_board()
        if try_move in possible_moves:
            return True
        return False
    def check_check(self):
        """Check if the one of the players are in check"""
        all_moves_white = set()
        all_moves_black = set()
        for piece in self.board:
            if piece.team == White():
                all_moves_white.update(piece.possible_moves_board())
                if isinstance(piece, King):
                    white_king = piece
            if piece.team == Black():
                all_moves_black.update(piece.possible_moves_board())
                if isinstance(piece, King):
                    black_king = piece
        if black_king.get_position() in all_moves_white:
            print("Black is check")
        if white_king.get_position() in all_moves_black:
            print("White is check")
    def board_move(self, try_move, piece):
    
        piece_on_position = self.board[try_move]
        
        self.capture_passant(try_move, piece_on_position, piece)
        
        self.castling(try_move, piece)

        self.capture(try_move, piece_on_position, piece)
        
        self.move_piece(piece, try_move)
        
        #self.check_check()
    def event_handler(self, try_move, piece):
        """ Get a piece, and the proposed move -  Check move, and moves if possible. """
        if self.board_move_check(try_move, piece):
            self.board_move(try_move, piece)
            
    
    def __repr__(self):
        return f"Board with positions:\n{self.board}"
        