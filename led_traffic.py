import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the LEDs
RED_LED = 14     # Red LED pin
YELLOW_LED = 15  # Yellow LED pin
GREEN_LED = 18   # Green LED pin

# Set up the GPIO pins as outputs
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

# Function to blink an LED
def blink_led(pin, blink_times, delay):
    for _ in range(blink_times):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)

try:
    while True:
        # Step 1: Blink the Red LED (Stop)
        print("Red light blinking (STOP)")
        blink_led(RED_LED, 3, 0.5)  # Blink 3 times with 0.5s delay

        # Step 2: Blink the Yellow LED (Get Ready)
        print("Yellow light blinking (READY)")
        blink_led(YELLOW_LED, 3, 0.5)  # Blink 3 times with 0.5s delay

        # Step 3: Blink the Green LED (Go)
        print("Green light blinking (GO)")
        blink_led(GREEN_LED, 3, 0.5)  # Blink 3 times with 0.5s delay

except KeyboardInterrupt:
    # Cleanup GPIO settings on user interruption
    print("Exiting program...")
    GPIO.cleanup()