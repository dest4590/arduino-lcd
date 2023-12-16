import serial

com = 3 # Enter your com port here

class Screen:
    def __init__(self, com: int):
        self.port = 'COM' + str(com)

        try: 
            self.com = serial.Serial(self.port, baudrate=9600, timeout=0.5)

        except serial.SerialException as e:
            e = str(e)

            if 'FileNotFound' in e:
                print(f'{self.port} port not found, make sure you are selected valid port.')
            elif 'PermissionError' in e:
                print(f'''{self.port} access is denied, maybe it is busy with something else or you don't have rights, also make sure you close Arduino IDE''')
            
            quit()

        print(f'Connected to {self.port}, check screen')

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