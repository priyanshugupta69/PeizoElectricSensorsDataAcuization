import smbus
import time
import os
import RPi.GPIO as GPIO

address = 0x48

def contData(channel):
  try:
     while True:
        bus = smbus.SMBus(1)
        bus.write_byte(address, channel)
        value = bus.read_byte(address)
        time.sleep(0.5)
        print(value)
  except KeyboardInterrupt:
     GPIO.cleanup()
