"""
title: tkinter_lab
author: raga mandali
date: 06/22/2021
"""

from tkinter import *

window = Tk()
window.title("class example")
canvas = Canvas(window, width=400, height=300)
canvas.pack()

window.mainloop(30)


canvas.create_oval(50, 50, 120, 120)  #head

canvas.create_line(70, 90, 70, 60) #eye1
canvas.create_line(100, 90, 100, 60) #eye2

canvas.create_oval(80, 100, 90, 110, outline = "red")  #mouth

canvas.create_line(90, 120, 90, 230) #body

canvas.create_line(90, 230, 120, 290) #leg1
canvas.create_line(90, 230, 70, 290)  #leg2

canvas.create_line(90, 130, 120, 190) #arm1
canvas.create_line(120, 190, 130, 150) #arm1segment
canvas.create_line(90, 130, 70, 225)  #arm2

canvas.create_oval(128, 150, 138, 140) #hand1
canvas.create_oval(70, 225, 60, 235) #hand1

#Hi!
canvas.create_line(220, 100, 220, 50) 
canvas.create_line(220, 75, 250, 75) 
canvas.create_line(250, 100, 250, 50)
canvas.create_line(280, 100, 280, 50)
canvas.create_line(270, 99, 290, 99)
canvas.create_line(270, 50, 290, 50)
canvas.create_line(310, 90, 310, 50) 
canvas.create_oval(307, 95, 313, 100)  