from RGBsensor import RGBsensor
import time
import RPi.GPIO as GPIO

sensor_L = RGBsensor('RGBSENSOR_LEFT')
sensor_L.load_config()
sensor_L.print_config()
sensor_L.initiate_sensor()

#sensor_R = RGBsensor('RGBSENSOR_RIGHT')
#sensor_R.load_config()
#sensor_R.print_config()
#sensor_R.initiate_sensor()


try:
    while True:
        result_L = sensor_L.sense_RGB()
        #result_R = sensor_R.sense_RGB()
        print(result_L)
        #print("LEFT [r,g,b]" + str(result_L) + "RIGHT [r,g,b]" + str(result_R))
        #time.sleep(0.2)

except KeyboardInterrupt:
    #servo.stop()
    GPIO.cleanup()


