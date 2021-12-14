
from pieces.init_piece import InitPiece
from game_logic.position import Position
from game_logic.moves import Moves


class Pawn(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)
        
        self.first_move = True
        
    def possible_moves(self):
        

        try_moves = Moves([])        

        try_moves.append(self._pos + Position(self.team*1, 0, self.boardsize))
        
        try_moves.append(self._pos + Position(self.team*1, 1, self.boardsize))
        
        try_moves.append(self._pos + Position(self.team*1, -1, self.boardsize))

        
        if self.first_move:
            try_moves.append(self._pos + Position(self.team*2, 0, self.boardsize))
            self.first_move = False
        
        
        moves = self.isLegal(try_moves)


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

        moves = self.isLegal(try_moves)

                
        return moves


class Rook(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)
        
    def possible_moves(self):
        try_moves = Moves([])
        for i in range(1, self.boardsize):
            try_moves.append(self._pos + Position(i, 0, self.boardsize))
            try_moves.append(self._pos + Position(-i, 0, self.boardsize))
            try_moves.append(self._pos + Position(0, -i, self.boardsize))
            try_moves.append(self._pos + Position(0, i, self.boardsize))
        
        
        moves = self.isLegal(try_moves)

        return moves


class Bishop(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)
        
    def possible_moves(self):
        try_moves = Moves([])
        for i in range(1, self.boardsize):
            try_moves.append(self._pos + Position(i, i, self.boardsize))
            try_moves.append(self._pos + Position(-i, -i, self.boardsize))
            try_moves.append(self._pos + Position(i, -i, self.boardsize))
            try_moves.append(self._pos + Position(-i, i, self.boardsize))
        
        
        moves = self.isLegal(try_moves)

        return moves


class Queen(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)
        
    def possible_moves(self):
        try_moves = Moves([])
        for i in range(1, self.boardsize):
            #Bishop moves
            try_moves.append(self._pos + Position(i, i, self.boardsize))
            try_moves.append(self._pos + Position(-i, -i, self.boardsize))
            try_moves.append(self._pos + Position(i, -i, self.boardsize))
            try_moves.append(self._pos + Position(-i, i, self.boardsize))
            ## Rook moves
            try_moves.append(self._pos + Position(i, 0, self.boardsize))
            try_moves.append(self._pos + Position(-i, 0, self.boardsize))
            try_moves.append(self._pos + Position(0, -i, self.boardsize))
            try_moves.append(self._pos + Position(0, i, self.boardsize))
        
        
        moves = self.isLegal(try_moves)

        return moves





class King(InitPiece):
    def __init__(self, init_pos, team, boardsize):
        super().__init__(init_pos, team, boardsize)

    def possible_moves(self):
        try_moves = Moves([])
        try_moves.append( self._pos + Position(-1, -1, self.boardsize) ) 
        try_moves.append( self._pos + Position(-1, 0, self.boardsize) )
        try_moves.append( self._pos + Position(-1, 1, self.boardsize) )
        try_moves.append( self._pos + Position(0, 1, self.boardsize) )
        try_moves.append( self._pos + Position(0, -1, self.boardsize) )
        try_moves.append( self._pos + Position(1, 1, self.boardsize) )
        try_moves.append( self._pos + Position(1, 0, self.boardsize) )
        try_moves.append( self._pos + Position(1, -1, self.boardsize) )


        moves = self.isLegal(try_moves)


        return moves

