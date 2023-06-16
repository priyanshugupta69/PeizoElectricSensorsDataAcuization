import threading
import time
import RPi.GPIO as GPIO
import wavGen
import wavRec1


# Define a function to be run as thread 1
def thread1_function(pin):
    # Code for thread 1
    wavGen.wavGenerator(pin)

# Define a function to be run as thread 2
def thread2_function(channel):
    # Code for thread 2
    wavRec1.wavReception(channel)
pin = 11
channel = 0
duration = 10
# Create thread 1
thread1 = threading.Thread(target=thread1_function , args =  (pin , ))

# Create thread 2
thread2 = threading.Thread(target=thread2_function , args = (channel , ))

# Start both threads
thread1.start()
thread2.start()


# Function to stop the execution of threads
def stop_execution():
    thread1.join()
    thread2.join()
    GPIO.cleanup()

# Schedule the stop_execution function to be called after the specified duration
timer = threading.Timer(duration, stop_execution)
timer.start()


