#Code for recieving data and st
import smbus
import time
import os

address = 0x48

directory = "sensor_data"
timestamp = time.strftime("%Y%m%d%H%M%S")  # Get the current timestamp
filename = os.path.join(directory, f"sensor_data{timestamp}.txt")

def save_sensor_data_to_file(channel):

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






       
       


