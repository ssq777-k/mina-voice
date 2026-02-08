class MotorController:
    def __init__(self, port):
        self.port = port
        # Initialize serial port communication
        self.initialize_serial(port)

    def initialize_serial(self, port):
        import serial
        self.serial_port = serial.Serial(port, baudrate=9600, timeout=1)

    def forward(self):
        self.serial_port.write(b'FORWARD')
        print('Moving forward')

    def backward(self):
        self.serial_port.write(b'BACKWARD')
        print('Moving backward')

    def turn_left(self):
        self.serial_port.write(b'TURN_LEFT')
        print('Turning left')

    def turn_right(self):
        self.serial_port.write(b'TURN_RIGHT')
        print('Turning right')

    def stop(self):
        self.serial_port.write(b'STOP')
        print('Stopping motors')

    def close(self):
        self.serial_port.close()
        print('Serial port closed')
