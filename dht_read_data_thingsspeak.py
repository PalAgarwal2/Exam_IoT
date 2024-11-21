#requirements.txt
#python3 -m venv venv
#source venv/bin/activate
#pip install adafruit-circuitpython-dht
import time 

import board 

import adafruit_dht 

import requests 

import json 

import RPi.GPIO as GPIO 

 

led_pin = 21 

GPIO.setup(led_pin,GPIO.OUT) 

 

# Sensor data pin is connected to GPIO 4 

sensor = adafruit_dht.DHT11(board.D4) 

 

# Your ThingSpeak Channel ID and Write API Key 

THINGSPEAK_CHANNEL_ID = 2640572 

THINGSPEAK_API_KEY = "4N6U7YY8JQWCI32G" 

THINGSPEAK_URL = "https://api.thingspeak.com/channels/2640572/fields/3.json?api_key=4N6U7YY8JQWCI32G&results=1" 

 

while True: 

    try: 

        TS=requests.get(THINGSPEAK_URL) 

         

        if TS.status_code == 200: 

            response = TS.text 

            data=json.loads(response) 

            val = data['feeds'][0]['field3'] 

             

            if val != "0": 

                GPIO.output(led_pin , GPIO.HIGH) 

                print("led glow") 

            else: 

                GPIO.output(led_pin , GPIO.LOW) 

                print("led not glow") 

            time.sleep(1) 

             

        else: 

            print(f"Failed to send data to ThingSpeak. Status code: {response.status_code}") 

         

 

    except KeyboardInterrupt: 

        # Errors happen fairly often with DHT sensors, just keep going 

        print("Controldvsbjvd ") 

        GPIO.cleanup() 

 
