from tkinter import *
import random
import time

main=Tk()
main.geometry("598x598")

x=300
y=300

def oben(event):
    global y
    y -=10
    char.place(y=y)
    if(y==0):
        y +=10

def unten(event):
    global y
    y +=10
    char.place(y=y)
    if(y==580):
        y -=10

def links(event):
    global x
    x -=10
    char.place(x=x)
    if(x==0):
        x += 10

def rechts(event):
    global x
    x +=10
    char.place(x=x)
    if(x==580):
        x-=10

def enemy(event):
    global feind
    feind.place(x=random.randint(20,550),y=random.randint(20,550),width=20,height=20)

def fds():
    feind.destroy()
    feind=Button(main,bg="red",text=" ",activebackground="dark red",command=fds)

char=Label(main,text="/n",bg="black")
char.place(x=x,y=y)

feind=Button(main,bg="red",text=" ",activebackground="dark red",command=fds)

main.bind("<Up>", oben)
main.bind("<Down>",unten)
main.bind("<Left>",links)
main.bind("<Right>",rechts)
main.bind("<Key-space>",enemy)

main.mainloop()
