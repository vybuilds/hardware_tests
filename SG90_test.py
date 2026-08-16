from gpiozero import Servo
from time import sleep

servo = Servo(18)

print("Moving to center")
servo.mid()
sleep(2)

print("Moving to minimum")
servo.min()
sleep(2)

print("Moving to maximum")
servo.max()
sleep(2)

print("Returning to center")
servo.mid()
sleep(2)

print("Test complete")
