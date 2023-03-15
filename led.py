import RPi.GPIO as GPIO
from time import *
from config import *
GPIO.setmode(GPIO.BCM)

def led_on(PIN):
    GPIO.output(PIN, GPIO.HIGH)
    return

def led_off(PIN):
    GPIO.output(PIN, GPIO.LOW)
    return

def led_off_2(PIN1, PIN2):
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)
    return

def led_off_3(PIN1, PIN2, PIN3):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN1, GPIO.OUT)
    GPIO.setup(PIN2, GPIO.OUT)
    GPIO.setup(PIN3, GPIO.OUT)

    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)
    GPIO.output(PIN3, GPIO.LOW)
    return

def blink_led (PIN, ON_TIME, OFF_TIME):
    GPIO.output(PIN, GPIO.HIGH)
    sleep(ON_TIME)
    GPIO.output(PIN, GPIO.LOW)
    sleep(OFF_TIME)
    return

def blink_2_led (PIN1, PIN2, ON_TIME, OFF_TIME):
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN2, GPIO.HIGH)
    sleep(ON_TIME)
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)
    sleep(OFF_TIME)
    return

def blink_3_led (PIN1, PIN2, PIN3, ON_TIME, OFF_TIME):
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN2, GPIO.HIGH)
    GPIO.output(PIN3, GPIO.HIGH)
    sleep(ON_TIME)
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)
    GPIO.output(PIN3, GPIO.LOW)
    sleep(OFF_TIME)
    return
    
def light_show_1(PIN1, PIN2, PIN3):
    led_off_3(PIN1, PIN2, PIN3)

    #blink up
    #blink down 
    blink_led(PIN1, 0.1, 0.1)
    blink_led(PIN2, 0.1, 0.1)
    blink_led(PIN3, 0.1, 0.1)
    blink_led(PIN1, 0.1, 0.1)
    blink_led(PIN2, 0.1, 0.1)
    blink_led(PIN3, 0.1, 0.1)
    blink_led(PIN1, 0.1, 0.1)
    blink_led(PIN2, 0.1, 0.1)
    blink_led(PIN3, 0.1, 0.1)
    blink_led(PIN1, 0.1, 0.1)
    blink_led(PIN2, 0.1, 0.1)
    blink_led(PIN3, 0.1, 0.1)

    #sleep
    sleep(1)

    #Rise to top
    blink_led(PIN1, 0.2, 0.05)
    blink_led(PIN1, 1.0, 0.05)
    blink_2_led(PIN1, PIN2, 0.2, 0.05)
    blink_2_led(PIN1, PIN2, 1.0, 0.05)
    blink_3_led(PIN1, PIN2, PIN3, 0.2, 0.05)
    blink_3_led(PIN1, PIN2, PIN3, 1.0, 0.05)

    #Shut off pins used
    led_off_3(PIN1, PIN2, PIN3)
    return

def light_show_2(PIN1, PIN2, PIN3):
    #led_off_3(PIN1, PIN2, PIN3)

    #Rise to top
    blink_led(PIN3, 0.2, 0.211)
    blink_led(PIN3, 0.2, 0.211)
    blink_led(PIN3, 0.2, 0.211)
    blink_led(PIN3, 0.2, 0.211)
    blink_2_led(PIN3, PIN2, 0.2, 0.211)
    blink_2_led(PIN3, PIN2, 0.2, 0.211)
    blink_2_led(PIN3, PIN2, 0.2, 0.211)
    blink_2_led(PIN3, PIN2, 0.2, 0.211)
    blink_3_led(PIN3, PIN2, PIN1, 0.2, 0.211)
    blink_3_led(PIN3, PIN2, PIN1, 0.2, 0.211)
    blink_3_led(PIN3, PIN2, PIN1, 0.2, 0.211)
    blink_3_led(PIN3, PIN2, PIN1, 0.2, 0.211)

    #Shut off pins used
    led_off_3(PIN1, PIN2, PIN3)
    return
