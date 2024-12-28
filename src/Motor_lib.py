# -*- coding: utf-8 -*- 
import configparser
import RPi.GPIO as GPIO
import time

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
	
def set_power(servo):
    print("want to set power")
    foo = servo.ChangeDutyCycle(8.0)
    print(str(foo))
    return "did it"


def initiate_servo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.OUT)

    servo = GPIO.PWM(13, 15) # GPIO 18 als PWM mit 50Hz
    servo.start(0) # Initialisierung
    servo.ChangeDutyCycle(8.0)
    return servo
    
