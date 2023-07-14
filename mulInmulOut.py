import threading
import time
import RPi.GPIO as GPIO
import wavGen
import wavRec1

def thread1_function(pin , frequency):
    # Code for thread 1
    wavGen.wavGenerator(pin , frequency)

# Define a function to be run as thread 2
def thread2_function(channel  ,filename):
    # Code for thread 2
    wavRec1.save_sensor_data_to_file(channel , filename)

pins = [11, 13, 15, 16]
channels = [0, 1, 2, 3]
transducers = 4
directory = "sensor_data"
timestamp = time.strftime("%Y%m%d%H%M%S")  # Get the current timestamp
filename = os.path.join(directory, f"sensor_data_{timestamp}.txt")

while transducers >= 0:
    threads = []
    frequency = 1500
    for i in range(transducers, len(pins)):
        threads.append(threading.Thread(target=thread1_function, args=(pins[i],frequency,)))
        for j in range(i + 1, len(channels)):
            threads.append(threading.Thread(target=thread2_function, args=(channels[j], filename,)))

    for thread in threads:
        thread.start()
    transducers-= 1
