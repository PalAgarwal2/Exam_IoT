#requirements.txt
#python3 -m venv venv
#source venv/bin/activate
#pip install rpi.gpio

import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the LED and the button
LED_PIN = 4
BUTTON_PIN = 21

# Set up the GPIO pins
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the button
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:  # Button is pressed
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        time.sleep(0.1)  # Small delay to debounce the button
except KeyboardInterrupt:
    GPIO.cleanup()

