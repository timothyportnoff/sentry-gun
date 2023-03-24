import pygame
import random
from time import sleep
from config import *

#global variables
file_path = "sounds/"
file_ext = ".wav"
speaker_volume = .10 
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
    global prev_sound
    sounds = ["is_anyone_there", "hi_question", "who's_there", "come_over_here", "hello_question", "canvasing", "searching"]
    sound = sounds[random.randrange(0, len(sounds))]
    while sound == prev_sound: sound = sounds[random.randrange(0, len(sounds))] # Don't repeat ourselves
    prev_sound = sound
    if AUDIO_DEBUG: print(sound_path)
    play_audio(sound)
    return

def play_found():
    #Pick random path and play sound
    global prev_sound
    sounds = ["acquired", "i_see_you", "ahahaha", "firing", "gotcha", "hello", "hellooo", "there_you_are", "hold_still"]
    sound = sounds[random.randrange(0, len(sounds))]
    while sound == prev_sound: sound = sounds[random.randrange(0, len(sounds))] # Don't repeat ourselves
    prev_sound = sound
    if AUDIO_DEBUG: print(sound_path)
    play_audio(sound)
    while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY
    play_audio("turret_fire") #Play firing sound
    while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY
    return

#This is a MUCH better way to print from queue, an array of strings
def play_bye():
    #Pick random path and play sound
    global prev_sound
    sounds= ["goodbye","goodnight","hibernating","resting","nap_time","sleep_mode_activated"]
    sound = sounds[random.randrange(0, len(sounds))]
    while sound == prev_sound: sound = sounds[random.randrange(0, len(sounds))] # Don't repeat ourselves
    prev_sound = sound
    play_audio(sound)
    while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY
    return

def play_picked_up():
    #Pick random path and play sound
    global prev_sound
    sounds = ["help","whoa","wheee","please_put_me_down","put_me_down"]
    sound = sounds[random.randrange(0, len(sounds))]
    while sound == prev_sound: sound = sounds[random.randrange(0, len(sounds))] # Don't repeat ourselves
    prev_sound = sound
    if AUDIO_DEBUG: print(sound)
    play_audio(sound)
    while pygame.mixer.music.get_busy() == True: continue #CHECK TO SEE IF BUSY
    return
