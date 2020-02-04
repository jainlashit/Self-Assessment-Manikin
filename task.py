from tkinter import *
from PIL import Image
from PIL import ImageTk


class TaskFrame:
    def __init__(self, root):
        self.root = root
        # SAM Scale taken as 9
        self.scale = 9
        self.padding = 10

        self.emotionFiles = ["happy.jpg", "contemptuous.jpg"]
        self.fileIndex = 0

        self.emotionFrame = Frame(root)

        self.arousalFrame = Frame(root)
        self.arousalButton = [None] * self.scale
        self.arousalPhoto = [None] * self.scale
        self.arousalVar = IntVar()
        self.arousalText = Label(self.arousalFrame, text="Arousal>>")

        self.valenceFrame = Frame(root)
        self.valenceButton = [None] * self.scale
        self.valencePhoto = [None] * self.scale
        self.valenceVar = IntVar()
        self.valenceText = Label(self.valenceFrame, text="Valence>>")

        self.emotionPhoto = self.load_emotion(self.emotionFiles[self.fileIndex], 0.4)
        self.emotionLabel = Label(self.emotionFrame, image=self.emotionPhoto)

        self.nextFrame = Frame(root)
        self.nextButton = Button(self.nextFrame, text="SUBMIT!", command=self.submit)

    def pack(self):
        self.emotionFrame.pack(pady=self.padding)
        self.emotionLabel.pack()

        self.arousalFrame.pack(pady=self.padding)
        self.valenceFrame.pack(pady=self.padding)

        self.nextFrame.pack()
        self.nextButton.pack()

        self.arousalText.pack(side=LEFT)
        for i in range(self.scale):
            arousalFile = "images/_arousal/arousal-" + str(i + 1) + ".png"
            self.arousalPhoto[i] = ImageTk.PhotoImage(file=arousalFile)
            self.arousalButton[i] = Radiobutton(self.arousalFrame, variable=self.arousalVar, value=i+1, indicatoron=0,
                                                image=self.arousalPhoto[i], selectcolor='#808080')
            self.arousalButton[i].pack(side=LEFT)

        self.valenceText.pack(side=LEFT)
        for i in range(self.scale):
            valenceFile = "images/_valence/valence-" + str(i + 1) + ".png"
            self.valencePhoto[i] = ImageTk.PhotoImage(file=valenceFile)
            self.valenceButton[i] = Radiobutton(self.valenceFrame, variable=self.valenceVar, value=i+1, indicatoron=0,
                                                image=self.valencePhoto[i], selectcolor='#808080')
            self.valenceButton[i].pack(side=LEFT)

    def submit(self):
        if self.valenceVar.get() == 0 or self.arousalVar.get() == 0:
            return
        else:
            self.fileIndex += 1

        if self.fileIndex >= len(self.emotionFiles):
            self.root.destroy()
        else:
            self.emotionLabel.forget()
            self.emotionPhoto = self.load_emotion(self.emotionFiles[self.fileIndex], 0.4)
            self.emotionLabel = Label(self.emotionFrame, image=self.emotionPhoto)
            self.emotionLabel.pack()

        print("Arousal: ", self.arousalVar.get())
        print("Valence: ", self.valenceVar.get())
        self.valenceVar.set(0)
        self.arousalVar.set(0)

    @staticmethod
    def load_emotion(file, scale=1):
        photo = Image.open(file)
        height, width = photo.size
        photo = photo.resize((int(scale * height), int(scale * width)), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image=photo)


if __name__ == "__main__":
    root = Tk()
    frame = TaskFrame(root)
    frame.pack()
    root.mainloop()
