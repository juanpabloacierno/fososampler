import mido

import pygame

i = 1
# kick = '2.wav'
# tom = '5.wav'
pygame.init()
pygame.mixer.init()
# mixer.music.load(kick)
ch1 = pygame.mixer.Channel(0) # argument must be int
ch2 = pygame.mixer.Channel(1)

kick = pygame.mixer.Sound('2.wav')
ton = pygame.mixer.Sound('5.wav')

port = mido.get_input_names()  # MIDI port name
print(port)
inport = mido.open_input('IAC Driver Bus 1')

while i == 1:
    msg = inport.receive()
    if msg.note == 60 and msg.velocity != 0:
        ch1.play(kick)
        print(f"note {msg.note} dale Cro KICK!")

    if msg.note == 62 and msg.velocity != 0:
        ch2.play(ton)
        print(f"note {msg.note} dale Cro TOM!")




