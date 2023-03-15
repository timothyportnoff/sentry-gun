#Python libs
import RPi.GPIO as GPIO
import threading
import os
import pygame
import random

#Sentry libs
from config import *
from time import sleep
from led import * 
from sonar import *
from audio import *
from motor import * 

try:
    if __name__ == "__main__":
        while True:
            #Welcome, and setup
            print("Sentry Mode: Activated.")

            #Start audio
            play_audio("sentry_mode_activated")
            prev_sound = "null"

            #Main Loop:
            while True:
                led_off(RED)
                for i in range(20):
                    print('Measure: ')
                    distance = measure_better_average(GPIO_TRIGGER_1, GPIO_ECHO_1) #check distance
                    if DEBUG: print('Sonar 1 Distance: ', distance, '.')

                    if distance < 50:
                        #Update warning LED  
                        led_on(RED)

                        #Pick random path and play sound
                        sound_path = random.randrange(0, 9)

                        #print(sound_path)
                        if sound_path == 0:
                            play_audio("acquired")
                        elif sound_path == 1:
                            play_audio("i_see_you")
                        elif sound_path == 2:
                            play_audio("ahahaha")
                        elif sound_path == 3:
                            play_audio("firing")
                        elif sound_path == 4:
                            play_audio("gotcha")
                        elif sound_path == 5:
                            play_audio("hello")
                        elif sound_path == 6:
                            play_audio("hellooo")
                        elif sound_path == 7:
                            play_audio("there_you_are")
                        elif sound_path == 8:
                            play_audio("hold_still")
                        sleep(2)

                        #Play firing sound
                        #play_audio_loop("fire", 10)
                        play_audio("turret_fire")
                        sleep(3)
                    #Sleep at the end of the loop. This is a magic number, please adjust.
                    sleep(0.4)
                #Pick random path and play sound
                sound_path = random.randrange(0, 7)
                if sound_path == prev_sound: sound_path = random.randrange(0, 7)
                #print(sound_path)
                if sound_path == 0:
                    play_audio("is_anyone_there")
                elif sound_path == 1:
                    play_audio("hi_question")
                elif sound_path == 2:
                    play_audio("who's_there")
                elif sound_path == 3:
                    play_audio("come_over_here")
                elif sound_path == 4:
                    play_audio("hello_question")
                elif sound_path == 5:
                    play_audio("canvasing")
                elif sound_path == 6:
                    play_audio("searching")

#Exit cleanly after a keyboard interrupt
except KeyboardInterrupt:
    print("\"Lowly Tarnished. Thou art unfit even to graft.\" - Kerney")
    #led_off_3(GREEN, YELLOW, RED)
    GPIO.cleanup()
    print("Exiting program.")
