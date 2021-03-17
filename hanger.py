from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# setup i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# create adc object using i2c bus
ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

try:
    while True:
        print("Sensor 0: {:>5.3f}".format(chan0.voltage))
        print("Sensor 1: {:>5.3f}".format(chan1.voltage))
        print("Sensor 2: {:>5.3f}".format(chan2.voltage))
        print("Sensor 3: {:>5.3f}".format(chan3.voltage))
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Ending...")

