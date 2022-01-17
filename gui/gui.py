


import tkinter as tk
from game_logic.game import Game

from game_logic.game import Game
from pieces.pieces import Pawn, King, Knight, Rook, Bishop, Queen
from game_logic.team import White, Black
from game_logic.position import Position
from game_logic.moves import Moves


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        width = 700
        height = 700
        self.create_background(width, height, 8, 8)
        self.game = Game(1)
        self.board = self.game.board
        
        self.width_image = 60
        
        self.labels = {}
        
        self.images = {}
        
        self.setup_images()
        
        self.show_board()



    def setup_images(self):
        """ Setup the image paths, this could be written more compressed"""
        for piece in self.board:
            if isinstance(piece.team, White):
                if isinstance(piece, Pawn):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_plt60.png')
                if isinstance(piece, Rook):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_rlt60.png')
                if isinstance(piece, Knight):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_nlt60.png')
                if isinstance(piece, Queen):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_qlt60.png')
                if isinstance(piece, King):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_klt60.png')
                if isinstance(piece, Bishop):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_blt60.png')
            if isinstance(piece.team, Black):
                if isinstance(piece, Pawn):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_pdt60.png')
                if isinstance(piece, Rook):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_rdt60.png')
                if isinstance(piece, Knight):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_ndt60.png')
                if isinstance(piece, Queen):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_qdt60.png')
                if isinstance(piece, King):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_kdt60.png')
                if isinstance(piece, Bishop):
                    self.images[piece] = tk.PhotoImage(file='./graphics/Chess_bdt60.png')
                        
            
    def show_board(self):
        for piece in self.board:
            self.setup_piece(piece)
    
    def delete_board(self):
        for piece in self.board:
            if piece != None:
                self.labels[piece].destroy()
        


                
            
    def setup_piece(self, piece):
        
        if not piece == None:
            position = piece.get_position()
            row, col = position.row, position.col
            x1, x2, y1, y2 = self.pos[row, col]
            self.labels[piece] = tk.Label(self, image = self.images[piece], anchor = tk.SW)
            self.labels[piece].place(x=(x1+x2)/2-self.width_image/2,y=(y1+y2)/2-self.width_image/2)
            self.labels[piece].bind("<Button-1>",lambda event, arg=piece: self.drag_start(event, piece))
            self.labels[piece].bind("<B1-Motion>",self.drag_motion)
            self.labels[piece].bind("<ButtonRelease-1>", lambda event, arg=piece: self.on_release(event, piece))
    
    def on_release(self, event, piece):
        widget = event.widget

        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        col, row = int(x // self.cellwidth), int(y // self.cellheight) ## This is weird...

        try_move = Position(row, col, self.board.size)
        # Delete the board.
        self.delete_board()
        # Game handles the move. Either it move, or not. 
        self.game.event_handler(try_move, piece) # Move the piece
        # Show updated move. 
        self.show_board()
        self.remove_underlay()
        

        
    def remove_underlay(self):
        for cans in self.underlay:
            self.canvas.delete(cans)
            
    def underlay_for_possible_moves(self, piece):
        possible_moves = piece.possible_moves_board()
        # Green border for possible moves
        for position in possible_moves:
            row, col = position.row, position.col
            x1, x2, y1, y2 = self.pos[row, col]
            self.underlay.append(
                self.canvas.create_rectangle(x1, y1, x2, y2, 
                                             fill='green', tags="rect") # stipple="gray50"
                                )
                
                
    def drag_start(self, event, piece):
        self.underlay = []
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
        self.underlay_for_possible_moves(piece)
        
                
    def drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x,y=y)
        
         
    def create_background(self, width, height, boardsizex, boardsizey):
        
        self.canvas = tk.Canvas(self, width = width, height = height, borderwidth = 0, highlightthickness = 0)
        
        self.canvas.pack(side="top", fill="both", expand="true")
        
        self.grid_size_x = boardsizex
        self.grid_size_y = boardsizey
        self.cellwidth = width / self.grid_size_x 
        self.cellheight = height / self.grid_size_y

        self.rect = {}
        self.pos = {}
        colors = ['grey','white smoke']
        count = 0 
        
        for column in range(self.grid_size_x):
            for row in range(self.grid_size_y):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.pos[row, column] = [x1, x2, y1, y2]
                self.rect[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2,
                                                                      fill=colors[count%2], tags="rect")
                count += 1
            count +=1
                


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()

