import pygame
#file setup
path = "/home/pi/hammer_time/sounds/"
sound_files = ["SeinFfeldTheme"]


def play_rift():
    pygame.mixer.init()
    speaker_volume = 0.5 
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load("sounds/intro.wav")
    pygame.mixer.music.play()
    return

def play_point():
    pygame.mixer.init()
    speaker_volume = 0.5 
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load("sounds/point.wav")
    pygame.mixer.music.play()
    return

def play_applause():
    pygame.mixer.init()
    speaker_volume = 0.5 
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load("sounds/applause.wav")
    pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #    continue
    return

def play_seinfeld():
    pygame.mixer.init()
    speaker_volume = 0.5 
    pygame.mixer.music.set_volume(speaker_volume)
    pygame.mixer.music.load("sounds/SeinfeldTheme.mp3")
    pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #    continue
    return

