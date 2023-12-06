import clr
import os

hwtypes = ['CPU', 'GPUNvidia', 'GPUAti']

class Temperature:
    def __init__(self):
        # Works only in windows
        file = rf'{os.getcwd()}\OpenHardwareMonitorLib.dll'
        clr.AddReference(file)

        from OpenHardwareMonitor import Hardware

        handle = Hardware.Computer()
        handle.CPUEnabled = True
        handle.GPUEnabled = True

        handle.Open()
        
        self.handle = handle


    def fetch_stats(self):
        cpu = None
        gpu = None

        for i in self.handle.Hardware:
            i.Update()
            for sensor in i.Sensors:
                if sensor.Value:
                    temp = self.parse_sensor(sensor)
                    if temp != None:
                        if temp[0]:
                            cpu = temp[0]
                        
                        if temp[1]:
                            gpu = temp[1]

        return [int(cpu), int(gpu)]

    cpu_temp = False
    gpu_temp = False

    def parse_sensor(self, sensor):
        if str(sensor.SensorType) == 'Temperature':
            if str(sensor.Hardware.HardwareType) == 'CPU' and not self.cpu_temp:
                self.cpu_temp = sensor.Value

            if str(sensor.Hardware.HardwareType) == 'GpuNvidia' and not self.gpu_temp:
                self.gpu_temp = sensor.Value
            
            if str(sensor.Hardware.HardwareType) == 'GpuAti' and not self.gpu_temp:
                self.gpu_temp = sensor.Value

            return [self.cpu_temp, self.gpu_temp]