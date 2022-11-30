import random
from tkinter import *

# create window
window = Tk()
# title of the window
window.title("game time")
# window width and height
window.configure(width=700, height=700)
# window background color
window.configure(bg='#9A0000')

# center the window
window.geometry('700x700') 

# text
label1 = Label(window, text = "Let's start the game!", bg='#9A0000')
label1.config(font =("Broadway", 30))

label2 = Label(window, bg='#FFFFFF')

textEntry = Entry(window)
textEntry.place(relx=0.5, rely=0.5, anchor='center', height=30, width=200)


globalword = ""



def guessTheword():
    # open file
    file = open('C:/Users/venla/Documents/Koodaus/joulukalenteri/joulusanat.txt', 'r')
    # read words from file
    lines = file.read()
    # words to list
    words = lines.split(",")
    # random number
    randomNumber = random.randint(0,(len(words)-1))
    # word for guessing
    guessThis = words[randomNumber]
    # close the file
    file.close()

    # open file
    hintFile = open('C:/Users/venla/Documents/Koodaus/joulukalenteri/vihjeet.txt', 'r')
    # read words from file
    hints = hintFile.read()
    # words to list
    getHint = hints.split(",")
    # word for guessing
    hintForWord = getHint[randomNumber]
    # close the file
    hintFile.close()
    return hintForWord, guessThis

def newWord():
    global globalword
    hint, globalword = guessTheword()
    #label = Label(window, bg='#9A0000')
    label2.config(font =("Consolas", 10), text = hint)
    label2.pack()
    

def check():
    global textEntry, globalword
    guess = textEntry.get()
    print(guess)
    print(globalword)
    if (guess == globalword):
        #label = Label(window, bg='#9A0000')
        label2.config(font =("Consolas", 10), text = "That's correct! Great!")
        label2.pack()
    else:
        #label = Label(window, bg='#9A0000')
        label2.config(font =("Consolas", 10), text="Hmm.. not just that, try again")
        label2.pack()
    return 

def game():

    #buttons
    buttonHint = Button(window, text = "New Word", bd = 5, bg = "#60100B", activebackground='#173518', height=4, width=10, command=newWord)
    buttonHint['font'] = 'Broadway'
    buttonHint.place(x=150,y=100)

    buttonCheck = Button(window, text = "Check", bd = 5, bg = "#60100B", activebackground='#173518', height=4, width=10, command=check)
    buttonCheck['font'] = 'Broadway'  
    buttonCheck.place(x=400,y=100)

    label1.pack()
    window.mainloop()
