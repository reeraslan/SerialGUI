from GUI_Master import RootGUI, ComGUI
from Serial_Com_Control import SerialControlClass


MySerial = SerialControlClass()

RootMaster = RootGUI()
ComMaster = ComGUI(RootMaster.root, MySerial)

RootMaster.root.mainloop()

