from tkinter import *
from PIL import Image
from PIL import ImageTk

scale_num = 9
padding = 10

root = Tk()
root.attributes("-fullscreen", True)

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
emotionFrame.pack(pady=padding)

arousalFrame = Frame(root)
arousalFrame.pack(pady=padding)
arousalButton = [None]*scale_num
arousalPhoto = [None]*scale_num

valenceFrame = Frame(root)
valenceFrame.pack(pady=padding)
valenceButton = [None]*scale_num
valencePhoto = [None]*scale_num

emotionPhoto = load_emotion(fileIndex)
emotionLabel = Label(emotionFrame, image=emotionPhoto)
emotionLabel.pack()


def submit():
    global fileIndex, emotionPhoto, emotionLabel, emotionFrame, valenceButton, arousalButton

    if valenceVar.get() == 0 or arousalVar.get() == 0:
        return
    else:
        fileIndex += 1

    if fileIndex >= len(emotionFiles):
        root.destroy()
    else:
        emotionLabel.forget()
        emotionPhoto = load_emotion(fileIndex)
        emotionLabel = Label(emotionFrame, image=emotionPhoto)
        emotionLabel.pack()

    print("Arousal: ", arousalVar.get())
    print("Valence: ", valenceVar.get())
    valenceVar.set(0)
    arousalVar.set(0)


nextFrame = Frame(root)
nextFrame.pack()
nextButton = Button(nextFrame, text="SUBMIT!", command=submit)
nextButton.pack()

arousalVar = IntVar()
valenceVar = IntVar()

arousalText = Label(arousalFrame, text="Arousal>>")
arousalText.pack(side=LEFT)

for i in range(scale_num):
    arousalFile = "images/_arousal/arousal-" + str(i+1) + ".png"
    arousalPhoto[i] = ImageTk.PhotoImage(file=arousalFile)
    arousalButton[i] = Radiobutton(arousalFrame, variable=arousalVar, value=i+1, indicatoron=0, image=arousalPhoto[i],
                                   selectcolor='#808080')
    arousalButton[i].pack(side=LEFT)

valenceText = Label(valenceFrame, text="Valence>>")
valenceText.pack(side=LEFT)

for i in range(scale_num):
    valenceFile = "images/_valence/valence-" + str(i+1) + ".png"
    valencePhoto[i] = ImageTk.PhotoImage(file=valenceFile)
    valenceButton[i] = Radiobutton(valenceFrame, variable=valenceVar, value=i+1, indicatoron=0, image=valencePhoto[i],
                                   selectcolor='#808080')
    valenceButton[i].pack(side=LEFT)

root.mainloop()
