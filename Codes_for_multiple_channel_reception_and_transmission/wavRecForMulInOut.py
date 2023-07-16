# code for reception at multiple channels[used in mulInmulOut.py]
import time
import smbus
import csv
address = 0x48
def save_sensor_data_to_file(channel, filename):
    try:
        with open(filename, "a") as file:
            bus = smbus.SMBus(1)
            start_time = time.time()
            end_time = start_time + 10
            row = []

            while time.time() - end_time <= 0:
                bus.write_byte(address, channel)
                value = bus.read_byte(address)
                row.append(str(value))
            writer = csv.writer(file)
            writer.writerow(row)

    except IOError:
        print("Error: Unable to open the file.")
