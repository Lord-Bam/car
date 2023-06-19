import machine
import time


class MotorShield():
    
    def __init__(self, dir_latch, dir_clk, dir_ser, pwm_pin1, pwm_pin2, pwm_pin3, pwm_pin4):
        self.dir_latch = machine.Pin(dir_latch, machine.Pin.OUT)
        self.dir_clk = machine.Pin(dir_clk, machine.Pin.OUT)
        self.dir_ser = machine.Pin(dir_ser, machine.Pin.OUT)

        self.pwm1 = machine.PWM(machine.Pin(pwm_pin1))
        self.pwm1.freq(800)
        self.pwm1.duty(0)

        self.pwm2 = machine.PWM(machine.Pin(pwm_pin2))
        self.pwm2.freq(800)
        self.pwm2.duty(0)

        self.pwm3 = machine.PWM(machine.Pin(pwm_pin3))
        self.pwm3.freq(800)
        self.pwm3.duty(0)

        self.pwm4 = machine.PWM(machine.Pin(pwm_pin4))
        self.pwm4.freq(800)
        self.pwm4.duty(0)
        
        self.motorstates = [0,0,0,0,0,0,0,0]
        self.shift_write(self.motorstates)

    #dir_en.off()

    def pulse_clock(self):  
        self.dir_clk.value(1)
        self.dir_clk.value(0)

    def pulse_latch(self):  
        self.dir_latch.value(1)
        self.dir_latch.value(0)

    def shift_write(self, motorstates):
        for motorstate in self.motorstates:
            if motorstate == 1:
                self.dir_ser.on()          
            else:
                self.dir_ser.off()          
                
            self.pulse_clock()
            
        self.pulse_latch()
        print()
        
    def forward(self):
        #set motostate to full stop
        self.motorstates = [0 for motor in self.motorstates]
        #set all engines to forward
        self.motorstates[5] = 1
        self.motorstates[6] = 1
        self.motorstates[2] = 1
        self.motorstates[7] = 1
        self.shift_write(self.motorstates)
        
    def back(self):
        #set motostate to full stop
        self.motorstates = [0 for motor in self.motorstates]
        #set all engines to forward
        self.motorstates[4] = 1
        self.motorstates[3] = 1
        self.motorstates[0] = 1
        self.motorstates[1] = 1
        self.shift_write(self.motorstates)
        
    def stop(self):
        #set motostate to full stop
        self.motorstates = [0 for motor in self.motorstates]
        self.shift_write(self.motorstates)
        
      
    #motor 1
    def left_front_forward(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 1
        self.shift_write(self.motorstates)
        
    def left_front_back(self):
        self.motorstates[4] = 1
        self.motorstates[5] = 0
        self.shift_write(self.motorstates)
        
    def left_front_stop(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 0
        self.shift_write(self.motorstates)

    #motor2
    def right_front_forward(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 1
        self.shift_write(self.motorstates)
        
    def right_front_back(self):
        self.motorstates[3] = 1
        self.motorstates[6] = 0
        self.shift_write(self.motorstates)
        
    def right_front_stop(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 0
        self.shift_write(self.motorstates)
        
    #motor 3
    def left_rear_forward(self):
        self.motorstates[0] = 0
        self.motorstates[2] = 1
        self.shift_write(self.motorstates)
        
    def left_rear_back(self):
        self.motorstates[0] = 1
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
    def left_rear_stop(self):
        self.motorstates[0] = 0
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
    #motor 4
    def right_rear_forward(self):
        self.motorstates[1] = 0
        self.motorstates[7] = 1
        self.shift_write(self.motorstates)
        
    def right_rear_back(self):
        self.motorstates[1] = 1
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)
        
    def right_rear_stop(self):
        self.motorstates[1] = 0
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)
        
        
    def left_wheels_forward(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 1
        self.motorstates[0] = 0
        self.motorstates[2] = 1
        self.shift_write(self.motorstates)
        
    def left_wheels_back(self):
        self.motorstates[4] = 1
        self.motorstates[5] = 0
        self.motorstates[0] = 1
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
    def left_wheels_stop(self):
        self.motorstates[4] = 0
        self.motorstates[5] = 0
        self.motorstates[0] = 0
        self.motorstates[2] = 0
        self.shift_write(self.motorstates)
        
        
    def right_wheels_forward(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 1
        self.motorstates[1] = 0
        self.motorstates[7] = 1
        self.shift_write(self.motorstates)

        
    def right_wheels_back(self):
        self.motorstates[3] = 1
        self.motorstates[6] = 0
        self.motorstates[1] = 1
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)
        
    def right_wheels_stop(self):
        self.motorstates[3] = 0
        self.motorstates[6] = 0
        self.motorstates[1] = 0
        self.motorstates[7] = 0
        self.shift_write(self.motorstates)


    def all_wheels_forward(self):
        self.left_wheels_forward()
        self.right_wheels_forward()
        print("all wheels forward")

    def all_wheels_back(self):
        self.left_wheels_back()
        self.right_wheels_back()
        print("all wheels back")

    def all_wheels_stop(self):
        self.left_wheels_stop()
        self.right_wheels_stop()
        print("all wheels stop")
        
    def speed_left_wheels(self, speed):
        self.pwm1.duty(speed)
        self.pwm2.duty(speed)
        
    def speed_right_wheels(self, speed):
        self.pwm3.duty(speed)
        self.pwm4.duty(speed)
        
    def speed_all_wheels(self, speed):
        self.speed_left_wheels(speed)
        self.speed_right_wheels(speed)