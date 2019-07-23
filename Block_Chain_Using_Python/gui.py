##########################################################################################################
# Libraries
##########################################################################################################


import tkinter # To import library so that i can work with gui.
from tkinter import * 
from tkinter import messagebox


##########################################################################################################
# GLOBAL VARIABLES
##########################################################################################################


top = tkinter.Tk()


##########################################################################################################
# FUNCTIONS
##########################################################################################################


def donothing():
   filewin = Toplevel(top)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   

def authentication_gui():
    #creating label and text box.
    l1 = Label(top, text="User Name")
    l1.pack(side=LEFT)
    l1.place(x=10, y=10)
    l2 = Entry(top, bd = 5)
    l2.pack(side=RIGHT)
    l2.place(x=100, y=10)
    p1 = Label(top, text="Password")
    p1.pack(side=LEFT)
    p1.place(x=10,y=50)
    p2 = Entry(top, bd = 5)
    p2.pack(side=RIGHT)
    p2.place(x=100, y=50)


def frames():
    # using frames before addding wiget to window. 
    frame = Frame(top)
    frame.pack()
    bottomframe = Frame(top)
    bottomframe.pack( side = BOTTOM )
    redbutton = Button(frame, text="Red", fg="red", command=donothing)
    redbutton.pack( side = LEFT)
    greenbutton = Button(frame, text="Brown", fg="brown", command=donothing)
    greenbutton.pack( side = LEFT )
    bluebutton = Button(frame, text = "Blue", fg = "blue",command=donothing)
    bluebutton.pack( side = LEFT )
    blackbutton = Button(bottomframe, text="Black", fg="black", command=donothing)
    blackbutton.pack( side = BOTTOM)


def menu_bar():
    # menu bar code start.
    menubar = Menu(top)
    # creating a file menu start.
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label = "Close", command = donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=top.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # creating file menu stop.
    top.config(menu=menubar)
    # menu bar code stop.


def creating_list():
    listlist = Listbox(top)
    listlist.insert(1, "puthon")
    listlist.pack()


def creating_button():
    b = Button(top, text = "T&C", command = donothing)
    b.place(x=10, y=70)
    b = Button(top, text = "LOGIN", command = donothing)
    b.place(x=240, y=70)

    
##########################################################################################################
# WIDGETS CODE
##########################################################################################################


top.mainloop()


##########################################################################################################
# END OF PROGRAM
##########################################################################################################