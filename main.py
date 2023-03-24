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

i = 0
try:
    if __name__ == "__main__":
        while True:
            #Welcome, and setup
            print("Sentry Mode: Activated.")
            setup()
            play_audio("sentry_mode_activated") #Disable if repetitive 
            while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY
            led_off(LASER_1) #TURN ON LASER_1 *not a mistake*

            #Main Loop:
            while True:
                play_finding()
                #TODO Add motor direction boolean
                for i in range(40):
                    #Turn motor
                    if i < 8:
                        clockwise(1, 0.005)
                    elif i < 12:
                        pass
                    elif i < 28:
                        cclockwise(1, 0.005)
                    elif i < 32:
                        pass
                    else:
                        clockwise(1, 0.005)

                    #Occasional Sentry Beep
                    if i == 10: play_audio("turret_deploy")
                    if i == 17: play_audio("turret_retract")

                    #If sentry is picked up off ground
                    distance2 = measure_average(GPIO_TRIGGER_2, GPIO_ECHO_2) #check distance
                    if distance2 > 25 and distance2 < 150:
                        play_picked_up()
                        sleep(1.5)
                        play_audio("turret_ping")
                        sleep(0.5)
                        continue

                    #If there is a target within range
                    distance1 = measure_average(GPIO_TRIGGER_1, GPIO_ECHO_1) #check distance
                    if distance1 < 100:
                        play_found()
                        continue

                    sleep(0.1) #Sleep at the end of the loop. This is a magic number, please adjust.

#Exit cleanly after a keyboard interrupt
except KeyboardInterrupt:
    #Return to center
    if i < 20:
        if i > 8 and i < 12: i = 8
        if i > 8: i = i - 8
        while i > 0:
            cclockwise(1, 0.05)
            i = i-1
    else:
        i = i-20
        if i > 8 and i < 12: i = 8
        if i > 8: i = i - 8
        while i > 0:
            clockwise(1, 0.05)
            i = i-1

    destroy()
