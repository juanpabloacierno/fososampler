import mido

import pygame

i = 1   # init

pygame.init()   #init pygame
pygame.mixer.init(frequency=44100, size= -16, channels=2, buffer=128)     # init mixer w/parameters
ch1 = pygame.mixer.Channel(0)  # declare N channels
ch2 = pygame.mixer.Channel(1)

kick = pygame.mixer.Sound('audio/2.wav')  # sound bank
ton = pygame.mixer.Sound('audio/5.wav')

port = mido.get_input_names()   # MIDI port names
print(port)
inport = mido.open_input('IAC Driver Bus 1')    # listen port

while i == 1:
    msg = inport.receive()  # create input msg
    if msg.note == 60 and msg.velocity != 0:
        ch1.play(kick)  # play ch 1
        print(f"note {msg.note} dale Cro KICK!")

    if msg.note == 62 and msg.velocity != 0:
        ch2.play(ton)
        print(f"note {msg.note} dale Cro TOM!")




