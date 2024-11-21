import RPi.GPIO as GPIO
import time
import datetime
import requests

# Set up GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Define the GPIO pin where the button is connected
BUTTON_PIN = 17  # Replace with your button's GPIO pin

# Set up the GPIO pin for the button
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Configures pull-up resistor

# ThingSpeak API setup
channel_id = '2631265'
write_key = 'U25PKZY5K3BYKRH8'
thing_speak_url = f'https://api.thingspeak.com/update?api_key={write_key}'

try:
    while True:
        # Read the button state
        button_state = GPIO.input(BUTTON_PIN)

        # Invert logic if necessary (depends on button wiring)
        # For pull-up configuration: Pressed = 0 (LOW), Released = 1 (HIGH)
        is_pressed = button_state == GPIO.LOW

        # Send the button state to ThingSpeak
        response = requests.get(thing_speak_url, params={'field1': int(is_pressed)})

        # Log the data
        print(f"{datetime.datetime.now()} - Button Pressed: {is_pressed}, Data sent: {response.status_code}")

        # Delay to avoid rapid polling
        time.sleep(1.0)

finally:
    GPIO.cleanup()