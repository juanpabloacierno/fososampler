# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

import pygame

lst = [
'2.wav',   # key 1
'5.wav',  # key 2
'crovo.wav' # key 3
]

pygame.init()
size = (250, 250)
screen = pygame.display.set_mode(size)

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=128)
print("channel cnt",pygame.mixer.get_num_channels()) # max track count (8 on my machine)

while True:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    idx = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]: idx = 1
    if keys[pygame.K_2]: idx = 2
    if keys[pygame.K_3]: idx = 3
    if (idx):
       ch = pygame.mixer.find_channel() # find open channel, returns None if all channels used
       snd = pygame.mixer.Sound(lst[idx-1])  # create sound object, must be wav or ogg
       if (ch): ch.play(snd)  # play on channel if available