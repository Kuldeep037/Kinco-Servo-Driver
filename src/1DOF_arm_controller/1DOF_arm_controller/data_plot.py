import tkinter as tk

class DrawingApp:
    def __init__(self,root):
        self.root = root

    def create_rect_anime(self,data,row,column):
        self.data = data
        self.canvas = tk.Canvas(self.root, width=100, height=250)
        self.canvas.grid(row=row,column=column)
        self.outer_rect = self.canvas.create_rectangle(3, 30, 30, 243, outline='black')  # Outer rectangle
        self.inner_rect = self.canvas.create_rectangle(6, 240, 27, 250, fill='blue')     # Inner rectangle
        self.update_inner_rect()

    def update_inner_rect(self):
        inner_rect_height = 240-self.data
        self.canvas.coords(self.inner_rect, 6, 240, 27, inner_rect_height)
        self.root.after(10, self.update_inner_rect)
