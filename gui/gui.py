


# from tkinter import *

# class GUI:
#     def __init__(self, game, window_size =(400, 400)):
        
#         window = Tk()
#         wx, wy = window_size
#         window.geometry(f"{wx}x{wy}")
#         label = Label(window,bg="red",width=10, height=5)
#         label.place(x=0,y=0)

#         label2 = Label(window,bg="blue",width=10, height=5)
#         label2.place(x=100,y=100)

#         label.bind("<Button-1>",self.drag_start)
#         label.bind("<B1-Motion>",self.drag_motion)

#         label2.bind("<Button-1>",self.drag_start)
#         label2.bind("<B1-Motion>",self.drag_motion)

#         window.mainloop()

        

#     def drag_start(self, event):
#         widget = event.widget
#         widget.startX = event.x
#         widget.startY = event.y
    
#     def drag_motion(self, event):
#         widget = event.widget
#         x = widget.winfo_x() - widget.startX + event.x
#         y = widget.winfo_y() - widget.startY + event.y
#         widget.place(x=x,y=y)



# GUI(1)


import tkinter as tk

class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        width = 700
        height = 700
        self.create_background(width, height, 8, 8)
        
        label = tk.Label(self, bg="red",width=10, height=5)
        label.place(x=0,y=0)
        print(int(self.cellwidth-2))
        label2 = tk.Label(self, bg="blue",width=10, height=5)
        x1, x2, y1, y2 = self.pos[6, 3]
        print(x1, x2, y1, y2)
        label2.place(x=int(x1+7),y=int(y1+7))

        label.bind("<Button-1>",self.drag_start)
        label.bind("<B1-Motion>",self.drag_motion)

        label2.bind("<Button-1>",self.drag_start)
        label2.bind("<B1-Motion>",self.drag_motion)
        
    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
        
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

