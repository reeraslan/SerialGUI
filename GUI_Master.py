from tkinter import *


class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Zelp FMLR Serial GUI")
        self.root.geometry("360x360")
        self.root.config(bg = "white")

class ComGUI:
    # Frame
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(root, text = "Com Manager", padx= 5, pady= 5, bg = "white")
        self.label_com = Label(self.frame, text = "Available Ports", width= 15, bg = "white", anchor="w")
        self.baudrate = Label(self.frame, text = "BaudRate", width= 15, bg = "white", anchor="w")

        self.publish()


        pass

    # put component on the frame
    def publish(self):
        self.frame.grid(row= 0, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5)
        self.label_com.grid(column=1, row = 2)
        self.baudrate.grid(column=1, row=3)
        pass

if __name__ == "__main__":
    RootGUI()
    ComGUI()