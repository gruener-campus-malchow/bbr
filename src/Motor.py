# -*- coding: utf-8 -*- 
import configparser
import RPi.GPIO as GPIO
import time

class Motor():

    name = 'CENTER'
    pin = 1
    frequency = 50
    forward_slow = 6
    forward_fast = 7
    backward_slow = 8
    backward_fast = 9
    dutyCycle = 0
    steps = 0.05
    servo = True
    direction = 1

    def __init__(self, name):
    	self.name = name
    	
    	
    def set_power(self, power):
        power = int(power)
        print("power ist set to "+str(power))
        if power > 0:
            print("rotate forward")
            forward_range = abs(self.forward_slow - self.forward_fast)
            forward_steps = forward_range/100
            dc = self.forward_slow - power * forward_steps
        elif power <= 0:
            print("rotate backwards")
            backward_range = abs(self.backward_fast - self.backward_slow)
            backward_steps = backward_range/100
            dc = self.backward_slow + abs(power) * backward_steps
        print("hhhuuuhh: "+str(dc))
        if abs(power)>100:
            print("Wrong power range: use an integer between -100 an 100")
            return False

        foo = self.servo.ChangeDutyCycle(dc)
        print(str(foo))
        return "did it"

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.pin = int(config[self.name]['pin'])
        self.forward_slow = float(config[self.name]['forward_slow'])
        self.forward_fast = float(config[self.name]['forward_fast'])
        self.backward_slow = float(config[self.name]['backward_slow'])
        self.backward_fast = float(config[self.name]['backward_fast'])
        self.direction = int(config[self.name]['direction'])
        self.frequency = int(config['GENERAL']['frequency'])
    
    def print_config(self):
        print("name of the motor: " + self.name)
        print("pin on the header: " + str(self.pin))
        print("frequency of the pwm-signal: " + str(self.frequency))
        print("dutycycle for rotating slow forward: " + str(self.forward_slow))
        print("dutycycle for rotating fast forward: " + str(self.forward_fast))
        print("dutycycle for rotating slow backward: " + str(self.backward_slow))
        print("dutycycle for rotating fast backward: " + str(self.backward_fast))
        print("direction or orientation " + str(self.direction))

    def initiate_servo(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        self.servo = GPIO.PWM(self.pin, self.frequency) # GPIO 18 als PWM mit 50Hz
        self.servo.start(0) # Initialisierung
        # self.servo.ChangeDutyCycle(8)
        # return self.servo
        

    def increase(self):
        while self.dutyCycle < 9:
            self.dutyCycle = self.dutyCycle+self.steps
            print("Aktueller dutyCycle: "+str(self.dutyCycle))
            #servo.ChangeDutyCycle(dutyCycle)
            time.sleep(0.05)

    def decrease(self):   
        while self.dutyCycle > 7.2:
            self.dutyCycle = self.dutyCycle-self.steps
            print("Aktueller dutyCycle: "+str(self.dutyCycle))
            #servo.ChangeDutyCycle(dutyCycle)
            time.sleep(0.01)
