import pygame
from pygame import mixer

pygame.init()
# dimensions
WITH = 1400
HEIGHT = 800
# colores
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)
tickness1 = 5

# create screen
screen = pygame.display.set_mode([WITH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)
# init mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=128)
ch1 = pygame.mixer.Channel(0)
ch2 = pygame.mixer.Channel(1)
ch3 = pygame.mixer.Channel(2)
ch4 = pygame.mixer.Channel(3)
ch5 = pygame.mixer.Channel(4)
ch6 = pygame.mixer.Channel(5)

fps = 60
# MASTER CLOCK
timer = pygame.time.Clock()
instruments = 6
beats = 8
boxes = []
# negative coordenates list
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 1
beat_changed = True
image = pygame.image.load('crovo.png')

# --- LOAD IN SOUNDS ---
hi_hat = mixer.Sound('sounds/hi hat.wav')
snare = mixer.Sound('sounds/snare.wav')
kick = mixer.Sound('sounds/kick.wav')
crash = mixer.Sound('sounds/crash.wav')
clap = mixer.Sound('sounds/clap.wav')
tom = mixer.Sound('sounds/tom.wav')
pygame.mixer.set_num_channels(instruments * 3)


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                ch1.play(hi_hat)
            if i == 1:
                ch2.play(snare)
            if i == 2:
                ch3.play(kick)
            if i == 3:
                ch4.play(crash)
            if i == 4:
                ch5.play(clap)
            if i == 5:
                ch6.play(tom)


def draw_grid(clicks, beat):
    # left box-Arguments (x, y, with, height, tick)
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT], tickness1)
    botton_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WITH, 200], tickness1)
    boxes = []  # steps
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    tom_text = label_font.render('Tom', True, white)
    screen.blit(tom_text, (30, 530))

    for i in range(instruments):
        # surface, color, start position (x, y), end position, with
        pygame.draw.line(screen, gray, (0, i * 100), (200, i * 100), tickness1)
    # NESTED Loop
    for i in range(beats):
        for j in range(instruments):
            # if we get negative click, the color is grey
            if clicks[j][i] == -1:
                color = gray
            # if the click is positive, color will be green
            else:
                color = green

            rect = pygame.draw.rect(screen, color,  # TEST --> print(f"i: {i}  j: {j}  rect: {rect}")
                                    [i * ((WITH - 200) // beats) + 205,  # initial position (x axis)
                                     (j * 100) + 5,  # initial position (y axis)
                                     (WITH - 200) // beats - 10,  # with a bias
                                     ((HEIGHT - 200) // instruments) - 10],  # high
                                    0, 3)

            pygame.draw.rect(screen, gold, [i * ((WITH - 200) // beats) + 200, (j * 100), ((WITH - 200)) // beats,
                                            ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black, [i * ((WITH - 200) // beats) + 200, (j * 100), ((WITH - 200)) // beats,
                                             ((HEIGHT - 200) // instruments)], 3, 5)
            if color == green:
                x_img = i * ((WITH - 200) // beats) + 205
                y_img = (j * 100) + 5
                screen.blit(image, (x_img, y_img))

            # this list box was empty. So it add boxes as a list
            boxes.append((rect, (i, j)))
        active = pygame.draw.rect(screen, blue,
                                  [beat * ((WITH - 200) // beats) + 200, 0, ((WITH - 200) // beats), instruments * 100],
                                  5, 3)
    return boxes


# start the game
run = True
while run:
    timer.tick(fps)
    # meanwhile the game is ON, fill the screen
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat)
    if beat_changed:
        play_notes()
        beat_changed = False
    # check if someone is pressing a key, mouse, etc (every event)
    for event in pygame.event.get():
        # if some quit, stop the game
        if event.type == pygame.QUIT:
            run = False
        # if someone down the mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # in range of boxes = beats (0 - 47) (only if mousebuttondown is True)
            for i in range(len(boxes)):
                # TRUE if the mouse is inside the rectangle / event.pos get mouse pointer on screen (x, y)
                if boxes[i][0].collidepoint(event.pos):
                    # get coordinates (not pixels, instead boxes cells) on every click
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
    # 3600 = fps * 60 sec
    beat_length = 3600 // bpm

    # THIS SECTION IS A BEAT COUNTER
    if playing:
        # if active length is less than beat_length...
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                # beat count 1 2 3 4...
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True
    pygame.display.flip()
pygame.quit()