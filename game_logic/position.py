
from board.chessboard import BoardSize

class Position:
    def __init__(self, row=0, col=0, boardsize = BoardSize(8, 8)):
        self.row = row
        self.col = col
        self.boardsize = boardsize

    def __add__(self, pos):
        return Position(self.row + pos.row, self.col + pos.col, self.boardsize)

    def __repr__(self):
        return f"Position(row={self.row}, col={self.col}, boardsize={self.boardsize})"
    
    
    def __eq__(self, other):
        """ Method for checking how to compare the object, for the 'in' operation """
        if isinstance(other, Position):
            return self.row == other.row and self.col == other.col and self.boardsize == other.boardsize
        else:
            return self.row == other
    
    
    
    def isLegal(self):
        row_bol = 0 <= self.row < self.boardsize.rows  
        col_bol = 0 <= self.col < self.boardsize.cols 
        return row_bol and col_bol
