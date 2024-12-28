from Motor import Motor
import time

#motor_L = Motor('MOTOR_LEFT')

#motor_L.set_power(0.5)
#motor_L.load_config()
#motor_L.print_config()

motor_R = Motor('MOTOR_RIGHT')
motor_R.load_config()
motor_R.print_config()
motor_R.initiate.servo()
motor_R.set_power(0.5)


#try:
#  while True:
#    motor_R.increase()
#    print("rotiere weiter für 5 Sekunden")
#    time.sleep(5)
#    motor_R.decrease()
#    print("warte für 5 Sekunden")
#    time.sleep(5)

#except KeyboardInterrupt:
#  servo.stop()
# GPIO.cleanup()
#    pass


