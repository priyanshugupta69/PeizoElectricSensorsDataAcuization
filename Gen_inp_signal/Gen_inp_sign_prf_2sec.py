#generate input signal for a PRF of 2 seconds
import RPi.GPIO as GPIO
import time

def wavGenerator(pin):
    # Set up GPIO mode and pin
    GPIO.setmode(GPIO.BOARD)
    output_pin = pin

    # Set the frequency (in Hz)
    frequency = 5000

    # Calculate the period (in seconds)
    period = 1.0 / frequency

    # Set the initial state of the output pin
    initial_state = GPIO.LOW

    # Configure the GPIO pin as output
    GPIO.setup(output_pin, GPIO.OUT, initial=initial_state)
    
    start_time = time.time()
    end_time = start_time + 10
    
    # Generate the square wave
    try:
        while time.time() - start_time <= 10:
            if (time.time() - start_time) % 4 < 2:  # Run for 2 seconds, stop for 2 seconds
                GPIO.output(output_pin, GPIO.HIGH)
                time.sleep(period / 2)
                GPIO.output(output_pin, GPIO.LOW)
                time.sleep(period / 2)
            else:
                time.sleep(1)  # Stop for 2 seconds
    except KeyboardInterrupt:
        GPIO.cleanup()

# Usage:
pin = 11  # Change to your desired pin
wavGenerator(pin)
