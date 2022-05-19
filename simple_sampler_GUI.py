from tkinter import *
import mido
import pygame

i = 1   # init

root = Tk()
root.title('fososampler')
root.geometry("500x400")

pygame.init()   #init pygame
pygame.mixer.init()     # init mixer
ch1 = pygame.mixer.Channel(0)  # declare channels
ch2 = pygame.mixer.Channel(1)

kick = pygame.mixer.Sound('2.wav')  # sound bank
ton = pygame.mixer.Sound('5.wav')

port = mido.get_input_names()   # MIDI port names
print(port)
inport = mido.open_input('IAC Driver Bus 1')    # listen port

def play1():
    ch1.play(ton)
title = Label(root, text="fososampler", bd=9, relief=GROOVE,
                font=("times new roman", 50, "bold"), bg="white", fg="green")
title.pack(side=TOP, fill=X)

play_button = Button(root, text="crovo", font=("Helvetica", 32), command=play1)
play_button.pack(pady=20)
root.mainloop()

while i == 1:
    msg = inport.receive()  # create input msg
    if msg.note == 60 and msg.velocity != 0:
        ch1.play(kick)  # play ch 1
        print(f"note {msg.note} dale Cro KICK!")

    if msg.note == 62 and msg.velocity != 0:
        ch2.play(ton)
        print(f"note {msg.note} dale Cro TOM!")





