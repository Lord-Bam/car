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
    #time.sleep(0.05)   
    dir_clk.value(1)
    #time.sleep(0.05)
    dir_clk.value(0)
    #time.sleep(0.05)

def pulse_latch():
    #time.sleep(0.05)    
    dir_latch.value(1)
    #time.sleep(0.05)
    dir_latch.value(0)
    #time.sleep(0.05)

def shift_write(value):

    for x in range(0, 8):
        temp = value & 128
        print("temp=",temp, "/", end="")
        if temp == 128:
            dir_ser.on()           
        else:
            dir_ser.off()           
            
        pulse_clock()        
        value = value<<1     
        
    pulse_latch()
    print()


def stop():
    print("stop")    
    shift_write(0b00000000)
    
def m1_v():
    print("m1_v")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     0  0   0   0   1   0   0   >> hex  =  0x04
    shift_write(0b00000100)
    
def m1_a():
    print("m1_a")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     0  0   0   1   0   0   0   >> hex  =  0x08
    shift_write(0b00001000)
def m2_v():
    print("m2_v")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     0  0   0   0   0   1   0   >> hex  =  0x02
    shift_write(0b00000010)
    
def m2_a():
    print("m2_a")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     0  0   1   0   0   0   0   >> hex  =  0x10
    shift_write(0b00010000)
    
def m3_v():
    print("m3_v")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     0  0   0   0   0   0   1   >> hex  =  0x01
    shift_write(0b00100000)
    
def m3_a():
    print("m3_a")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     1  0   0   0   0   0   0   >> hex  =  0x40
    shift_write(0b10000000)
    
def m4_v():
    print("m4_v")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 0     0  1   0   0   0   0   0   >> hex  =  0x20
    shift_write(0b00000001)
    
def m4_a():
    print("m4_a")
    # M4B/M3B/M4A/M2B/M1B/M1A/M2A/M3A
    # QH / QG/ QF/ QE/QD /QC /QB /QA
    # 1     0  0   0   0   0   0   0   >> hex  =  0x80  
    shift_write(0b01000000) 
    
    
stop()
msgstr = ""
motorstates = [0,0,0,0,0,0,0,0]

while True:
    msgstr = input()
    
    
    if msgstr == "1/v":
        m1_v()
        
    elif msgstr == "1/0":
        stop()
        
    elif msgstr == "1/a":
        m1_a()
        

    elif msgstr == "2/v":
        m2_v()
        
    elif msgstr == "2/0":
        stop()
        
    elif msgstr == "2/a":
        m2_a()
        
    elif msgstr == "3/v":
        m3_v()
        
    elif msgstr == "3/0":
        stop()
        
    elif msgstr == "3/a":
        m3_a()   
        
    elif msgstr == "4/v":
        m4_v()
        
    elif msgstr == "4/0":
        stop()
        
    elif msgstr == "4/a":
        m4_a()
        
    else:
        print("verkeerd commando")
        
                


                

