from tkinter import *

def readFile():
    # open file
    dough = open('C:/Users/venla/Documents/Koodaus/advent_calendar/piparit.txt', 'r')
    # read lines from file
    lines = dough.read()
    # words to list
    words = lines.split(",")
    
    # random number
    dough.close()

    # open file
    instructions = open('C:/Users/venla/Documents/Koodaus/advent_calendar/pipariohje.txt', 'r')
    # read lines from file
    doThis = instructions.read()
    
    doThis = doThis.split("\n")
    
    # close the file
    instructions.close()
    return words, doThis

def mainDough():
    global window
    # create window
    window = Tk()
    # title of the window
    window.title("Piparitaikina")
    # window width and height
    window.configure(width=700, height=700)
    # window background color
    window.configure(bg='#9A0000')

    # center the window
    window.geometry('700x700') 
    needs, whatToDo = readFile()
    
    label = Label(window, text = "Piparit", bg='#9A0000')
    label.config(font =("Broadway", 30))

    tarvikkeet = Message(window, text = '\n'.join(needs), bg='#9A0000')
    tarvikkeet.config(font =("Broadway", 10))
    
    ohje = Message(window, text ='\n'.join(whatToDo), bg='#9A0000')
    ohje.config(font =("Broadway", 10))
    
    label.pack()
    tarvikkeet.pack()
    ohje.pack()
    window.mainloop()
