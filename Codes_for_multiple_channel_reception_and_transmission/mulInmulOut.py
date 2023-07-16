#Code for transmitting and recieving singals on multiple channels[using threading to combine transmission and reception codes]
import threading
import time
import RPi.GPIO as GPIO
import wavGen
import wavRecForMulInOut
import os

def thread1_function(pin, frequency):
    # Code for thread 1
    wavGen.wavGenerator(pin, frequency)

# Define a function to be run as thread 2
def thread2_function(channel, filename):
    # Code for thread 2
    wavRecForMulInOut.save_sensor_data_to_file(channel, filename)

pins = [11, 13, 15, 16]
channels = [0, 1, 2, 3]
transducers = 0
frequency = 750
directory = "sensor_data"
timestamp = time.strftime("%Y%m%d%H%M%S")  # Get the current timestamp
filename = os.path.join(directory, f"sensor_data{timestamp}.csv")

for i in range(transducers, len(pins)):
    threads = []
    threads.append(threading.Thread(target=thread1_function, args=(pins[i], frequency,)))
    for j in range(i + 1, len(channels)):
        threads.append(threading.Thread(target=thread2_function, args=(channels[j], filename,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    threads.clear()
    transducers += 1

print("Data is stored successfully.")

