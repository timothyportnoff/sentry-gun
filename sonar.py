# Measure distance using an ultrasonic module
# in a loop.
import time
import RPi.GPIO as GPIO
from config import *

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Speed of sound in cm/s at temperature
temperature = 20
speedSound = 33100 + (0.6*temperature)

# Set pins as output and input
#GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
#GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
#GPIO.output(GPIO_TRIGGER, False)

def measure(GPIO_TRIGGER, GPIO_ECHO):
    # This function measures a distance
    #def DEBUG
    #print("Ultrasonic Measurement: measure()")

    #set trig to high
    GPIO.output(GPIO_TRIGGER, True)

    #After 0.01 ms set trig to low 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start = time.time()
    stop = time.time()

    #save start time
    #print("before start")
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    #print("after stop")

    #save stop time
    #print("before start")
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()
    #print("after stop")

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    #print(distance)
    return distance

def measure_average(GPIO_TRIGGER, GPIO_ECHO):
    # This function takes 3 measurements and returns the average.
    distance1=measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.1)
    distance2=measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.1)
    distance3=measure(GPIO_TRIGGER, GPIO_ECHO)
    
    if SONAR_DEBUG: print("TRIG: {:.0f} ECHO: {:.0f} DIST: {:.2f}".format(distance1,distance1,distance1))
    #((distance1 + distance2 + distance3) / 3)
    return (distance1 + distance2 + distance3) / 3

def measure_better_average(GPIO_TRIGGER, GPIO_ECHO):
    # This function takes 3 measurements and returns the average.
    distance1=measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.001)
    distance2=measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.001)
    distance3=measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.001)
    distance4=measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.001)

    distance5=measure(GPIO_TRIGGER, GPIO_ECHO)
    distance = (distance1 + distance2 + distance3 + distance4 + distance5) / 5
    return distance

# This function takes in a distance and returns a boolean.
def within_sonar_range(CM):
    print("Ultrasonic Measurement: within_sonar_range")
    if measure_average() < CM: return True       #Try 1
    elif measure_average() < CM: return True  #Try 2
    elif measure_average() < CM: return True  #Try 3
    else: return False

if __name__ =="__main__":
    #Hello message
    print("Ultrasonic Measurement: sonar.py")
    print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")
    # Allow module to settle
    # time.sleep(1)

    # Wrap main content in a try block so we can
    # catch the user pressing CTRL-C and run the
    # GPIO cleanup function. This will also prevent
    # the user seeing lots of unnecessary error
    # messages.
    try:
        min = 1000
        while True:
            distance = measure_better_average()
            centimeters = distance
            print("Distance : {0:5.1f}".format(distance), "cm")
            #print "Distance : %.1f" % distance
            if centimeters < min:
                min = centimeters
            time.sleep(1)

    except KeyboardInterrupt:
        # User pressed CTRL-C
      # Reset GPIO settings
      GPIO.cleanup()
