from tkinter import *
import random

# to make a window of our size
window = Tk()
window.configure(bg='black')
window.geometry('600x400')
window.title("Dice Roller by_GDJ")
window.resizable(0, 0)   # restricts window from maximize/ varying size of window..To make resizable use(1,1)

def roll_dices():
    dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']   # \u2680 unicode for dice with one dot and so on.
    label.configure(text=f'{random.choice(dice_dots)}{random.choice(dice_dots)}')
    label.pack()

roll_button = Button(window, text='Roll!', width=10, height=2, font = 100,bg='cyan', bd=7, command=roll_dices)
roll_button.pack(padx=15, pady=15)
label = Label(window, font=('times', 250), bg='black', fg='yellow')
window.mainloop()