#DEBUG
DEBUG = 1

#INPUT
POTENTIOMMETER  = 0
START_BUTTON    = 26
STOP_BUTTON     = 0
#KNOB           = 0
GPIO_TRIGGER    = 23
GPIO_ECHO       = 24

#OUTPUT
BUZZER      = 0
#MOTOR      = 0

#LED'S
FANCY   = 1
RED     = 4
YELLOW  = 3
GREEN   = 2
#BLUE   = 0

#############################################################################

#GPIO settings
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#LEDS
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
