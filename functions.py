from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image


class GFG:
    def __init__(self,file_name,master=None):
        self.master = master

        # to take care movement in x direction
        self.x = 1
        # to take care movement in y direction
        self.y = 0

        # canvas object to add image
        self.canvas = Canvas(master)
        # adding image
        self.watermark_image = Image.open(file_name)
        self.watermark_image = self.watermark_image.resize((100, 100), Image.ANTIALIAS)
        self.new_watermark_image = ImageTk.PhotoImage(self.watermark_image)
        self.canvas.create_image(0, 0, image=self.new_watermark_image, anchor="nw")
        self.canvas.place(x=290, y=300)
        # right_.image = self.new_watermark_image
        # calling class's movement method to
        # move the rectangle
        self.movement()

    def movement(self):
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.rectangle, self.x, self.y)

        self.canvas.after(100, self.movement)

    # for motion in negative x direction
    def left(self, event):
        print(event.keysym)
        self.x = -5
        self.y = 0

    # for motion in positive x direction
    def right(self, event):
        print(event.keysym)
        self.x = 5
        self.y = 0

    # for motion in positive y direction
    def up(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -5

    # for motion in negative y direction
    def down(self, event):
        print(event.keysym)
        self.x = 0
        self.y = 5

    if __name__ == "__main__":
