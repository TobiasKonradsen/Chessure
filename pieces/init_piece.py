
from abc import ABC, abstractmethod
from game_logic.exceptions import IllegalMoveError
from game_logic.moves import Moves


class InitPiece(ABC):
    def __init__(self, init_pos, team, board):
        self._pos = init_pos
        self.team = team
        self.boardsize  = board.size
        self.name = 'Init piece'
        self.acii = 'I'
        self.board = board
    
    @abstractmethod
    def possible_moves(self):
        raise NotImplementedError('This piece should not be able to move')
    
    def isLegal(self, try_moves):
        moves = Moves([])                         
        for move in try_moves:
            if move.isLegal():
                moves.append(move)
        return moves
    
    
    def check_not_empty(self, final_position):
        piece_at_pos = self.board[final_position]
        return not ((piece_at_pos == None) or (type(piece_at_pos) == int))
        
    
    def __repr__(self):
        return f"{self.team} {self.name} at {self._pos}"
    
    def get_position(self):
        return self._pos

        
    def move(self, pos):
        ## Checks is done at the game-level
        self._pos = pos

    

