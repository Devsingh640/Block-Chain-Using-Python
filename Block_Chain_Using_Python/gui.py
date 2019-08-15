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
var = IntVar()

##########################################################################################################
# FUNCTIONS
##########################################################################################################


def donothing():
   filewin = Toplevel(top)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   

def authentication_gui():
    #creating label and text box inside a frame.
    frame = Frame(top)
    frame.pack()
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


def scroll_bar():
    scrollbar = Scrollbar(top)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(top, yscrollcommand = scrollbar.set )
    
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))
    
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )


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
    bluebutton.pack(side=LEFT)
    blackbutton = Button(bottomframe, text="Black", fg="black", command=donothing)
    blackbutton.pack(side=BOTTOM)


def body_title_display_function():                                                                                # created a function that creates a frame at the top of the window that displayes title.
    body_title_display_frame = Frame(top, width=800, height=80, bg="powder blue", relief=SUNKEN)                  # creating frame body_title_display_frame.
    body_title_display_frame.pack(side=TOP)                                                                       # packes the frame body_title_display_frame and aligned at top of master window.
    body_title_display_text = Label(body_title_display_frame, font="arial", text="COIN EXCHANGE SYSTEM")          # this will display the text in frame body_title_display_frame. 
    body_title_display_text.pack()                                                                                # packes the label body_title_display_text and aligned at top of master window.


def displat_all_transaction_function():                                                                           # created a function that creates a frame at the top of the window that displayes title.
    right_frame = Frame(top, width=400, height=600, bg="powder blue", relief=SUNKEN)                 # creating frame body_title_display_frame.
    right_frame.pack(side=RIGHT)                                                                     # packes the frame body_title_display_frame and aligned at top of master window.
    right_frame_heading_display_text = Label(right_frame, font="arial", text="COIN EXCHANGE SYSTEM")        # this will display the text in frame body_title_display_frame. 
    right_frame_heading_display_text.pack()                                                                              # packes the label body_title_display_text and aligned at top of master window.
    l1 = Label(right_frame, text="User Name")
    l1.pack(side=LEFT)
    l1.place(x=10, y=10)
    l2 = Entry(right_frame, bd = 5)
    l2.pack(side=RIGHT)
    l2.place(x=100, y=10)
    p1 = Label(right_frame, text="Password")
    p1.pack(side=LEFT)
    p1.place(x=10,y=50)
    p2 = Entry(right_frame, bd = 5)
    p2.pack(side=RIGHT)
    p2.place(x=100, y=50)

def display_all_options():                                                                                        # created a function that creates a frame at the top of the window that displayes title.
    body_title_display_frame = Frame(top, width=400, height=600, bg="powder blue", relief=SUNKEN)                 # creating frame body_title_display_frame.
    body_title_display_frame.pack(side=LEFT)                                                                      # packes the frame body_title_display_frame and aligned at top of master window.
    body_title_display_text = Label(body_title_display_frame, font="arial", text="COIN EXCHANGE SYSTEM")        # this will display the text in frame body_title_display_frame. 
    body_title_display_text.pack()                                                                              # packes the label body_title_display_text and aligned at top of master window.



def radio_button():
    R1 = Radiobutton(top, text="Option 1", variable=var, value=1, command=sel)
    R1.pack(anchor=W)
    R2 = Radiobutton(top, text="Option 2", variable=var, value=2, command=sel)
    R2.pack(anchor=W)
    R3 = Radiobutton(top, text="Option 3", variable=var, value=3, command=sel)
    R3.pack(anchor=W)
    label = Label(top)
    label.pack()


def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)


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

top.title("COIN EXCHANGE SYSTEM")  # this is window title.
top.geometry("800x600")    # this will det a default window size.

menu_bar()  # calling menu bar function to display a menu.
body_title_display_function()
displat_all_transaction_function()
display_all_options()
top.mainloop()


##########################################################################################################
# END OF PROGRAM
##########################################################################################################