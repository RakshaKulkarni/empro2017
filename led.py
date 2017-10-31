import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

start_time = time.time()

humidity1, temperature1 = Adafruit_DHT.read_retry(22,4)
print('Reading from 1st sensor: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature1, humidity1))
time.sleep(0.1)

humidity2, temperature2 = Adafruit_DHT.read_retry(22,17)
print('Reading from 2nd sensor: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature2, humidity2))
time.sleep(0.1)

humidity3, temperature3 = Adafruit_DHT.read_retry(22,27)
print('Reading from 3rd sensor: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature3, humidity3))

humidity = (humidity1 +humidity2 + humidity3)/3
temperature =(temperature1+ temperature2+temperature3)/3

if humidity is not None and temperature is not None:
    print('Average temperature is: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
if (temperature > 40 or humidity > 55):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(15, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(15,True) ## Turn on GPIO pin 7

if (37 <= temperature <= 39 and 50 <= humidity <= 55):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(19, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(19,True) ## Turn on GPIO pin 7

if (temperature < 37 or humidity < 50):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(21, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(21,True) ## Turn on GPIO pin 7

else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

print("Time taken is: --- %s seconds ---" % (time.time() - start_time))
