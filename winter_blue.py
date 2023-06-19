from ble_uart import BLEUART
import bluetooth
    
    
class WinterBlue():
    
    def __init__(self, name, handler):
        print("creating bluetooth")
    
        self.ble = bluetooth.BLE()
        self.uart = BLEUART(self.ble, name)

        def on_rx():
#             print("rx: ", uart.read().decode().strip())
            handler(self.uart.read().decode().strip())

        self.uart.irq(handler=on_rx)
        self.uart.close()
