from tkinter import *
from sana import mainloop
import webbrowser
import random

# create window
window = Tk()
# title of the window
window.title("Advent Calender")
# window width and height
window.configure(width=700, height=700)
# window background color
window.configure(bg='#9A0000')

# center the window
window.geometry('700x700') 

# text
label = Label(window, text = "Advent Calender", bg='#9A0000')
label.config(font =("Broadway", 30))

# commands
url1 = "https://www.youtube.com/watch?v=E8gmARGvPlI&ab_channel=WhamVEVO"
url2 = "https://fi.wikipedia.org/wiki/Suomen_itsen%C3%A4isyysp%C3%A4iv%C3%A4"
poem = "I’m A Little Snowman \nI’m a little snowman short and fat,\nHere is my scarf and here is my hat.\nWhen I see the snowfall,\nHear me shout “All you children please come out!”"

def open(url):
    webbrowser.open(url)

def openWindow():
    textWindow = Toplevel(window)
    textWindow.geometry("400x400")
    textWindow.title("Day 2")
    textWindow.configure(bg='#173518')
    textlabel = Label(textWindow, text = "2.12.", bg='#173518')
    textlabel.config(font =("Broadway", 50))
    textlabel.pack()
    addPoem = Text(textWindow, height=400, width=400, bg='#173518')
    addPoem.pack()
    addPoem.insert(END,poem)

functions = [open, openWindow, mainloop, open, open, open, open, open, open, open, open, open, open, open, open, open, open, open, open, open, open, open, open]
arguments = [url1, None, None, url1, url1, url1, url1, url1, url1, url2, url2, url2, url2, url2, url2, url2, url2, url2, url2, url2, url2, url2, url2, url2]


# buttons
x = 35
y = 25
day = 1



for j in range(4):
    y=(y+120)
    x=35
    for i in range(6):
        print(arguments[day-1])
        if (arguments[day-1]==None):
            button = Button(window, text = day, bd = 5, bg = "#60100B", activebackground='#173518', height=4, width=6, command= lambda : functions[day-1]())
            button['font'] = 'Broadway'
            if (i <= 6):
                button.place(x=x,y=y)
        else:        
            button = Button(window, text = day, bd = 5, bg = "#60100B", activebackground='#173518', height=4, width=6, command= lambda : functions[day-1](arguments[day-1]))
            button['font'] = 'Broadway'
            if (i <= 6):
                button.place(x=x,y=y)
        x=x+105
        day += 1


label.pack()
window.mainloop()

