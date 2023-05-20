import machine
import time

#dir_en = machine.Pin(13, machine.Pin.OUT)
dir_latch = machine.Pin(23, machine.Pin.OUT)
dir_clk = machine.Pin(22, machine.Pin.OUT)
dir_ser = machine.Pin(21, machine.Pin.OUT)

pwm1 = machine.PWM(machine.Pin(16))
pwm1.freq(800)
pwm1.duty(1023)

pwm2 = machine.PWM(machine.Pin(17))
pwm2.freq(800)
pwm2.duty(1023)

pwm3 = machine.PWM(machine.Pin(18))
pwm3.freq(800)
pwm3.duty(1023)

pwm4 = machine.PWM(machine.Pin(19))
pwm4.freq(800)
pwm4.duty(1023)

#dir_en.off()

def pulse_clock():  
    dir_clk.value(1)
    dir_clk.value(0)

def pulse_latch():  
    dir_latch.value(1)
    dir_latch.value(0)

def shift_write(motorstates):
    print(motorstates)
    for motorstate in motorstates:
        if motorstate == 1:
            dir_ser.on()          
        else:
            dir_ser.off()          
            
        pulse_clock()
        
    pulse_latch()
    print()
    
msgstr = ""
motorstates = [0,0,0,0,0,0,0,0]
shift_write(motorstates)

while True:
    msgstr = input()
    old_motorstates = motorstates.copy()
    
    #motor1
    if msgstr == "1/v":
        motorstates[4] = 0
        motorstates[5] = 1

    elif msgstr == "1/a":
        motorstates[4] = 1
        motorstates[5] = 0
        
    elif msgstr == "1/0":
        motorstates[5] = 0
        motorstates[4] = 0
        
    #motor2
    elif msgstr == "2/v":
        motorstates[3] = 0
        motorstates[6] = 1
        
    elif msgstr == "2/a":
        motorstates[3] = 1
        motorstates[6] = 0
        
    elif msgstr == "2/0":
        motorstates[3] = 0
        motorstates[6] = 0
        
    #motor3
    elif msgstr == "3/v":
        motorstates[0] = 0
        motorstates[2] = 1
        
    elif msgstr == "3/a":
        motorstates[0] = 1
        motorstates[2] = 0
        
    elif msgstr == "3/0":
        motorstates[0] = 0
        motorstates[2] = 0
        
    #motor4
    elif msgstr == "4/v":
        motorstates[1] = 0
        motorstates[7] = 1
        
    elif msgstr == "4/a":
        motorstates[1] = 1
        motorstates[7] = 0
        
    elif msgstr == "4/0":
        motorstates[1] = 0
        motorstates[7] = 0
        
    elif msgstr == "a/v":
        motorstates = [0 for motor in motorstates]
        motorstates[5] = 1
        motorstates[6] = 1
        motorstates[2] = 1
        motorstates[7] = 1
        
        
    elif msgstr == "a/a":
        motorstates = [0 for motor in motorstates]
        motorstates[4] = 1
        motorstates[3] = 1
        motorstates[0] = 1
        motorstates[1] = 1
    
    elif msgstr == "a/0":
        motorstates = [0 for motor in motorstates]

        
    else:
        print("verkeerd commando")
        
    if motorstates != old_motorstates:
        shift_write(motorstates)
        
                


                

