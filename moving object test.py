from tkinter import *
import time

class Enemy:

    def __init__(self , canvas , x1 , y1 , x2 , y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas=canvas
        self.enemy = canvas.create_oval(self.x1 , self.y1 , self.x2 , self.y2 , fill="dark red")

    def move_enemy(self):
        deltax = 0
        deltay = 0
        self.canvas.move(self.enemy , deltax , deltay)
        self.canvas.after(30 , self.move_enemy)

class User:

    def __init__(self , canvas , x1 , y1 , x2 , y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas=canvas
        self.user = canvas.create_oval(self.x1 , self.y1 , self.x2 , self.y2 , fill="blue")

def move_left(event):
    deltax = -1
    deltay = 0
    user1.canvas.move(user1.user , deltax , deltay)

def move_right(event):
    deltax = 1
    deltay = 0
    user1.canvas.move(user1.user , deltax , deltay)

def move_up(event):
    deltay = -1
    deltax = 0
    user1.canvas.move(user1.user , deltax , deltay)

def move_down(event):
    deltay = 1
    deltax = 0
    user1.canvas.move(user1.user , deltax , deltay)
        
    

main = Tk()
main.title("Enemys")
main.resizable(False,False)
main.geometry("500x500")
canvas=Canvas(main,width=500,height=500)
canvas.place(x=0,y=0)

main.bind("<Key-Left>",move_left)
main.bind("<Key-Up>",move_up)
main.bind("<Key-Down>",move_down)
main.bind("<Key-Right>",move_right)
    
enemy1 = Enemy(canvas , 30 , 30 , 10 ,10)
user1 = User(canvas , 30 , 30 , 10, 10)

enemy1.move_enemy()
main.mainloop()
