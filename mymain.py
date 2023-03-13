from PySide6.QtWidgets import QApplication, QWidget, QDialog
from PySide6.QtCore import  QThread, Signal
from serial import Serial

from satellite import Satellite
from ui_main import Ui_Dialog

import sys
import json
import glob


def find_serials():
    temp = glob.glob("/dev/ttyAMA*")
    temp += glob.glob("/dev/ttyUSB*")
    return temp

class DataSource(QThread):
    updateProgress = Signal()
    
    def __init__(self, serialport):
        QThread.__init__(self)
        self.serial = serialport
        self.lastline = None

    def run(self):
        while 1:            
            self.lastline = self.serial.readline().decode().strip()
            if len(self.lastline) > 0:
                self.updateProgress.emit()


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, app = None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.datasource = None
        self.satellite = Satellite("Sat1",  parent=self)
        for serial in find_serials():
            self.cmbSerialPorts.addItem(serial)
        self.show()

    def updateplots(self):
        if self.datasource.lastline is not None:
            print(self.datasource.lastline)
            self.satellite.new_data(json.loads(self.datasource.lastline))


    def serial_connect(self):
        if self.datasource is not None:
            self.datasource.exit()
            self.datasource = None
        tempserial = Serial(self.cmbSerialPorts.currentText(), int(self.comboBox.currentText()))
        self.datasource = DataSource(tempserial)
        self.datasource.updateProgress.connect(self.updateplots)
        self.datasource.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)

