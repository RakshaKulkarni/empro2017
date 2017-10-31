import sys
import time
import Adafruit_DHT


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

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
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
