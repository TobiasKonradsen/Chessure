

class Position:
    def __init__(self, row = 0, col = 0, boardsize = [8,8]):
        self.row = row
        self.col = col
        self.boardsize = boardsize
        
    def __add__(self, pos):
        self.row = self.row + pos.row
        self.col = self.col + pos.col
        
    def isLegal(self):
        row_bol = self.row <= self.boardsize[0] or self.row >= 0
        col_bol = self.col <= self.boardsize[1] or self.col >= 0
        if row_bol and col_bol:
            return True
        else:
            return False
        