import gpiozero
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

gpiozero.Device.pin_factory=PiGPIOFactory('127.0.0.1')
servo = Servo(25)
def servin_time():
    servo.mid()
    sleep(0.5)
    servo.max()
    sleep(0.5)

