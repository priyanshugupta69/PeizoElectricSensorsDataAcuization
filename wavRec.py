import board
import time
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object
ads = ADS.ADS1015(i2c)

# Set the gain (if necessary)
ads.gain = 1

# Create an analog input channel on single-ended channel 0
chan = AnalogIn(ads, ADS.P0)

while True:
    # Read the raw ADC value
    raw_value = chan.value

    # Read the voltage value
    voltage = chan.voltage

    # Print the results
    print("Raw ADC Value:", raw_value)
    print("Voltage:", voltage, "V")
    time.sleep(1)


