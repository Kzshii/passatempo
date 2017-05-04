import tkinter
rel = tkinter.Label()
rel.pack()
rel['font']= 'Arial 30 bold'
from time import strftime
strftime('%H:%M:%S')
def tic():
    rel['text']=strftime('%H:%M:%S')
def tac():
    tic()
    rel.after(1000, tac)
tac()
    
