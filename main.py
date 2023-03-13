import ast
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from uart import Ui_WesTech
from functions import Function_UI
import serial, serial.tools.list_ports

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_WesTech()
        self.uic.setupUi(self.main_win)

        self.serial = Function_UI()
        self.serialPort = serial.Serial()
        self.serial.update_port()

        self.uic.portInput.addItems(self.serial.portList)
        self.uic.baudrateInput.addItems(self.serial.baudList)
        self.uic.baudrateInput.setCurrentText('9600')

        # Clickable Buttons   
        self.serial.data_available.connect(self.update_views)

        self.uic.baslatBtn.clicked.connect(self.connect_or_disconnect)
        self.uic.secBtn.clicked.connect(lambda: self.select_file(btn=True))
        self.uic.sendCommand.clicked.connect(lambda: self.terminal(''))
        self.uic.commandInput.returnPressed.connect(lambda: self.terminal('', btn=True))

    def update_views(self, data):
        try:
            data = ast.literal_eval(data)
            #Hatalar Güncellenmesi
            errors = data.get('HATALAR')
            if errors.get('1') == 1:
                self.uic.hatalar1input.setStyleSheet("background-color: red;\n"
                                                "border-radius: 5px;\n"
                                                "border-color: red;\n"
                                                "border-width: 5px;")
            else:
                self.uic.hatalar1input.setStyleSheet("background-color: green;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
            if errors.get('2') == 1:
                self.uic.hatalar2input.setStyleSheet("background-color: red;\n"
                                                "border-radius: 5px;\n"
                                                "border-color: red;\n"
                                                "border-width: 5px;")
            else:
                self.uic.hatalar2input.setStyleSheet("background-color: green;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
            if errors.get('3') == 1:
                self.uic.hatalar3input.setStyleSheet("background-color: red;\n"
                                                "border-radius: 5px;\n"
                                                "border-color: red;\n"
                                                "border-width: 5px;")
            else:
                self.uic.hatalar3input.setStyleSheet("background-color: green;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
            if errors.get('4') == 1:
                self.uic.hatalar4input.setStyleSheet("background-color: red;\n"
                                                "border-radius: 5px;\n"
                                                "border-color: red;\n"
                                                "border-width: 5px;")
            else:
                self.uic.hatalar4input.setStyleSheet("background-color: green;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
            if errors.get('5') == 1:
                self.uic.hatalar5input.setStyleSheet("background-color: red;\n"
                                                "border-radius: 5px;\n"
                                                "border-color: red;\n"
                                                "border-width: 5px;")
            else:
                self.uic.hatalar5input.setStyleSheet("background-color: green;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
            # Zaman Güncellenmesi
            times = data.get('SAAT')
            self.uic.saatInput.setText(f"{times.get('REALTIME')}")
            self.uic.baslangicInput.setText(f"{times.get('START')}")
            self.uic.ayrilmaInput.setText(f"{times.get('LEAVE')}")
            self.uic.inisInput.setText(f"{times.get('DOWN')}")
            self.uic.toplamInput.setText(f"{times.get('TOPLAM')}")

            # Gyro Güncellenmesi
            gyro = data.get('GYRO')
            self.uic.xInput.setText(f"{gyro.get('x')}")
            self.uic.yInput.setText(f"{gyro.get('y')}")
        except:
            print('Loading...')

    def connect_or_disconnect(self):
        if self.uic.baslatBtn.text() == 'BAŞLAT':
            # if len(Function_UI.data)>0:
            self.connect_serial()
            self.uic.terminalBrowser.append('<span style=\" font-size:8pt;\">starting: </span><span style=\" font-size:8pt; color:#306c00;\">succesfully</span>')
        elif self.uic.baslatBtn.text() == 'DURDUR':
            if self.serial.serialPort.is_open:
                self.disconnect_serial()
                self.uic.terminalBrowser.append('<span style=\" font-size:8pt;\">stoping: </span><span style=\" font-size:8pt; color:#306c00;\">succesfully</span>')

    def connect_serial(self):
        port = self.uic.portInput.currentText()
        baud = self.uic.baudrateInput.currentText()
        self.serial.serialPort.port = port
        self.serial.serialPort.baudrate = baud
        self.serial.connect_serial()
        self.uic.baslatBtn.setText("DURDUR")
        # IP
        self.uic.ipInput.setEnabled(False)
        # ComboBox
        self.uic.portInput.setEnabled(False)
        self.uic.baudrateInput.setEnabled(False)

    def disconnect_serial(self):
        self.uic.baslatBtn.setText("BAŞLAT")
        self.serial.stop_thread()
        self.serial.serialPort.close()

        # IP
        self.uic.ipInput.setEnabled(True)
        # ComboBox
        self.uic.portInput.setEnabled(True)
        self.uic.baudrateInput.setEnabled(True)

        # Errors
        self.uic.hatalar1input.setStyleSheet("background-color: white;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
        self.uic.hatalar2input.setStyleSheet("background-color: white;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
        self.uic.hatalar3input.setStyleSheet("background-color: white;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
        self.uic.hatalar4input.setStyleSheet("background-color: white;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
        self.uic.hatalar5input.setStyleSheet("background-color: white;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: red;\n"
                                            "border-width: 5px;")
        
        # Times
        self.uic.saatInput.setText("")
        self.uic.baslangicInput.setText("")
        self.uic.ayrilmaInput.setText("")
        self.uic.inisInput.setText("")
        self.uic.toplamInput.setText("")

        # GYRO
        self.uic.xInput.setText("0")
        self.uic.yInput.setText("0")

    def select_file(self, btn):
        options = QFileDialog.Options()
        file_url = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);", options=options)
        file_name = file_url[0].split("/")[-1]
        self.uic.dosyaAdi.setText(file_name)
        if btn:
            self.uic.terminalBrowser.append(f'<span style=\" font-size:8pt;\">selected: {file_name}</span>')
        return file_name

    def terminal(self, outcommand, btn):
        if len(outcommand)>0:
            command = outcommand
        else:
            command = self.uic.commandInput.text()
        # self.uic.terminalBrowser.append(command)
        self.uic.commandInput.setText('')
        if command == 'saga -help':
            self.uic.terminalBrowser.append("""<span style=\" font-size:8pt;\">use the 'saga' keyword</span><br>
                                                <span style=\" font-size:8pt;\">-help: get help</span><br>
                                                <span style=\" font-size:8pt;\">-clean: clean terminal</span><br>
                                                <span style=\" font-size:8pt;\">-start: start system</span><br>
                                                <span style=\" font-size:8pt;\">-stop: shut down the system</span><br>
                                                <span style=\" font-size:8pt;\">-selectfile: select file</span><br>""")
        elif command == 'saga -clean':
            self.uic.terminalBrowser.clear()
        elif command == 'saga -start':
            self.connect_or_disconnect()
        elif command == 'saga -stop':
            if self.serial.serialPort.is_open:
                self.connect_or_disconnect()

        elif command == 'saga -selectfile':
            self.uic.terminalBrowser.append(f'<span style=\" font-size:8pt;\">selected: {self.select_file(btn=False)}</span>')


        elif command == 'saga -dev':
                self.uic.terminalBrowser.append('<span style=\" font-size:8pt;\">Developed by Shohrat Agazada</span>')

    # def send_data(self):
    #     data_send = self.uic.send_Text.toPlainText()
    #     self.serial.send_data(data_send)

    # def update_ports(self):
    #     self.serial.update_port()
    #     self.uic.port_List.clear()
    #     self.uic.port_List.addItems(self.serial.portList)

    # def clear(self):
    #     self.uic.textBrowser.clear()

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())