import serial.tools.list_ports
from serials import getData

class GetData:
    def __init__(self, ip, port, baudrate) -> None:
        self.ip = ip
        self.port = port
        self.baudrate = baudrate      

    def set_connection():
        # Check Serial Ports
        def ports():
          comlist = serial.tools.list_ports.comports()
          connected = []
          for element in comlist:
              connected.append(element.device)
          return connected
        connection_data_list = [['300', '600', '1200', '2400', '4800',
                                 '9600', '14400', '19200', '38400', '57600',
                                 '115200', '230400', '250000', '500000',
                                 '1000000'], ports()]
        return connection_data_list
    
    def connect(ip, port, baudrate):
        getData(port, baudrate)
        

    def camera():
        pass
    
    def gps():
        pass
    
    def gyro():
        pass
    
    def buttons():
        pass
    
    def terminal():
        pass
    
    def errors():
        pass
    
    def date():
        pass
    
    def upload_file():
        pass
    
    #Charts

    def temperature():
        pass
    
    def accelerometer(): #Ivmeolcer
        pass
    
    def speed():
        pass
    
    def damp(): #Nem
        pass
    
    def pressure_carrier(): #Taşıyıcı Basınç
        pass
    
    def pressure_duty_load(): #Taşıyıcı Görev Yükü
        pass
    
    

    