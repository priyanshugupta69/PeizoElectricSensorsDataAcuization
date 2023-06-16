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
    return wavRec1.wavReception(channel)

# Define a function to print sensor output in columns
def print_sensor_output(sensor_num, output):
    print(f"Sensor {sensor_num}: {output}")

# Create GPIO pin and channel lists for the four sensors
pins = [11, 13, 15, 16]
channels = [0, 1, 2, 3]

# Create threads for each sensor
threads = []
for i in range(4):
    # Create thread for wavGen.py (sensor i)
    thread_gen = threading.Thread(target=thread1_function, args=(pins[i],))
    threads.append(thread_gen)

    # Create thread for wavRec1.py (sensor i+1)
    thread_rec = threading.Thread(target=thread2_function, args=(channels[i],))
    threads.append(thread_rec)

# Start all threads
for thread in threads:
    thread.start()

# Join all threads and collect outputs
outputs = []
for i, thread in enumerate(threads):
    thread.join()
    if i % 2 != 0:
        outputs.append(thread.result())

# Print the outputs in separate columns
sensor_labels = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4"]
for label, output in zip(sensor_labels, outputs):
    print_sensor_output(label, output)

# Additional logic for the second set of operations
# Create threads for each sensor (sensor 2 to sensor 4)
threads = []
for i in range(1, 4):
    # Create thread for wavGen.py (sensor i+1)
    thread_gen = threading.Thread(target=thread1_function, args=(pins[i],))
    threads.append(thread_gen)

    # Create thread for wavRec1.py (sensor i+2)
    thread_rec = threading.Thread(target=thread2_function, args=(channels[i+1],))
    threads.append(thread_rec)

# Start all threads
for thread in threads:
    thread.start()

# Join all threads and collect outputs
outputs = []
for i, thread in enumerate(threads):
    thread.join()
    if i % 2 != 0:
        outputs.append(thread.result())

# Print the outputs in separate columns
sensor_labels = ["Sensor 2", "Sensor 3", "Sensor 4"]
for label, output in zip(sensor_labels, outputs):
    print_sensor_output(label, output)

# Additional logic for the third set of operations
# Create threads for each sensor (sensor 3 and sensor 4)
threads = []
for i in range(2, 4):
    # Create thread for wavGen.py (sensor i+1)
    thread_gen = threading.Thread(target=thread1_function, args=(pins[i],))
    threads.append(thread_gen)

    # Create thread for wavRec1.py (sensor i+2)
    thread_rec = threading.Thread(target=thread2_function, args=(channels[i+1],))
    threads.append(thread_rec)

# Start all threads
for thread in threads:
    thread.start()

# Join all threads and collect outputs
outputs = []
for i, thread in enumerate(threads):
    thread.join()
    if i % 2 != 0:
        outputs.append(thread.result())

# Print the outputs in separate columns
sensor_labels = ["Sensor 3", "Sensor 4"]
for label, output in zip(sensor_labels, outputs):
    print_sensor_output(label, output)

GPIO.cleanup()
