import smbus
import time
import os

address = 0x48

def save_sensor_data_to_file(channel , filename):

    try:
        with open(filename, "a") as file:
            bus = smbus.SMBus(1)
            start_time = time.time()
            end_time = start_time + 10

            while time.time() - end_time <= 0:
                bus.write_byte(address, channel)
                value = bus.read_byte(address)
                file.write(str(value) + "\n")  # Write the sensor data to the file, append a newline character
            file.write("\n")
            print("data_stored")

    except IOError:
        print("Error: Unable to open the file.")






       
       


