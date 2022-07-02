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
        self.ComOptionMenu()
        self.BaudOptionMenu()

        self.padx = 10
        self.pady = 5

        self.publish()
        pass

    # create optionmenu object
    def ComOptionMenu(self):
        coms = [" - ", "COM3", "COM4", "COM5"]
        self.clicked_com = StringVar()
        self.clicked_com.set(coms[0])
        self.dropcom = OptionMenu(self.frame, self.clicked_com, *coms)
        self.dropcom.config(width= 20)
        pass

    # create baud option object
    def BaudOptionMenu(self):
        baudList = [" - ",
                    "9600",
                    "19200",
                    "115200",
                    "230400"]
        self.clicked_baud = StringVar()
        self.clicked_baud.set(baudList[1])
        self.clicked_baud = OptionMenu(self.frame, self.clicked_baud, *baudList)

        self.clicked_baud.config(width= 20)
        pass


    # put component on the frame
    def publish(self):
        self.frame.grid(row= 0, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5)
        self.label_com.grid(column=1, row = 2)
        self.dropcom.grid(column=2, row=2, padx= self.padx, pady= self.pady)
        self.clicked_baud.grid(column=2, row=3)
        self.baudrate.grid(column=1, row=3)

        pass

if __name__ == "__main__":
    RootGUI()
    ComGUI()