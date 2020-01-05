from tkinter import *
from PIL import Image
from PIL import ImageTk

scale_num = 9

root = Tk()

emotionFiles = ["happy.jpg", "contemptuous.jpg"]
fileIndex = 0


def load_emotion(index):
    file = emotionFiles[index]
    photo = Image.open(file)
    height, width = photo.size
    scale = 0.4
    photo = photo.resize((int(scale*height), int(scale*width)), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image=photo)


emotionFrame = Frame(root)
emotionFrame.pack()

arousalIndex = -1
arousalFrame = Frame(root)
arousalFrame.pack()
arousalButton = [None]*scale_num
arousalPhoto = [None]*scale_num

valenceIndex = -1
valenceFrame = Frame(root)
valenceFrame.pack()
valenceButton = [None]*scale_num
valencePhoto = [None]*scale_num

emotionPhoto = load_emotion(fileIndex)
emotionLabel = Label(emotionFrame, image=emotionPhoto)
emotionLabel.pack()


def arousal(index):
    global arousalIndex
    arousalIndex = index
    print("Button Number " + str(index+1))
    pass


def valence(index):
    global valenceIndex
    valenceIndex = index
    print("Button Number " + str(index+1))
    pass


def submit():
    global fileIndex, emotionPhoto, emotionLabel, emotionFrame, valenceIndex, arousalIndex, valenceButton, arousalButton
    emotionLabel.forget()
    fileIndex += 1
    emotionPhoto = load_emotion(fileIndex)
    emotionLabel = Label(emotionFrame, image=emotionPhoto)
    emotionLabel.pack()
    # valenceButton[valenceIndex].deselect()
    # arousalButton[arousalIndex].deselect()
    valenceVar.set(11)
    arousalVar.set(11)
    valenceIndex = -1
    arousalIndex = -1


nextFrame = Frame(root)
nextFrame.pack()
nextButton = Button(nextFrame, text="SUBMIT!", command=submit).pack()

arousalVar = IntVar()
valenceVar = IntVar()


for i in range(scale_num):
    arousalFile = "images/_arousal/arousal-" + str(i+1) + ".png"
    arousalPhoto[i] = ImageTk.PhotoImage(file=arousalFile)
    arousalButton[i] = Radiobutton(arousalFrame, variable=arousalVar, value=i+1, text="Arousal",
                                   command=lambda index=i: arousal(index))
    arousalButton[i].pack(side=LEFT)

for i in range(scale_num):
    valenceFile = "images/_valence/valence-" + str(i+1) + ".png"
    valencePhoto[i] = ImageTk.PhotoImage(file=valenceFile)
    valenceButton[i] = Radiobutton(valenceFrame, variable=valenceVar, value=i+1, text="Valence",
                                   command=lambda index=i: valence(index))
    valenceButton[i].pack(side=LEFT)

root.mainloop()
