import pygame

pygame.init()  # init pygame

size = (250, 250)
screen = pygame.display.set_mode(size)

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=128)  # init mixer
ch1 = pygame.mixer.Channel(0)  # declare channels
ch2 = pygame.mixer.Channel(1)
ch3 = pygame.mixer.Channel(2)

a1 = pygame.mixer.Sound('site/assets/audio/2.wav')  # sound bank
a2 = pygame.mixer.Sound('site/assets/audio/dale.wav')
a3 = pygame.mixer.Sound('site/assets/audio/crovo.wav')

def play_1():
    ch1.play(a1)
def play_2():
    ch2.play(a2)
def play_3():
    ch3.play(a3)

while True:
    pygame.time.Clock().tick(10)
    # print("Press '1' to play audio_1, '2' to play audio_2, '3' to play audio_3")
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # print(query)

    if keys[pygame.K_1]:
        play_1()

    elif keys[pygame.K_2]:
        play_2()

    elif keys[pygame.K_3]:
        play_3()
