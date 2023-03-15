#DEBUG
DEBUG               = 1
FANCY               = 1

#INPUT
POTENTIOMMETER      = 0
START_BUTTON        = 26
STOP_BUTTON         = 0
#KNOB               = 0

#SONAR
GPIO_TRIGGER_1      = 23
GPIO_ECHO_1         = 24
GPIO_TRIGGER_2      = 0
GPIO_ECHO_2         = 0

#OUTPUT
BUZZER              = 0
#MOTOR              = 0

#LED'S
RED                 = 0
YELLOW              = 0
GREEN               = 0
BLUE                = 0

#############################################################################
import os

#PYGAME settings
PYGAME_HIDE_SUPPORT_PROMPT = 0
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#GPIO settings
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LEDS
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

#SONAR
GPIO.setup(GPIO_TRIGGER_1,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_1,GPIO.IN)      # Echo

#MOTOR
#MOTOR1
#MOTOR2
