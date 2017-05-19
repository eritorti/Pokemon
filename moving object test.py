from tkinter import *
import time

main = Tk()


canv =  Canvas(main, width=500, height=500, bg="white")
canv.pack(expand=YES)

top = canv.create_line(0, 0, 500, 0, fill="black")
ball = canv.create_oval(230, 230, 250, 250, fill="dark red", tags="ball")

while(canv.find_overlapping(canv.coords(ball)[0],canv.coords(ball)[1],canv.coords(ball)[2],canv.coords(ball)[3]) != 1):
    time.sleep(0.5)
    if(canv.find_overlapping(canv.coords(ball)[0],canv.coords(ball)[1],canv.coords(ball)[2],canv.coords(ball)[3]) == 1):
        print("Herzlichen Glückwunsch Eliseo du bist Klasse!!!")
    deltax = 0
    deltay = -1
    canv.move(ball, deltax, deltay)
    #canv.after(20, move_ball)
    canv.update()
    
def show_coords(event):    
    print(canv.find_overlapping(canv.coords(ball)[0],canv.coords(ball)[1],canv.coords(ball)[2],canv.coords(ball)[3])[0],canv.find_overlapping(canv.coords(top)[0],canv.coords(top)[1],canv.coords(top)[2],canv.coords(top)[3])[0])

move_ball()

main.bind("<Key-d>", show_coords)

main.mainloop()
