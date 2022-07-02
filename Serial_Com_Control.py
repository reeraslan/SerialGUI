import serial.tools.list_ports


class SerialControlClass:

    def __init__(self):
        self.COM_Port_List = []
        pass

    def get_com_port(self):
        ports = serial.tools.list_ports.comports()
        # get the second element in the list which is full name of port info
        self.COM_Port_List = [com[0] for com in ports]
        # add '-' character to the first index of list
        self.COM_Port_List.insert(0, "-")

    def serial_open(self, gui):
        try:
            self.ser.is_open
        except:
            PORT = gui.clicked_com.get()
            BAUD = gui.clicked_baud.get()
            self.ser = serial.Serial()
            self.ser.baudrate = BAUD
            self.ser.port = PORT
            self.ser.timeout = 0.1

        try:
            if self.ser.is_open:
                self.ser.status = True
            else:
                PORT = gui.clicked_com.get()
                BAUD = gui.clicked_baud.get()
                self.ser = serial.Serial()
                self.ser.baudrate = BAUD
                self.ser.port = PORT
                self.ser.timeout = 0.1
                self.ser.open()
                self.ser.status = True
        except:
            self.ser.status = False

    def serial_close(self):
        try:
            self.ser.is_open
            self.ser.close()
            self.ser.status = False
        except:
            self.ser.status = False



if __name__ == "__main__":
    SerialControlClass()
