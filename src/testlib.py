import Motor_lib
import time

#motor_L = Motor('MOTOR_LEFT')

#motor_L.set_power(0.5)
#motor_L.load_config()
#motor_L.print_config()


motor_R = Motor_lib.initiate_servo()

while True:
    dc = float(input("set dc: "))
    Motor_lib.set_power(motor_R,dc)

        
