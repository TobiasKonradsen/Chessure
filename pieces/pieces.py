
from pieces.init_piece import InitPiece
from game_logic.position import Position
from game_logic.moves import Moves


class Pawn(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)
        
        self.first_move = True
        
    def possible_moves(self):
        
        moves = Moves([])
        
        p1 = self._pos + Position(self.team*1, 0, self.boardsize)
        p2 = self._pos + Position(self.team*1, 1, self.boardsize)
        p3 = self._pos + Position(self.team*1, -1, self.boardsize)

        try_moves = [p1, p2, p3]
        
        if self.first_move:
            try_moves.append(self._pos + Position(self.team*2, 0, self.boardsize))
            self.first_move = False
        
        
        for move in try_moves:
            if move.isLegal():
                moves.append(move)

        return moves

class Knight(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)

    def possible_moves(self):
        try_moves = Moves([])
        for sign in [-1, 1]:
            try_moves.append(self._pos + Position(sign*1, sign*2, self.boardsize))
            try_moves.append(self._pos + Position(sign*2, sign*1, self.boardsize))
            try_moves.append(self._pos + Position(-sign*1, sign*2, self.boardsize))
            try_moves.append(self._pos + Position(-sign*2, sign*1, self.boardsize))

        moves = Moves([])                         
        for move in try_moves:
            if move.isLegal():
                moves.append(move)
                
        return moves




class King(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)

    def possible_moves(self):
        moves = Moves([])
        p1 = self._pos + Position(-1, -1, self.boardsize)
        p2 = self._pos + Position(-1, 0, self.boardsize)
        p3 = self._pos + Position(-1, 1, self.boardsize)
        p4 = self._pos + Position(0, 1, self.boardsize)
        p5 = self._pos + Position(0, -1, self.boardsize)
        p6 = self._pos + Position(1, 1, self.boardsize)
        p7 = self._pos + Position(1, 0, self.boardsize)
        p8 = self._pos + Position(1, -1, self.boardsize)

        try_moves = [p1, p2, p3, p4, p5, p6, p7, p8]
        for move in try_moves:
            if move.isLegal():
                moves.append(move)

        return moves

