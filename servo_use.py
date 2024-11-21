import requests
import RPi.GPIO as GPIO
import time

# ThingSpeak API details
CHANNEL_ID = '2641846'
READ_API_KEY = '0P4DTGO73GLJZHAK'
FIELD_NUMBER = 1

# GPIO setup
Servo_Pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_Pin, GPIO.OUT)

# Set PWM frequency to 50Hz (standard for servos) 
pwm = GPIO.PWM(SERVO_PIN, 50) 
pwm.start(0) # Initialize PWM with a 0% duty cycle (no signal)

def get_field_data():
    # Construct the URL to fetch data from ThingSpeak
    url =
f'https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{FIELD_NUMBER}/last.json?api_key={READ_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['field' + str(FIELD_NUMBER)]
    else:
        print("Failed to retrieve data")
        return None

def set_servo_angle(angle): 
    duty = 2 + (angle / 18) # Convert angle to duty cycle 
    pwm.ChangeDutyCycle(duty) 
    time.sleep(1)
    pwm.ChangeDutyCycle(0) # Stop sending signals to hold the position

try:
    while True:
        field_data = get_field_data()
        if field_data is not None:
            print(f"Field {FIELD_NUMBER} data: {field_data}")
	angle = int(field_data) 
if angle == 0: 
    pwm.ChangeDutyCycle(0) # No signal when angle is 0 
elif 0 < angle <= 180: # Ensure the angle is within the valid range for the servo   
    set_servo_angle(angle)
        time.sleep(10)  # Delay before fetching data again
except KeyboardInterrupt:
    print("Program stopped")
finally:
    pwm.stop() 
    GPIO.cleanup()
