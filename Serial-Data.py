import serial, time
port = "/dev/ttyUSB0"
baud = 9600

while True:
    s = serial.Serial(port)
    s.baudrate = baud
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    data = s.readline()
    time.sleep(1)
    data = str(data)
    data = data[2:7]
    data = float(data)
    print(data)
    if data > 21:
        print("It is warm")
    else:
        print("It is cold")

