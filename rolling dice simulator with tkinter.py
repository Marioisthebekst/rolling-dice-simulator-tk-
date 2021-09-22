from random import *
from tkinter import *

# setting up the window
WIN= Tk()
WIN.title("Rolling dice simulator")
WIN.geometry("500x250")

# the shape
label = Label(WIN,text='',font=("times",200))

def roll():
        # shapes of the cube (from 1-6)
        nums = ['\u2680','\u2681',"\u2682",'\u2683','\u2684','\u2685']

        # put the 2 dices randomly
        label.config(text=f'{choice(nums)}{choice(nums)}',fg="black")
        # packing all to the middle of the screen
        label.pack()

# putting the text into the window
text = Label(WIN, text='Welcome For Rolling Press Yes')
text.pack()

# setting up the button
# command is the def roll
input_yes = Button(WIN,text="Yes",bg="red",fg="lightskyblue",command=roll)
input_yes.pack()








WIN.mainloop()