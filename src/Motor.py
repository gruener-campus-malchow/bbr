# -*- coding: utf-8 -*- 
import configparser
import RPi.GPIO as GPIO
import time

class Motor():

    name = 'CENTER'
    pin = 1
    frequency = 50
    forward_min = 6
    forward_max = 7
    backward_min = 8
    backward_max = 9
    dutyCycle = 0
    steps = 0.05
    servo = True

    def __init__(self, name):
    	self.name = name
    	pass
    	
    def set_power(self, servo):
        print(power)
        foo = servo.ChangeDutyCycle(8.0)
        print(str(foo))
        return power

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.pin = int(config[self.name]['pin'])
        self.forward_min = float(config[self.name]['forward_min'])
        self.forward_max = float(config[self.name]['forward_max'])
        self.backward_min = float(config[self.name]['backward_min'])
        self.backward_max = float(config[self.name]['backward_max'])
        self.frequency = int(config['GENERAL']['frequency'])
    
    def print_config(self):
        print("name of the motor: " + self.name)
        print("pin on the header: " + str(self.pin))
        print("frequency of the pwm-signal: " + str(self.frequency))
        print("minimal dutycycle for rotating forward: " + str(self.forward_min))
        print("maximal dutycycle for rotating forward: " + str(self.forward_max))
        print("minimal dutycycle for rotating backward: " + str(self.backward_min))
        print("maximal dutycycle for rotating backward: " + str(self.backward_max))

    def initiate_servo(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        servo = GPIO.PWM(self.pin, self.frequency) # GPIO 18 als PWM mit 50Hz
        servo.start(0) # Initialisierung
        return servo
        

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
