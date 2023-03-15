#Python libs
import RPi.GPIO as GPIO
import threading
import os
import pygame

#Hammer_time libs
from config import *
from time import sleep
from tickets import * 
from led import * 
from sonar import *
from call import *
from audio import *
from motor import * 
#from speaker import * 

if __name__ =="__main__":
    while True:
        #Welcome, and setup
        print("\"It's Hammer Time.\" - MC Hammer")
        #Create threads
        #intro_sound_thread_1 = threading.Thread(target=play_seinfeld)
        #point_sound_thread_1 = threading.Thread(target=play_point)
        #point_sound_thread_2 = threading.Thread(target=play_point)
        #point_sound_thread_3 = threading.Thread(target=play_point)
        #intro_sound_thread_1 .start() 
        #intro_sound_thread_1 .join() 

        if FANCY:
            for i in range(4):
                servin_time()
            light_show_1(RED, YELLOW, GREEN)
        led_off_3(GREEN, YELLOW, RED)

        #Point system
        points = 0

        #while True:
        for i in range(500):
            #check distance
            distance = measure_better_average() 
            #distance = measure_average() 
            print('Distance: ')
            print(distance)
            #print("Distance: %d", %(distance))

            if distance < 92:
                led_on(RED)
                if points < 1:
                    points = 1
                    #point_sound_thread_1 .start() 
                    #point_sound_thread_1 .join() 
            if distance < 62:
                led_on(YELLOW)
                if points < 2:
                    points = 2
                    #point_sound_thread_2 .start() 
                    #point_sound_thread_2 .join() 
            if distance < 32:
                led_on(GREEN)
                if points < 3:
                    points = 3
                    #point_sound_thread_3 .start() 
                    #point_sound_thread_3 .join() 
                    #play_applause()
                break

        if points == 0:
            print("\"Lowly Tarnished. Thou art unfit even to graft.\" - Kerney")
            exit(1)
        elif points == 1:
            TICKETS()
            print_tickets(points)
        elif points == 2:
            TICKETS()
            print_tickets(points)
        elif points == 3:
            if FANCY:
                for i in range(4):
                    servin_time()
                light_show_2(RED, YELLOW, GREEN)
            TICKETS()
            print_tickets(points)

        #Cool off for next game
        sleep(2)
        led_off_3(GREEN, YELLOW, RED)
        print("Game ready in 3.")
        sleep(1)
        print("Game ready in 2.")
        sleep(1)
        print("Game Ready in 1.")
        sleep(1)

    #Exit cleanly
    #TODO
    print("Exiting program.")
    GPIO.cleanup()
