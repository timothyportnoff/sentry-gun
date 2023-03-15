import pygame
from time import sleep

#file setup
file_path = "sounds/"
file_ext = ".wav"
speaker_volume = 0.3 

def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load(file_path + file_name + file_ext)
    pygame.mixer.music.play()
    return

def play_audio_loop(file_name, loop):
    #for i in range(loop):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load(file_path + file_name + file_ext)
    pygame.mixer.music.play(loop)
    #sleep(.3)
    return

def play_seinfeld():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("sounds/SeinfeldTheme.mp3")
    pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #    continue
    return

