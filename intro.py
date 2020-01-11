from tkinter import *
from PIL import Image
from PIL import ImageTk


class IntroFrame(object):
	def __init__(self, root, files, taskFrame=None):
		self.root = root
		self.index = 0

		self.taskFrame = taskFrame
		self.files = files

		self.mainFrame = Frame(root)
		self.image = self.load_image(files[self.index], 0.8)
		self.mainLabel = Label(self.mainFrame, image=self.image)

		self.buttonFrame = Frame(root)
		self.previousButton = Button(self.buttonFrame, text="Previous", command=self.prev)
		self.continueButton = Button(self.buttonFrame, text="Continue", command=self.next)
		self.pack()

	def pack(self):
		self.mainFrame.pack()
		self.mainLabel.pack()
		self.buttonFrame.pack()
		self.previousButton['state'] = DISABLED

		# update required for getting window width
		self.root.update()
		self.previousButton.grid(column=0, row=0, padx=self.root.winfo_width()/4)
		self.continueButton.grid(column=1, row=0, padx=self.root.winfo_width()/4)

	def prev(self):
		self.index -= 1
		if self.index == 0:
			self.previousButton['state'] = DISABLED
		self.mainLabel.destroy()
		self.image = self.load_image(self.files[self.index], 0.8)
		self.mainLabel = Label(self.mainFrame, image=self.image)
		self.mainLabel.pack()

	def next(self):
		self.index += 1
		if self.index == len(self.files):
			self.destroy()
			# self.taskFrame.pack()
		else:
			self.previousButton['state'] = NORMAL
			self.mainLabel.destroy()
			self.image = self.load_image(self.files[self.index], 0.8)
			self.mainLabel = Label(self.mainFrame, image=self.image)
			self.mainLabel.pack()

	def destroy(self):
		self.mainFrame.destroy()
		self.buttonFrame.destroy()

	@staticmethod
	def load_image(file, scale=1.0):
		photo = Image.open(file)
		height, width = photo.size
		photo = photo.resize((int(scale * height), int(scale * width)), Image.ANTIALIAS)
		return ImageTk.PhotoImage(image=photo)


myRoot = Tk()
files = ["images/first.png", "images/second.png"]
firstFrame = IntroFrame(myRoot, files)
myRoot.mainloop()
