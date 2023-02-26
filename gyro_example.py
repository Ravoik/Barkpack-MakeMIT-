import time
import board
import busio
import adafruit_l3gd20

I2C = busio.I2C(27,23)
SENSOR = adafruit_l3gd20.L3GD20_I2C(I2C)

while True:
    print("Angular Velocity (rad/s): {}".format(SENSOR.gyro))
    print()
    time.sleep(1)

