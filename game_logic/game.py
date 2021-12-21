

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
        pieces = [Rook, Bishop, Knight, Queen, King, Bishop, Knight, Rook]
        for col, piece in zip(range(8), pieces):
            pos = Position(0, col)
            self.board[pos] = piece(pos, White(), self.board)
        
        # Set frontline for white
        for col in range(8):
            pos = Position(1, col)
            self.board[pos] = Pawn(pos, White(), self.board)
            
        # Set backline for black
        pieces = [Rook, Bishop, Knight, Queen, King, Bishop, Knight, Rook]
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
    
    def capture(self, try_move):
        self.board[try_move] = None
        
    def capture_passant(self, try_move, piece_on_position, piece):
        if isinstance(piece, Pawn):
            passant_check, position = piece.check_passant(try_move)
            if passant_check:
                self.board[position] = None

    def board_move_check(self, piece, try_move):
        possible_moves_internal = piece.possible_moves() # Get possible moves without knowing anything about the boardstate.
        ## First check if occupied with a same-colored piece.
        possible_moves = Moves([])
        for move in possible_moves_internal:
            temp_piece = self.board[move]
            if not temp_piece == None:

                if temp_piece.team != piece.team:
                    possible_moves.append(move)
            else:
                possible_moves.append(move)
        if try_move in possible_moves:
            return True
        return False
    
    def board_move(self, piece, try_move):
    
        piece_on_position = self.board[try_move]
        
        self.capture_passant(try_move, piece_on_position, piece)
        
        if piece_on_position != None and piece_on_position.team != piece.team:
            self.capture(try_move)
        
        self.move_piece(piece, try_move)

    def event_handler(self, piece, try_move):
        """ Get a piece, and the proposed move -  Check move, and moves if possible. """
        if self.board_move_check(piece, try_move):
            self.board_move(piece, try_move)
            
    
    def __repr__(self):
        return f"Board with positions:\n{self.board}"
        