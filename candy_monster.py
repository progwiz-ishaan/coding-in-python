# The Candy Monster Game program:
from tkinter import *
import random

# make window
window = Tk()
window.title("The Candy Monster Game")

# create a canvas to put objects on the screen
canvas = Canvas(window, width=400, height=400, bg='black')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text='The Candy Monster',\
 fill='white', font=('Helvetica', 30))
directions = canvas.create_text(200, 300, text='Collect Candy but no red ones\
', fill='white', font=('Helvetica', 20))

# set up score display using label wiget
score = 0
score_display = Label(window, text='Score: ' + str(score))
score_display.pack()

# set up level display using label wiget
level = 1
level_display = Label(window, text='Level: ' + str(level))
level_display.pack()

# create an image object using the .gif file
player_image = PhotoImage(file='/home/ishaan/Documents/Ishaan\'s-Coding/coding\
-in-python/greenChar.gif')
# use image object to create a character at position 200, 360
my_char = canvas.create_image(200, 360, image=player_image)

window.mainloop() # last line is the GUI main event loop