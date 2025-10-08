from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE


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

multiPack()