# code for transmission and switching of multiple transmitters[used in mulInmulOut.py]
# the input signal is of ten sec duration and of zero PRF(cont signal)
import RPi.GPIO as GPIO
import time

def wavGenerator(pin ,frequency):
    # Set up GPIO mode and pin
    GPIO.setmode(GPIO.BOARD)
    output_pin = pin
    # Calculate the period (in seconds)
    period = 1.0 / frequency

    # Set the initial state of the output pin
    initial_state = GPIO.LOW

    # Configure the GPIO pin as output
    GPIO.setup(output_pin, GPIO.OUT, initial=initial_state)
    
    start_time = time.time()
    end_time = start_time + 10;
    

    # Generate the square wave
    try:
        while time.time() - end_time <= 0:
            GPIO.output(output_pin, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(output_pin, GPIO.LOW)
            time.sleep(period / 2)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()


