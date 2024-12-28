from Motor import Motor
import time

motor_L = Motor('MOTOR_LEFT')
motor_L.load_config()
motor_L.print_config()
motor_L.initiate_servo()

motor_R = Motor('MOTOR_RIGHT')
motor_R.load_config()
motor_R.print_config()
motor_R.initiate_servo()

try:
    while True:
        power_R = int(input("set power level_R: "))
        motor_R.set_power(power_R)
        power_L = int(input("set power level_L: "))
        motor_L.set_power(power_L)
        #print("rotiere weiter für 5 Sekunden")
        #time.sleep(5)

except KeyboardInterrupt:
    #servo.stop()
    GPIO.cleanup()


