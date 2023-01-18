from tkinter import *
import time
import os

# Initiate Window
root=Tk()
root.title("Timer thing")
# root.configure(bg="#EBDBB2")

#Set up the main variable (counter) label
var = StringVar()
var.set("Hello World")
a = Label(root, textvariable=var, font=("Arial",100))
a.place(relx=0.5, rely=0.5, anchor="center")

# Handle the events of keypresses as Interrupts
def continueKey(event):
    root.destroy()
    os.system("python3 ./balagui.py")

def key_pressed(event):
    var.set("Done in: " + f'{counter:.2f}') 
    if counter==15.00:
        var.set("You win")
        root.bind("<Key>", continueKey)
        root.update()
    else:
        var.set("You Loose")
        b = Label(root, text="You stopped at " +f'{counter:.2f}' + " seconds", font=("Arial",60))
        b.place(relx=0.5, rely=0.6, anchor="center")
        c = Label(root, text="Press the button to try again", font=("Arial",50))
        c.place(relx=0.5, rely=0.8, anchor="center")
        # def continueKey(event):
        #     root.destroy()
        #     os.system("python2 ./balagui.py")
        root.bind("<Key>",continueKey)
    root.mainloop()

#Main Counting Loop
counter=0
delayTime=0.01

try:
    while counter<20:
        time.sleep(delayTime)
        var.set(f'{counter:.2f}')
        print(counter)
        counter += delayTime
        root.bind("<Key>",key_pressed)
        root.update()
except KeyboardInterrupt:
        # var.set("Done in: " + f'{counter:.2f}') 
        # if counter==15.00:
        #     var.set("You win")
        #     root.bind("<Key>", continueKey)
        #     root.update()
        # else:
        #     var.set("You Loose")
        #     b = Label(root, text="Time is " +f'{counter:.2f}', font=("Arial",60))
        #     b.place(relx=0.5, rely=0.7, anchor="center")
        root.destroy()
except:
    root.destroy()