import random
from tkinter import *

root = Tk()
root.geometry("700x450")

text_1 = Label(root, text='', font=("times", 200))

def roll_the_dice():
        number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        text_1.config(text=f'{random.choice(number)}{random.choice(number)}')
        text_1.pack()

        b_1 = Button(root, text="Roll the dice", command=roll_the_dice)
        b_1.place(x=330, y=0)

root.mainloop()
