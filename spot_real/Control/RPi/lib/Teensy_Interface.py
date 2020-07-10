import serial


class TeensyInterface:
    def __init__(self, port='/dev/ttyS0', baud=500000):
        self.ser = serial.Serial(port, baud)
        self.ser.flush()

        self.buffer = []

    def __construct_string(self, i, x, y, z):
        return "{},{},{},{}\n".format(i, x, y, z)

    def add_to_buffer(self, i, x, y, z):
        self.buffer.append(self.__construct_string(i, x, y, z))

    def add_calib_to_buffer(self, i, x, spd=100):
        self.buffer.append("{},{},{},{}\n".format(4, i, x, spd))

    def add_raw(self, val):
        self.buffer.append("{}\n".format(val))

    def send_buffer(self):
        for message in self.buffer:
            self.ser.write(message.encode('utf-8'))
        self.buffer = []
