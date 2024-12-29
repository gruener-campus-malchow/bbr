from RGBsensor import RGBsensor
import time
import RPi.GPIO as GPIO

sensor = RGBsensor('RGBSENSOR_LEFT')
sensor.load_config()
sensor.print_config()
sensor.initiate_sensor()

try:
    while True:
        result = sensor.sense_RGB()
        print(result)
        #time.sleep(0.2)

except KeyboardInterrupt:
    #servo.stop()
    GPIO.cleanup()


