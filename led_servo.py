import RPi.GPIO as GPIO
import requests
import time

# Setup GPIO pins
LED_PIN = 4
SERVO_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Servo PWM setup
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency
pwm.start(0)

# ThingSpeak API details
CHANNEL_ID = '2645560'
WRITE_API_KEY = 'EJIYPQM5L6F7LFL0'
READ_API_KEY = 'QN0JI6YSFBU4J4VO'
READ_API_URL = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1'

def set_led(state):
    GPIO.output(LED_PIN, GPIO.HIGH if state == '1' else GPIO.LOW)

def set_servo(angle):
    duty = 2 + (angle / 18)
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        response = requests.get(READ_API_URL)
        data = response.json()
        led_state = data['feeds'][0]['field1']
        servo_angle = int(data['feeds'][0]['field2'])

        set_led(led_state)
        set_servo(servo_angle)

        time.sleep(15)  # Wait before the next update
except KeyboardInterrupt:
    print("Experiment stopped")
finally:
    pwm.stop()
    GPIO.cleanup()
