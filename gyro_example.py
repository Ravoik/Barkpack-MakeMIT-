import time
import board
import busio
import adafruit_l3gd20
I2C = busio.I2C(board.SCL, board.SDA)
SENSOR = adafruit_l3gd20.L3GD20_I2C(I2C)

