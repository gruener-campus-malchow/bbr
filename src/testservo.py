import RPi.GPIO as GPIO
import time

servoPIN = int(input("Please input BCM-Pin-Number: "))
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

frequency = int(input("Please input frequency (e.g. 50): "))
servo = GPIO.PWM(servoPIN, frequency)
servo.start(0) # Initialisierung

try:
  while True:
    dutyCycle = real(input("Input dutycycle: "))
    print("Aktueller dutyCycle: "+str(dutyCycle))
    servo.ChangeDutyCycle(dutyCycle)
except KeyboardInterrupt:
  servo.stop()
  GPIO.cleanup()
