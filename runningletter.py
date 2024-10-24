from tkinter import *
from time import *

window=Tk()
window.geometry('500x300+250+600')

counting = 0
wordtext = ''

def runningword():
    global counting, wordtext
    if counting == len(theword):
        counting = 0
        wordtext = ''
    
    
    
    wordtext = wordtext + theword[counting]
    thewordLabel.config(text=wordtext)
    counting +=1
    thewordLabel.after(200,runningword)





theword = 'Lorem ipsum dolor sit amet'
thewordLabel = Label (window, text= theword)
thewordLabel.grid(row=0,column = 0)
runningword()




window.mainloop()




















