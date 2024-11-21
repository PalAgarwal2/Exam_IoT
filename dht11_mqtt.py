import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt
import time

# GPIO setup for DHT11
DHT_PIN = 4 

# Initialize GPIO and DHT11 instance
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dht_sensor = dht11.DHT11(pin=DHT_PIN)

# MQTT Setup
broker_url = "test.mosquitto.org"
broker_port = 1883
publish_topic = "home/room/sensor"  # Topic to publish sensor data

# MQTT client setup
client = mqtt.Client()
client.connect(broker_url, broker_port)

# Start MQTT client loop
client.loop_start()

try:
    while True:
        # Read data from the DHT11 sensor
        result = dht_sensor.read()
        
        if result.is_valid():
            temperature = result.temperature
            humidity = result.humidity
            
            # Create payload with sensor data
            sensor_data = f"Temperature: {temperature:.1f}C, Humidity: {humidity:.1f}%"
            print(sensor_data)
            
            # Publish the sensor data to the MQTT topic
            client.publish(publish_topic, sensor_data)
        else:
            print("Failed to retrieve data from DHT11 sensor")
        
        time.sleep(2)  # Delay to avoid flooding with messages
except KeyboardInterrupt:
    print("Experiment stopped")
finally:
    GPIO.cleanup()
    client.loop_stop()