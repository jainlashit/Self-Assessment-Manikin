from tkinter import *
from task import TaskFrame
from intro import IntroFrame

root = Tk()
root.attributes("-fullscreen", True)

taskFrame = TaskFrame(root)
introFiles = ["images/first.png", "images/second.png"]
introFrame = IntroFrame(root, introFiles, taskFrame)


root.mainloop()
