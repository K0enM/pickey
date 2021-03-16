from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

# setup i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# create adc object using i2c bus
ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)

try:
    while True:
        print("{:>5.3f}".format(chan0.voltage))
        sleep(2.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Ending...")

