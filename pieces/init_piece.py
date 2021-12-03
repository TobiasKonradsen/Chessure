
from abc import ABC, abstractmethod
from game_logic.exceptions import IllegalMoveError


class InitPiece(ABC):
    def __init__(self, init_pos, team):
        self._pos = init_pos
        self._team = team
    
    @abstractmethod
    def possible_moves(self):
        raise NotImplementedError('This piece should not be able to move')
    
    
    def move(self, pos):
        if pos in self.possible_moves():
             self.set_position(pos)
        else:
            raise IllegalMoveError()
            
 
    def get_position(self):
         return self._pos
      
    def set_position(self, pos):
        self._pos = pos


