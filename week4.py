from tkinter import Tk, Label, PhotoImage, Button, Entry, Text
from tkinter import BOTTOM, LEFT, RIGHT, RIDGE, RAISED, END, BOTH
from time import strftime, localtime, strptime
from tkinter.messagebox import showinfo


def helloWorld(msg = "Hello GUI World"):
    root = Tk()
    helloWorld = Label(master=root,text=msg, height=480,width=640)
    helloWorld.pack()
    root.mainloop()

def helloImage():
    root = Tk()
    pic = PhotoImage(file="images\halloween01.png")
    halloweenLabel = Label(master=root, image=pic, width=640,height=480)
    halloweenLabel.pack()
    root.mainloop()

def multiPack():
    root = Tk()
    textLabel = Label(master=root, 
                    font=('Helvetica', 16, 'bold italic'),           
                    foreground='white',   
                    background='black', 
                    pady=10,  
                    text='It\'s the most wonderful time of the year!')
    textLabel.pack(side=BOTTOM)    

    halloween01 = PhotoImage(file='images/halloween01.png')
    halloween02 = PhotoImage(file='images/halloween02.png')

    halloween01Label = Label(root,
                   borderwidth=15,  
                   relief=RIDGE,   
                   image=halloween01)
    
    halloween02Label = Label(root, image=halloween02)

    halloween01Label.pack(side=LEFT)
    halloween02Label.pack(side=RIGHT)

    root.mainloop()

def non_functioning_calculator():
    root = Tk()
    labels = [['1', '2', '3'],     
            ['4', '5', '6'],     
            ['7', '8', '9'],
            ['*', '0', '#']]
    for r in range(4):
        for c in range(3):
            # create label for row r and column c
            label = Label(root,
                        relief=RAISED,      
                        padx=25,            
                        text=labels[r][c])
            # place label in row r and column c
            label.grid(row=r, column=c)
    root.mainloop()

def clicked():
    'prints day and time info'
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    #print(time)
    showinfo(message=time)


def buttonIntro():
    root = Tk()
    button = Button(root,
                    text='Click it',   
                    command=clicked)
    button.pack()
    root.mainloop()

def add(num):
    try:
        number1 = eval(num)
    except:
        showinfo(message="You can only add numbers!")

def functioning_calculator():
    root = Tk()
    labels = [['1', '2', '3'],     
            ['4', '5', '6'],     
            ['7', '8', '9'],
            ['*', '0', '#']]
    for r in range(4):
        for c in range(3):
            # create label for row r and column c
            button = Button(root,
                        relief=RAISED,      
                        padx=25,            
                        text=labels[r][c],
                        command=lambda: add(labels[r][c]))
            # place label in row r and column c
            button.grid(row=r, column=c)
    root.mainloop()

functioning_calculator()

def compute():
    date = dateEnt.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message = '{} was a {}'.format(date, weekday))
    dateEnt.delete(0, END)

def date_compute():
    root = Tk()
    label = Label(root, text='Enter date')
    label.grid(row=0, column=0)
    global dateEnt   # dateEnt is a global variable
    dateEnt = Entry(root)
    dateEnt.grid(row=0, column=1)
    button = Button(root, text='Enter', command=compute) 
    button.grid(row=1, column=0, columnspan=2)
    root.mainloop()

def record(event):
    '''event handling function for key press events;
       input event is of type tkinter.Event'''
    print('char = {}'.format(event.keysym)) # print key symbol



def keyboard_events():
    root = Tk()
    text = Text(root,
                width=20,  # set width to 20 characters
                height=5)  # set height to 5 rows of characters
    # Bind a key press event with the event handling function record()
    text.bind('<KeyPress>', record)
    # widget expands if the master does
    text.pack(expand=True, fill=BOTH)
    root.mainloop()

#keyboard_events()