from tkinter import *
from task import TaskFrame
from intro import IntroFrame

root = Tk()
root.attributes("-fullscreen", True)

outputPath = "data/" + input("Enter subject number: ") + ".csv"
outputFile = open(outputPath, "w")
taskFrame = TaskFrame(root, outputFile)
introFiles = ["images/first.png", "images/second.png"]
introFrame = IntroFrame(root, introFiles, taskFrame)

root.mainloop()
outputFile.close()
