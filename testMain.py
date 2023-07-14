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
    wavRec1.save_sensor_data_to_file(channel)

pin1 = 11
pin2 = 13  # Additional pin for the new thread
pin3 = 15
pin4 = 16
channel1 = 0
channel2 = 1  # Additional channel for the new thread
channel3 = 2 
channel4 = 3 

# transmitor 1
thread1 = threading.Thread(target=thread1_function, args=(pin1,))

# reciever 1
thread2 = threading.Thread(target=thread2_function, args=(channel1,))

# transmitter 2
thread3 = threading.Thread(target=thread1_function, args=(pin2,))

# reciever 2
thread4 = threading.Thread(target=thread2_function, args = (channel2,))

# trasmitter 3
thread5 = threading.Thread(target=thread2_function, args=(pin3,))

# reciver 3
thread6 = threading.Thread(target=thread2_function, args=(channel3,))

# transmitter 4
thread7 = threading.Thread(target=thread2_function, args=(pin4,))

# reciever 4
thread8 = threading.Thread(target=thread2_function, args=(channel4,))



# Start thread 1 and thread 2 simultaneously
thread1.start()
thread2.start()

# Sleep for 10 seconds
time.sleep(10)
GPIO.cleanup()

# Start thread 3 and thread 4 simultaneously
thread3.start()
thread4.start()

# Sleep for another 10 seconds
time.sleep(10)
GPIO.cleanup()

# Function to stop the execution of threads
def stop_execution():
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
stop_execution()

 


# Call the stop_execution function to join all threads and perform GPIO cleanup


