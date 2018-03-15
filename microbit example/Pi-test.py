import serial, time
port = "/dev/ttyACM0"
baud = 115200

while True:
    s = serial.Serial(port)
    s.baudrate = baud
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    data = s.readline()
    data = str(data)
