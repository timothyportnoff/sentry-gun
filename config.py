
#############################################################################

#DEBUG
MOTOR_DEBUG         = 0
SONAR_DEBUG         = 1
AUDIO_DEBUG         = 0
LED_DEBUG           = 0
FANCY               = 0

#INPUTS
POTENTIOMMETER      = 0
START_BUTTON        = 0 
STOP_BUTTON         = 0
KNOB                = 0
IR                  = 25

#OUTPUTS
GPIO_TRIGGER_1      = 23
GPIO_ECHO_1         = 24
GPIO_TRIGGER_2      = 0
GPIO_ECHO_2         = 0
BUZZER              = 0
MOTOR               = 0

#LED'S
RED                 = 0
YELLOW              = 0
GREEN               = 0
BLUE                = 0

#LASER
LASER_1             = 2

#############################################################################

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

#LASER
GPIO.setup(LASER_1, GPIO.OUT)
