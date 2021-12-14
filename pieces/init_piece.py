
from abc import ABC, abstractmethod
from game_logic.exceptions import IllegalMoveError
from game_logic.moves import Moves


class InitPiece(ABC):
    def __init__(self, init_pos, team, boardsize):
        self._pos = init_pos
        self.team = team
        self.boardsize  = boardsize
    
    @abstractmethod
    def possible_moves(self):
        raise NotImplementedError('This piece should not be able to move')
    
    def isLegal(self, try_moves):
        moves = Moves([])                         
        for move in try_moves:
            if move.isLegal():
                moves.append(move)
        return moves
    
    def move(self, pos):
        if pos in self.possible_moves():
             self.set_position(pos)
        else:
            raise IllegalMoveError()
            
 
    def get_position(self):
         return self._pos
      
    def set_position(self, pos):
        self._pos = pos


