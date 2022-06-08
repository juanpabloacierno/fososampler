import pygame
from pygame import mixer

pygame.init()
# dimensions
WIDTH = 1400
HEIGHT = 800
# colores
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)
tickness1 = 5

<<<<<<< HEAD
# create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
=======
#create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])                        
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)

# initial BPM
bpm = 240
# Frame rate
fps = 60
# MASTER CLOCK
timer = pygame.time.Clock()
# number of instruments
<<<<<<< HEAD
instruments = 6
=======
instruments = 6                                                                 
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
# beats number
beats = 8
boxes = []
# negative coordenates list
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
playing = True
active_length = 0
active_beat = 1
beat_changed = True

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
                pygame.mixer.Channel(0).play(hi_hat)
            if i == 1:
                pygame.mixer.Channel(1).play(snare)
            if i == 2:
                pygame.mixer.Channel(2).play(kick)
            if i == 3:
                pygame.mixer.Channel(3).play(crash)
            if i == 4:
                pygame.mixer.Channel(4).play(clap)
            if i == 5:
                pygame.mixer.Channel(5).play(tom)


def draw_grid(clicks, beat):
    # left box-Arguments (x, y, wiDth, height, tick)
<<<<<<< HEAD
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT], tickness1)

    botton_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], tickness1)

=======
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT], tickness1)           
    
    botton_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], tickness1)
    
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
    # steps
    boxes = []
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
<<<<<<< HEAD
        # surface, color, start position (x, y), end position, wiDth
=======
        #surface, color, start position (x, y), end position, wiDth
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
        pygame.draw.line(screen, gray, (0, i * 100), (200, i * 100), tickness1)
    for i in range(beats):
        for j in range(instruments):
            # if we get negative click, the color is grey
<<<<<<< HEAD
            if clicks[j][i] == -1:
=======
            if clicks[j][i] == -1:                                          
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
                color = gray
            # else the click is positive, color will be green
            else:
                color = green
            rect = pygame.draw.rect(screen, color,
<<<<<<< HEAD
                                    [i * ((WIDTH - 200) // beats) + 205,  # initial position (x axis)
                                     (j * 100) + 5,  # initial position (y axis)
                                     (WIDTH - 200) // beats - 10,  # width width a bias
                                     ((HEIGHT - 200) // instruments) - 10],  # high
                                    0, 3)
            pygame.draw.rect(screen, gold, [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200)) // beats,
                                            ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black, [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200)) // beats,
                                             ((HEIGHT - 200) // instruments)], 3, 5)

            # this list box was empty. So it add boxes as a list
            boxes.append((rect, (i, j)))
        active = pygame.draw.rect(screen, blue, [beat * ((WIDTH - 200) // beats) + 200, 0, ((WIDTH - 200) // beats),
                                                 instruments * 100], 5, 3)
    return boxes


run = True
=======
                                    [i * ((WIDTH - 200) // beats) + 205,        # initial position (x axis)
                                    (j * 100) + 5,                              # initial position (y axis)
                                    (WIDTH - 200) // beats - 10,                # width width a bias
                                    ((HEIGHT - 200) // instruments) - 10],      # high
                                    0, 3)
            pygame.draw.rect(screen, gold,[i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200)) // beats, ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black, [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200)) // beats, ((HEIGHT - 200) // instruments)], 3, 5)

            # this list box was empty. So it add boxes as a list
            boxes.append((rect, (i, j)))                                        
        active = pygame.draw.rect(screen, blue, [beat * ((WIDTH - 200) // beats) + 200, 0,((WIDTH - 200) // beats), instruments * 100], 5, 3)
    return boxes


run = True                                                                  
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e

# start the game
while run:
    timer.tick(fps)
    # meanwhile the game is ON, fill the screen
<<<<<<< HEAD
    screen.fill(black)

=======
    screen.fill(black)                                                          
    
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
    boxes = draw_grid(clicked, active_beat)
    if beat_changed:
        play_notes()
        beat_changed = False
        # print(play_notes())

    # check if someone is pressing a key, mouse, etc (every event)
<<<<<<< HEAD
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
                    # get coordenates (not pixels, instead boxes cells) on every click
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

    # 3600 = fps * 60 sec
    beat_length = 3600 // bpm

    # THIS SECTION IS A BEAT COUNTER
    if playing:
        # if active length is less than beat_length...
        if active_length < beat_length:
=======
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
                    # get coordenates (not pixels, instead boxes cells) on every click
                    coords = boxes[i][1]                                        
                    clicked[coords[1]][coords[0]] *= -1

    # 3600 = fps * 60 sec
    beat_length = 3600 // bpm                                                   

    # THIS SECTION IS A BEAT COUNTER
    if playing:                                                                 
        # if active length is less than beat_length...
        if active_length < beat_length:                                         
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                # beat count 1 2 3 4...
<<<<<<< HEAD
                active_beat += 1
=======
                active_beat += 1                                                
>>>>>>> 21df13fa4e77cb45c2bee494394a9b3716fcf75e
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True
    pygame.display.flip()
pygame.quit()