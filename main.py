#Python libs
import RPi.GPIO as GPIO
import threading
import os
PYGAME_HIDE_SUPPORT_PROMPT = 1
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from time import sleep

#Sentry libs
from config import *
from led import * 
from sonar import *
from audio import *
from motor import * 

try:
    if __name__ == "__main__":
        while True:
            #Welcome, and setup
            print("Sentry Mode: Activated.")
            play_audio("sentry_mode_activated")

            #Main Loop:
            while True:
                led_off(RED)
                for i in range(20):
                    distance = measure_better_average(GPIO_TRIGGER_1, GPIO_ECHO_1) #check distance
                    #if DEBUG: print("Sonar 1 Distance: ", distance, ".")
                    if DEBUG: print("Sonar 1 Distance: ", distance, ".")

                    if distance < 50:
                        #Update warning LED  
                        led_on(RED)
                        play_found()
                    #Sleep at the end of the loop. This is a magic number, please adjust.
                    sleep(0.4)
                play_finding()

#Exit cleanly after a keyboard interrupt
except KeyboardInterrupt:
    print("\"Lowly Tarnished. Thou art unfit even to graft.\" - Kerney")
    #led_off_3(GREEN, YELLOW, RED)
    GPIO.cleanup()
    print("Exiting program.")
