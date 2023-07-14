import time
import os
directory = "sensor_data"
timestamp = time.strftime("%Y%m%d%H%M%S")  # Get the current timestamp
filename = os.path.join(directory, f"sensor_data_20230714163915.csv")
import wavRecForMulInOut
wavRecForMulInOut.save_sensor_data_to_file(0 , 2 , filename )



