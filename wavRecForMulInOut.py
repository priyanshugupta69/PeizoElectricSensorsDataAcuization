# import smbus
# import time
# import os

# address = 0x48

# def save_sensor_data_to_file(channel):

    # try:
        # bus = smbus.SMBus(1)
        # start_time = time.time()
        # end_time = start_time + 10
        # row = []

        # while time.time() - end_time <= 0:
            # bus.write_byte(address, channel)
            # value = bus.read_byte(address)
            # row.append(str(value))
        # return row 

    # except IOError:
        # print("Error: Unable to open the file.")
import time
import smbus
address = 0x48
def save_sensor_data_to_file(channel, column, filename):
    try:
        with open(filename, "a") as file:
            bus = smbus.SMBus(1)
            start_time = time.time()
            end_time = start_time + 10

            while time.time() - end_time <= 0:
                bus.write_byte(address, channel)
                value = bus.read_byte(address)
                file.write(',' * (column - 1) + str(value))  # Move to the specified column and write the sensor value
                file.write('\n')  # Append a newline character
            print("Data stored")

    except IOError:
        print("Error: Unable to open the file.")
