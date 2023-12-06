from lcd import screen
import psutil
import time

def monitoring():
    # Only for windows
    from temp import Temperature
    import wmi
    w = wmi.WMI()
    temp = Temperature()

    while True:
        cpu_load = w.Win32_Processor()[0].wmi_property("LoadPercentage").value

        ram = psutil.virtual_memory()
        temps = temp.fetch_stats()

        screen.print_top(f"CPU {cpu_load if cpu_load != None else '0'}% MEM {int(ram.percent)}%")

        screen.print_bottom(f"CPU {temps[0]}C GPU {temps[1]}C")

        if temps[1] >= 75 or temps[0] >= 80:
            screen.enable_led()
        else:
            screen.disable_led()

        time.sleep(1)

def static_text(top_text: str, bottom_text: str):
    while True:
        screen.print_top(top_text)
        screen.print_bottom(bottom_text)

        time.sleep(1)

static_text()