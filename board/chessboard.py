


class BoardSize(int):
    """A representation of the board size."""

    def __new__(cls, rows, cols, *args, **kwargs):
        """Return a Moves instance."""
        cls.rows = rows
        cls.cols = cols
        return super(cls, cls).__new__(cls, (rows)*(cols), *args, **kwargs)



class ChessBoard(list):
    """A representation of the chessboard."""

    def __new__(cls, *args, **kwargs):
        """Return a Moves instance."""
        return super(ChessBoard, cls).__new__(cls, *args, **kwargs)

    def __init__(self, rows, cols):
        """Call list __init__."""
        self.size = BoardSize(rows, cols)
        self.piece_positions = set() # Maybe other datatype better
        super().__init__([i for i in range(self.size)])

    def __len__(self):
        """Use builtin-methods."""
        return self.size

    def __getitem__(self, pos):
        """Get a Position class in the list that corresponds to this row, col indexing."""
        row, col = pos.row, pos.col
        return super().__getitem__(row*self.size.cols + col)
    
    def __setitem__(self, pos, value):
        """Get the value in the list that corresponds to this row, col indexing."""
        row, col = pos.row, pos.col
        index = row*self.size.cols + col
        if value == None and index in self.piece_positions:
            self.piece_positions.remove(index)
        else:
            self.piece_positions.add(index)
        return super().__setitem__(index, value)
    
    def __iter__(self):
       self.n = 0
       self.iterob = iter(self.piece_positions)
       return self

    def __next__(self):
       """ Could optimize such that it only loops over set from the setitem functions positions"""
       index = next(self.iterob)
       if self.n < len(self.piece_positions):
           result = super().__getitem__(index)
           if (result is not None) and (type(result) is not int):
               self.n += 1  
               return result
       else:
          raise StopIteration
      
    def show_acii(self):
        """ Simple representation of board, for debugging"""
        stringlist = ""
        stringrow = ""
        for i, piece in enumerate(self):
            if i%self.size.rows == 0:
                stringlist += stringrow+"\n"
                stringrow = ""
            if not ((piece == None) or (type(piece) == int)):
                stringrow += piece.acii
                
            else:
                stringrow += "."
        stringlist += stringrow
        return str(stringlist[1:])
            
        
        
    