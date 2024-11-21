#requirements.txt
#python3 -m venv venv
#source venv/bin/activate
#pip install adafruit-circuitpython-dht
import time 

import board 

import adafruit_dht 

import requests 

 

# Sensor data pin is connected to GPIO 4 

sensor = adafruit_dht.DHT11(board.D4) 

 

# Your ThingSpeak Channel ID and Write API Key 

THINGSPEAK_CHANNEL_ID = 2640576 

THINGSPEAK_API_KEY = "PA5R4TABBHXE7FB8" 

THINGSPEAK_URL = "https://api.thingspeak.com/update" 

 

while True: 

    try: 

        # Read the sensor data 

        temperature_c = sensor.temperature 

        temperature_f = temperature_c * (9 / 5) + 32 

        humidity = sensor.humidity 

        print("time:",time.strftime("%H:%M:%S", time.localtime())) 

        print("Temp={0:0.1f}C, Temp={1:0.1f}F, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity)) 

 

        # Send data to ThingSpeak 

        response = requests.get(THINGSPEAK_URL, params={ 

            'api_key': THINGSPEAK_API_KEY, 

            'field2': temperature_c, 

            'field3': humidity, 

    'field1': time.strftime("%H:%M:%S", time.localtime()) 

        }) 

 

        if response.status_code == 200: 

            print("Data successfully sent to ThingSpeak.") 

        else: 

            print(f"Failed to send data to ThingSpeak. Status code: {response.status_code}") 

 

    except RuntimeError as error: 

        # Errors happen fairly often with DHT sensors, just keep going 

        print(error.args[0]) 

        time.sleep(2.0) 

        continue 

    except Exception as error: 

        sensor.exit() 

        raise error 

 

    time.sleep(15.0)  # ThingSpeak rate limit for free accounts 
