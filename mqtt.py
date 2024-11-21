#sudo apt update && sudo apt install mosquitto mosquitto-clients
#requirements.txt
#python3 -m venv venv
#source venv/bin/activate
#pip install rpi.gpio paho-mqtt

import RPi.GPIO as GPIO 

import paho.mqtt.client as mqtt 

 

# GPIO Setup 

LED_PIN = 4 

GPIO.setmode(GPIO.BCM) 

GPIO.setup(LED_PIN, GPIO.OUT) 

 

# Callback when a message is received 

def on_message(client, userdata, message): 

    payload = message.payload.decode() 

    print(f"Received message: {payload}") 

    if payload == "ON": 

        GPIO.output(LED_PIN, GPIO.HIGH) 

    elif payload == "OFF": 

        GPIO.output(LED_PIN, GPIO.LOW) 

 

# MQTT Setup 

broker_url = "test.mosquitto.org"  # Eclipse Mosquitto public broker 

broker_port = 1883  # Default unencrypted MQTT port 

topic = "group10/home/room/led" 

 

client = mqtt.Client() 

client.connect(broker_url, broker_port) 

client.subscribe(topic) 

 

client.on_message = on_message 

 

# Start MQTT client loop 

client.loop_start() 

 

try: 

    while True: 

        pass  # Keep the script running 

except KeyboardInterrupt: 

    print("Experiment stopped") 

finally: 

    GPIO.cleanup() 

    client.loop_stop()
    
#mosquitto_pub -h test.mosquitto.org -t group10/home/room/led -m "ON"  

#mosquitto_pub -h test.mosquitto.org -t group10/home/room/led -m "OFF"  
