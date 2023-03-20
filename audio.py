import pygame
import random
from time import sleep
from config import *

#global variables
file_path = "sounds/"
file_ext = ".wav"
speaker_volume = .1 
prev_sound = "null"

def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load(file_path + file_name + file_ext)
    pygame.mixer.music.play()
    return

def play_audio_loop(file_name, loop):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load(file_path + file_name + file_ext)
    pygame.mixer.music.play(loop)
    return

#This Pi came with a copy of the seinfeld theme song lol
def play_seinfeld():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("sounds/SeinfeldTheme.mp3")
    pygame.mixer.music.play()
    return

def play_finding():
    #Pick random path and play sound
    sound_path = random.randrange(0, 7)
    if sound_path == prev_sound: sound_path = random.randrange(0, 7) # Don't repeat ourselves
    if sound_path == prev_sound: sound_path = random.randrange(0, 7) # Don't repeat ourselves
    if AUDIO_DEBUG: print(sound_path)
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
    return

def play_found():
    #Pick random path and play sound
    sound_path = random.randrange(0, 9)
    if sound_path == prev_sound: sound_path = random.randrange(0, 7) # Don't repeat ourselves
    if AUDIO_DEBUG: print(sound_path)

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
    while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY

    #Play firing sound
    play_audio("turret_fire")
    while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY
    return
