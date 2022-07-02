from tkinter import *
from tkinter import messagebox


class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Zelp FMLR Serial GUI")
        self.root.geometry("480x480")
        self.root.config(bg="white")


class ComGUI:
    # Frame
    def __init__(self, root, serial):
        self.drop_baud = None
        self.clicked_baud = None
        self.drop_com = None
        self.clicked_com = None
        self.root = root
        self.serial = serial

        # initilize the connection GUI and the main widget
        self.frame = LabelFrame(root, text="Com Manager", padx=5, pady=5, bg="white")
        self.label_com = Label(self.frame, text="Available Ports", width=15, bg="white", anchor="w")
        self.baudrate = Label(self.frame, text="BaudRate", width=15, bg="white", anchor="w")
        self.button_refresh = Button(self.frame, text="Refresh Port List", width=20, command=self.com_refresh)
        self.button_connect = Button(self.frame, text="Connect", width=20, state="disabled",
                                     command=self.serial_connect)

        self.com_option_menu()
        self.baud_option_menu()

        self.padx = 10
        self.pady = 5

        self.publish()

    # create optionmenu object
    def com_option_menu(self):
        self.serial.get_com_port()
        self.clicked_com = StringVar()
        # set the com list from comport list and show the first element of it
        self.clicked_com.set(self.serial.COM_Port_List[0])

        self.drop_com = OptionMenu(self.frame, self.clicked_com, *self.serial.COM_Port_List, command=self.connect_ctrl)
        self.drop_com.config(width=20)
        pass

    # create baud option object
    def baud_option_menu(self):
        baud_list = [" - ",
                     "9600",
                     "19200",
                     "115200",
                     "230400"]
        self.clicked_baud = StringVar()
        self.clicked_baud.set(baud_list[0])
        self.drop_baud = OptionMenu(self.frame, self.clicked_baud, *baud_list, command=self.connect_ctrl)

        self.drop_baud.config(width=20)
        pass

    # put component on the frame
    def publish(self):
        self.frame.grid(row=0, column=0, rowspan=3, columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)
        self.drop_com.grid(column=2, row=2, padx=self.padx, pady=self.pady)
        self.drop_baud.grid(column=2, row=3)
        self.baudrate.grid(column=1, row=3)
        self.button_refresh.grid(column=3, row=2)
        self.button_connect.grid(column=3, row=3)

        pass

    def connect_ctrl(self, widget):
        print("Connect Control")
        print(self.clicked_baud.get())
        if "-" in self.clicked_com.get() or "-" in self.clicked_baud.get():
            self.button_connect["state"] = "disable"
        else:
            self.button_connect["state"] = "active"

    # restart the connection

    def com_refresh(self):
        # destroy the widget, recreate and publish it to update the changes in ports
        self.drop_com.destroy()
        self.com_option_menu()
        self.drop_com.grid(column=2, row=2, padx=self.padx, pady=self.pady)
        logic = []
        self.connect_ctrl(logic)
        pass

    def serial_connect(self):
        if self.button_connect["text"] in "Connect":
            self.serial.serial_open(self)

            if self.serial.ser.status:
                self.button_connect["text"] = "Disconnect"
                self.button_refresh["state"] = "disable"
                self.drop_com["state"] = "disable"
                self.drop_baud["state"] = "disable"
                # infomsg = f"Successfull UART Connection {self.clicked_com.get()}"
                # messagebox.showinfo("showinfo", infomsg)
                self.conn = ConnGUI(self.root, self.serial)

            else:
                self.clicked_com.get()
                # errormsg = f"Failure to establish UART connection using {self.clicked_com.get()}"
                # messagebox.show("showerror", errormsg)

        else:
            self.conn.ConnGUIClose()
            # close the connection
            self.serial.serial_close()

            # infomsg = f"Uart connection using {self.clicked_com.get()} is now closed !"
            # messagebox.showwarning("showinfo", infomsg)

            self.button_connect["text"] = "Connect"
            self.button_refresh["state"] = "active"
            self.drop_com["state"] = "active"
            self.drop_baud["state"] = "active"


class ConnGUI():

    def __init__(self,root,serial):
        self.root = root
        self.serial = serial

        # Build ConnGui Static Elements
        self.frame = LabelFrame(root, text="Connection Manager",
                                padx=5, pady=5, bg="white", width=60)
        self.sync_label = Label(
            self.frame, text="Sync Status: ", bg="white", width=15, anchor="w")
        self.sync_status = Label(
            self.frame, text="..Sync..", bg="white", fg="orange", width=5)

        self.ch_label = Label(
            self.frame, text="Active channels: ", bg="white", width=15, anchor="w")
        self.ch_status = Label(
            self.frame, text="...", bg="white", fg="orange", width=5)

        self.btn_start_stream = Button(self.frame, text="Start", state="disabled",
                                       width=5, command=self.start_stream)

        self.btn_stop_stream = Button(self.frame, text="Stop", state="disabled",
                                      width=5, command=self.stop_stream)

        self.btn_add_chart = Button(self.frame, text="+", state="disabled",
                                    width=5, bg="white", fg="#098577",
                                    command=self.new_chart)

        self.btn_kill_chart = Button(self.frame, text="-", state="disabled",
                                     width=5, bg="white", fg="#CC252C",
                                     command=self.kill_chart)
        self.save = False
        self.SaveVar = IntVar()
        self.save_check = Checkbutton(self.frame, text="Save data", variable=self.SaveVar,
                                      onvalue=1, offvalue=0, bg="white", state="disabled",
                                      command=self.save_data)


        # Optional Graphic parameters
        self.padx = 20
        self.pady = 15

        self.ConnGUIOpen()

    def ConnGUIOpen(self):
        '''
        Method to display all the widgets
        '''
        self.root.geometry("1000x120")
        self.frame.grid(row=0, column=4, rowspan=3,
                        columnspan=5, padx=5, pady=5)

        self.sync_label.grid(column=1, row=1)
        self.sync_status.grid(column=2, row=1)

        self.ch_label.grid(column=1, row=2)
        self.ch_status.grid(column=2, row=2, pady=self.pady)

        self.btn_start_stream.grid(column=3, row=1, padx=self.padx)
        self.btn_stop_stream.grid(column=3, row=2, padx=self.padx)

        self.btn_add_chart.grid(column=4, row=1, padx=self.padx)
        self.btn_kill_chart.grid(column=5, row=1, padx=self.padx)

        self.save_check.grid(column=4, row=2, columnspan=2)

    def ConnGUIClose(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            self.frame.destroy()
            self.root.geometry("480x480")

    def start_stream(self):
        pass

    def stop_stream(self):
        pass

    def new_chart(self):
        pass

    def kill_chart(self):
        pass

    def save_data(self):
        pass

if __name__ == "__main__":
    RootGUI()
    ComGUI()
    ConnGUI()