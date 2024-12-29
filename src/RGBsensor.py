# -*- coding: utf-8 -*- 

# this code based on https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/

import RPi.GPIO as GPIO
import time
import configparser

# should go into config

class RGBsensor():

    name = "BORING"
    s2 = 23
    s3 = 24
    signal = 25
    NUM_CYCLES = 10 #think, this is number of timeslots waiting for good signal from sensor
    
    def __init__(self, name):
    	self.name = name
    

    def initiate_sensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.s2,GPIO.OUT)
        GPIO.setup(self.s3,GPIO.OUT)
        #print("\n")

    def sense_RGB(self):
            GPIO.output(self.s2,GPIO.LOW)
            GPIO.output(self.s3,GPIO.LOW)
            time.sleep(0.3) #important?
            start = time.time()
            for impulse_count in range(self.NUM_CYCLES):
                GPIO.wait_for_edge(self.signal, GPIO.FALLING)
            duration = time.time() - start      #seconds to run for loop
            red  = NUM_CYCLES / duration   #in Hz
            #print("red value - ",red)

            GPIO.output(self.s2,GPIO.LOW)
            GPIO.output(self.s3,GPIO.HIGH)
            time.sleep(0.3)
            start = time.time() #important?
            for impulse_count in range(self.NUM_CYCLES):
                GPIO.wait_for_edge(self.signal, GPIO.FALLING)
            duration = time.time() - start
            blue = NUM_CYCLES / duration
            #print("blue value - ",blue)

            GPIO.output(self.s2,GPIO.HIGH)
            GPIO.output(self.s3,GPIO.HIGH)
            time.sleep(0.3)#important?
            start = time.time()
            for impulse_count in range(self.NUM_CYCLES):
                GPIO.wait_for_edge(self.signal, GPIO.FALLING)
            duration = time.time() - start
            green = NUM_CYCLES / duration
            #print("green value - ",green)
            #time.sleep(2)
            
            return [red,green,blue]

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        #self.pin = int(config[self.name]['pin'])
        
    def print_config(self):
    
        print("comming soon")
