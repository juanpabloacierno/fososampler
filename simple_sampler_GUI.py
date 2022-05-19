from tkinter import *
import pygame

i = 1   # init

root = Tk()
root.title('fososampler')
root.geometry("500x400")

pygame.init()   # init pygame
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=128)     # init mixer
ch1 = pygame.mixer.Channel(0)  # declare channels
ch2 = pygame.mixer.Channel(1)

kick = pygame.mixer.Sound('2.wav')  # sound bank
ton = pygame.mixer.Sound('crovo.wav')

def play1():
    ch1.play(ton)
title = Label(root, text="fososampler", bd=9, relief=GROOVE, font=("Calibri", 50, "bold"), bg="white", fg="green")
title.pack(side=TOP, fill=X)

play_button = Button(root, text="crovo", font=("Calibri", 32), command=play1)
play_button.pack(pady=20)
root.mainloop()
