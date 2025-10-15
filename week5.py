from tkinter import Tk, Label, PhotoImage, Button, Entry, Text, Frame
from tkinter import BOTTOM, LEFT, RIGHT, RIDGE, RAISED, END, BOTH
from time import strftime, localtime
from tkinter.messagebox import showinfo
def clicked():
    time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    showinfo(message = time)

def clickIt_noClass():
    root = Tk()
    button = Button(root, text='Click it', command=clicked)
    button.pack()
    root.mainloop()


#sub optimal
class ClickIt(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        button = Button(self, text='Click it', command=self.clicked)
        button.pack()

    def clicked(self):
        time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
        showinfo(message=time)

# root = Tk()
# c = ClickIt(root)
# c.pack()
# root.mainloop()

class ClickBetter:
    def __init__(self):
        self.root = Tk()
        self.setup_widgets()

    def setup_widgets(self):
        self.button = Button(self.root, text='Click it', command=self.clicked)
        self.button.pack()

    def clicked(self):
        time = strftime('Day:  %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
        showinfo(message=time)

    def run(self):
        self.root.mainloop()

# c = ClickBetter()
# c.run()


class MultiPack:
    def __init__(self):
        self.root = Tk()
        self.on_screen_widgets = []
        self.setup_widgets()
        pass

    def setup_widgets(self):
        textLabel = Label(master=self.root, 
                    font=('Helvetica', 16, 'bold italic'),           
                    foreground='white',   
                    background='black', 
                    pady=10,  
                    text='It\'s the most wonderful time of the year!')
        
        halloween01 = PhotoImage(file='images/halloween01.png')
        halloween02 = PhotoImage(file='images/halloween02.png')

        halloween01Label = Label(master=self.root,
                   borderwidth=15,  
                   relief=RIDGE,   
                   image=halloween01)
    
        halloween02Label = Label(master=self.root, image=halloween02)

        btn = Button(master=self.root, text="Add Widget", command=self.add_widget)
        del_btn = Button(master=self.root, text="Delete Widget", command=self.remove_widget)
        

        textLabel.pack(side=BOTTOM)   
        halloween01Label.pack(side=LEFT)
        halloween02Label.pack(side=RIGHT)
        btn.pack()
        del_btn.pack()

    def remove_widget(self):
        widget_to_remove = self.on_screen_widgets.pop()
        widget_to_remove.destroy()

    def add_widget(self):
        textLabel = Label(master=self.root, 
                    font=('Helvetica', 16, 'bold italic'),           
                    foreground='white',   
                    background='black', 
                    pady=10,  
                    text='No thats Christmas silly')
        
        textLabel.pack(side=BOTTOM)  
        self.on_screen_widgets.append(textLabel)
         
        

    def run(self):
        self.root.mainloop()

m = MultiPack()
m.run()