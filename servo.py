#requirements.txt
#python3 -m venv venv
#source venv/bin/activate
#pip install rpi.gpio gpiozero
from gpiozero import Servo
from time import sleep

servo = Servo(25)

try:
	while True:
    		servo.min()
    		sleep(0.5)
    		servo.mid()
    		sleep(0.5)
    		servo.max()
    		sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")
from gpiozero import Servo
from time import sleep

servo = Servo(25)
val = -1

try:
	while True:
    		servo.value = val
    		sleep(0.1)
    		val = val + 0.1
    		if val > 1:
        		val = -1
except KeyboardInterrupt:
	print("Program stopped")
