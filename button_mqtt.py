import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

# GPIO Pin setup
BUTTON_PIN = 17  # GPIO pin connected to the button
LED_PIN = 18     # GPIO pin connected to the LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set button as input with pull-down resistor
GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED as output

# MQTT Setup
broker_url = "test.mosquitto.org"
broker_port = 1883
subscribe_topic = "home/room/led_control"  # Topic for LED control

# Initialize LED state
led_should_glow = False

# Callback for receiving MQTT messages
def on_message(client, userdata, message):
    global led_should_glow
    payload = message.payload.decode()
    print(f"Received message: {payload}")
    if payload == "ON":
        led_should_glow = True
    elif payload == "OFF":
        led_should_glow = False

# MQTT client setup
client = mqtt.Client()
client.on_message = on_message
client.connect(broker_url, broker_port)
client.subscribe(subscribe_topic)

# Start MQTT client loop
client.loop_start()

try:
    while True:
        # Check if button is pressed
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:  # Button is pressed
            if led_should_glow:
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
                print("LED is ON")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED when button isn't pressed
        
        time.sleep(0.1)  # Short delay to avoid bouncing issues
except KeyboardInterrupt:
    print("Experiment stopped")
finally:
    GPIO.cleanup()
    client.loop_stop()