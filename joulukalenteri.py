from tkinter import *
from sana import main
from PIL import Image
from taikinaohje import mainDough
from christmascard import mainCard
import webbrowser
import turtle


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

# coordinates
x = 35
y = 25

# day
day = 1

# commands
url1 = "https://www.youtube.com/watch?v=E8gmARGvPlI&ab_channel=WhamVEVO"
url2 = "https://fi.wikipedia.org/wiki/Suomen_itsen%C3%A4isyysp%C3%A4iv%C3%A4"
url3 = "https://www.youtube.com/watch?v=aAkMkVFwAoo&ab_channel=MariahCareyVEVO"
url4 = "https://www.youtube.com/watch?v=fyEAX7Cd3OE&ab_channel=7clouds"
url5 = "https://areena.yle.fi/1-50628566"

poem = "I’m A Little Snowman \nI’m a little snowman short and fat,\nHere is my scarf and here is my hat.\nWhen I see the snowfall,\nHear me shout “All you children please come out!”"

pic1 = Image.open('C:/Users/venla/Documents/Koodaus/advent_calendar/kuusi.jpg')
pic2 = Image.open('C:/Users/venla/Documents/Koodaus/advent_calendar/joulu.jpg')

# write text with turtle
def write():
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(0,0)
    turtle.bgcolor("red")
    turtle.color("black")
    turtle.write("Hey, it's only a few days until christmas!", font=("Consolas", 12), align="center")

# function for opening pictures
def openPic(pic):
    pic.show()

# function for opening web sites
def open(url):
    webbrowser.open(url)

# function for opening a new window with text
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


# list of functions and arguments
functions = [open, openWindow, main, open, open, open, openPic, write, open, mainDough, None, openPic, None, None, main, None, None, None, mainCard, None, None, None, None, None]
arguments = [url1, None, None, url3, url4, url2, pic1, None, url5, None, None, pic2, None, None, None, None, None, None, None, None, None, None, None, None]

# loop for creating grid and buttons

for j in range(4):
    y=(y+120)
    x=35
    for i in range(6):
        if (arguments[day-1]==None):
            button = Button(window, text = day, bd = 5, bg = "#60100B", activebackground='#173518', height=4, width=6, command= lambda day=day: functions[day-1]())
            button['font'] = 'Broadway'
            if (i <= 6):
                button.place(x=x,y=y)
        else:        
            button = Button(window, text = day, bd = 5, bg = "#60100B", activebackground='#173518', height=4, width=6, command= lambda day=day: functions[day-1](arguments[day-1]))
            button['font'] = 'Broadway'
            if (i <= 6):
                button.place(x=x,y=y)
        x=x+105
        day += 1


label.pack()
window.mainloop()

