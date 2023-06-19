import winterboot
import __main__
import car





def wb_handler(message):
    print(message)
    if "XY: " in message:
        message = message.split(" ")
        car.x = float(message[1])
        car.y = float(message[2])
        
    if "Button1" in message:
        message = message.split(" ")
        car.dim_lights = bool(int(message[1]))
        
    if "Button2" in message:
        message = message.split(" ")
        car.alarm_lights = bool(int(message[1]))


wb = winterboot.WinterBoot()
car = car.Car(wb.motor_shield, wb.front_lights, wb.rear_lights, wb.distance_sensor, wb.df, wb.voltage_meter, wb.battery_led)

car.start()
