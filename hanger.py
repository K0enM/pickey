from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import http.client as client
import json

con = client.HTTPConnection('mod7-pickey.herokuapp.com' , 80)

GPIO.setmode(GPIO.BCM)

# setup i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# create adc object using i2c bus
ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

def get_voltages():
    return {
            2: chan0.voltage,
            3: chan1.voltage,
            4: chan2.voltage,
            5: chan3.voltage,
     }

try:
    while True:
        data = get_voltages()
        print('Sending voltages...')
        headers = {'Content-type' : 'application/json'}
        for key, value in data.items():
            to_send = { 'weight': value}
            json_data = json.dumps(to_send)
            con.request("PUT", "/api/hanger/" + str(key), json_data, headers)  
            res = con.getresponse()
            res.read()
        sleep(2.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Ending...")

