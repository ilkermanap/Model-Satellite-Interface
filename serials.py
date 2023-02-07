import serial
import time

def getData(port, baudrate):
  ser = serial.Serial(port=f'{port}', baudrate=baudrate)
  while True:
      value  = ser.readline()
      valueInStr = str(value, 'UTF-8')
      print(valueInStr)
      
      time.sleep(1)