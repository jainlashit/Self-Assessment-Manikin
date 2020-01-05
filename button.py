from tkinter import *
from PIL import ImageTk

class Button:
    def __init__(self, frame, file):
        self.frame = frame
        self.photo = ImageTk.PhotoImage(file=file)
        self.button = Checkbutton(self.frame, image=self.photo)
        pass
