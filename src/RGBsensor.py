# -*- coding: utf-8 -*- 
# this code based on https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/

import RPi.GPIO as GPIO
import time
import configparser



class RGBsensor():

    name = "BORING"
    s2 = 23
    s3 = 24
    signal = 25
    NUM_CYCLES = 10 #think, this is number of values used for one measurement    
    def __init__(self, name):
    	self.name = name

    def initiate_sensor(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.s2,GPIO.OUT)
        GPIO.setup(self.s3,GPIO.OUT)
        print("initiation of " + str(self.name) + " completed")
    

#| s2 | s3 | selected diode             |
#|----|----|----------------------------|
#| L  | L  | red                        |
#| L  | H  | blue                       |
#| H  | L  | clear (no filter on diode) |
#| H  | H  | green                      |
    def sense(self, s2, s3):
        print("start measurement of " + str(self.name))     

        GPIO.output(self.s2,)
        GPIO.output(self.s3,GPIO.LOW)
        time.sleep(0.3) #important?
        start = time.time()
        print("everthing prepared")
        for impulse_count in range(self.NUM_CYCLES):
            print("wait for signal 500ms timeout")
            GPIO.wait_for_edge(self.signal, GPIO.FALLING, timeout=500)
        duration = time.time() - start      #seconds to run for loop
        return self.NUM_CYCLES / duration   #in Hz

    def sense_RGB(self):
        
        # measures red
        result = self.sense(GPIO.LOW. GPIO.LOW)
        print("red value - ", result)
        
        # measures blue
        result = self.sense(GPIO.LOW. GPIO.HIGH)
        print("blue value - ", result)
        
        # measures green
        result = self.sense(GPIO.HIGH. GPIO.HIGH)
        print("green value - ", result)
        #time.sleep(2)
        
        return [int(red),int(green),int(blue)]

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.s2 = int(config[self.name]['s2_pin'])
        self.s3 = int(config[self.name]['s3_pin'])
        self.signal = int(config[self.name]['signal_pin'])
        self.NUM_CYCLES = int(config[self.name]['NUM_CYCLES'])
        
    def print_config(self):
        print("Config of "+ str(self.name) + " following")
        print("pin of the s2-diode-selektor: " + str(self.s2))
        print("pin of the s3-diode-selektor: " + str(self.s3))
        print("pin of the sensor signal: " + str(self.signal))
        print("Number of cycles used for each measurement: " + str(self.NUM_CYCLES))
