# Xiaoxia Ning
# 4/5/2024
# P4LAB1a: Shapes
# This is a program that draws both a square and a triangle


import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.title("Triangle & Square")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)
tess.speed(1)


for i in [0,1,2]:
  tess.forward(80)             # Make tess draw  triangle
  tess.left(120)
  
tess.penup()                   # Turn tess around
tess.goto(-200,0)
tess.pendown()
tess.color("green")

i=1
while i <=4:           # Make tess draw a square
  tess.forward(50)
  tess.left(90)
  i+=1


wn.mainloop()

