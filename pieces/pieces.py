
from pieces.init_piece import InitPiece
from game_logic.position import Position
from game_logic.moves import Moves


class Pawn(InitPiece):
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
        
        self.first_move = True
        self.first_double = False ## Parameter to check for en passant. 
        self.name = 'Pawn'
        self.acii = 'P'
        
    def check_passant(self, pos):
        """Check if passant """
        test_pos = pos + Position(-self.team*1, 0, self.boardsize)
        
        if isinstance(self.board[test_pos], Pawn):
            other_pawn = self.board[test_pos]
            if other_pawn.first_double and other_pawn.team != self.team:
                return [True, test_pos]
            else:
                return [False, None]
        else:
            return [False, None]

    def check_empty_legal(self, move):
        return move.isLegal() and not self.check_not_empty(move)
    
    def possible_moves(self):
        
        if self.first_double:
            self.first_double = False
            
        try_moves = Moves([])  
        straight_move = self._pos + Position(self.team*1, 0, self.boardsize)
        
        ## This should be simplified
        # Check if the move is legal, then adds it the move, does the same for the first double move. 
        if self.check_empty_legal(straight_move):
                try_moves.append(straight_move)
                if self.first_move:
                    self.double_first_move = self._pos + Position(self.team*2, 0, self.boardsize)
                    if self.check_empty_legal(self.double_first_move):
                            try_moves.append(self.double_first_move)
            
        test_pos = [self._pos + Position(self.team*1, 1, self.boardsize),
                    self._pos + Position(self.team*1, -1, self.boardsize)]
        
        for pos in test_pos:
            if pos.isLegal() and (self.check_not_empty(pos) or self.check_passant(pos)[0]):
                    try_moves.append(pos)


        moves = self.isLegal(try_moves)


        return moves
    
    def move(self, pos):
        ## Overwrites the init move function
        self._pos = pos
        self.first_move = False
        if self.double_first_move == pos:
            self.first_double = True
        

class Knight(InitPiece):
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
        self.name = 'Knight'
        self.acii = 'N'
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
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
        self.name = 'Rook'
        self.acii = 'R'
        self.num_directions = 4
        self.first_move = True # For Castling 

    def get_collided_init(self):
        return [False]*self.num_directions
    
    def get_positions(self, i):
        positions = [Position(i, 0, self.boardsize),
                     Position(-i, 0, self.boardsize),
                     Position(0, -i, self.boardsize),
                     Position(0, i, self.boardsize)]
        return positions
    
    
    def check_collided(self, final_position, collided, k):
        if final_position.isLegal() and self.check_not_empty(final_position):                
            collided[k] = True
    
        return collided
    
    
    def possible_moves(self):
        
        collided = self.get_collided_init()
        try_moves = Moves([])
        for i in range(1, max(self.boardsize.rows, self.boardsize.cols)):
            positions = self.get_positions(i)
            
            for k, position in enumerate(positions):
                if not collided[k]:
                    final_position = self._pos + position
                    
                    try_moves.append(final_position)
                    
                    collided = self.check_collided(final_position, collided, k)
                        
        
        moves = self.isLegal(try_moves)

        return moves
    
    def move(self, pos):
        ## Checks is done at the game-level
        self._pos = pos
        self.first_move = False

class Bishop(Rook):
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
        self.name = 'Bishop'
        self.acii = 'B'

    def get_positions(self, i):
        positions = [Position(i, i, self.boardsize),
                     Position(-i, i, self.boardsize),
                     Position(i, -i, self.boardsize),
                     Position(-i, -i, self.boardsize)]
        return positions
    
    

class Queen(Rook):
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
        self.name = 'Queen'
        self.acii = 'Q'
        self.num_directions = 8
        
    def get_positions(self, i):
        positions = [Position(i, i, self.boardsize),
                     Position(-i, i, self.boardsize),
                     Position(i, -i, self.boardsize),
                     Position(-i, -i, self.boardsize),
                     Position(i, 0, self.boardsize),
                     Position(-i, 0, self.boardsize),
                     Position(0, -i, self.boardsize),
                     Position(0, i, self.boardsize)]
        return positions
        
        




class King(InitPiece):
    def __init__(self, init_pos, team, board):
        super().__init__(init_pos, team, board)
        self.name = 'King'
        self.acii = 'K'
        self.first_move = True # For Castling 

    def castling_check(self, move):
        """ Check if castling"""
        directionsposition = move - self._pos
        if self.first_move and abs(directionsposition.col) == 2:
            direction = directionsposition.col // 2
            collided = False
            for i in range(1, self.boardsize.cols):
                testmove = self._pos + Position(0, direction*i, self.boardsize)
                if testmove.isLegal() and self.check_not_empty(testmove) and not collided:
                    collided = True 
                    other_piece  = self.board[testmove]
                    if type(other_piece) == Rook: ## Strict check on the class, as bishop and queen inheirits from rook
                        if other_piece.first_move:
                            return [True, other_piece, Position(0, -direction, self.boardsize)]
                        
        return [False, None, None]
    def possible_moves(self):
        try_moves = Moves([])
        positions = [Position(-1, -1, self.boardsize),
                     Position(-1, 0, self.boardsize),
                     Position(-1, 1, self.boardsize),
                     Position(0, 1, self.boardsize),
                     Position(0, -1, self.boardsize),
                     Position(1, 1, self.boardsize),
                     Position(1, 0, self.boardsize),
                     Position(1, -1, self.boardsize)]
        for position in positions:
            try_moves.append(self._pos + position)

        
        castling_moves = [self._pos + Position(0, 2, self.boardsize),
                          self._pos + Position(0, -2, self.boardsize)]
        for move in castling_moves:
            if self.castling_check(move)[0]:
                try_moves.append( move )


        moves = self.isLegal(try_moves)


        return moves

    def move(self, pos):
        ## Checks is done at the game-level
        self._pos = pos
        self.first_move = False