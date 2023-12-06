import serial

com = 3 # Enter your com port here

class Screen:
    def __init__(self, com: int):
        self.port = 'COM' + str(com)

        self.com = serial.Serial(self.port, baudrate=9600, timeout=0.5)

        print(f'Connected to {self.port}')

    def write(self, data: str):
        self.com.write(f'\n{data}'.encode())

    def print_top(self, text: str): 
        self.write('T' + text)

    def print_bottom(self, text: str):
        self.write('B' + text)

    def enable_led(self):
        self.write('H') # HIGH

    def disable_led(self):
        self.write('L') # LOW

screen = Screen(com)