# Xiaoxia Ning
# 4/5/2024
# P4LAB1b: Initials
# This is a program that displays your first and last initials


import turtle
wn = turtle.Screen()# Set up the window and its attributes
wn.title("first and last initials")

pen = turtle.Turtle() # Create a turtle named "pen"
pen.color("blue")
pen.pensize(3)
pen.speed(1)
# Draw the letter "N"
pen.penup()
pen.goto(-200, 0)
pen.pendown()
pen.left(90)
pen.forward(100)
pen.right(150)
pen.forward(115)
pen.left(150)
pen.forward(100)
  
# Move to draw the letter "X"
pen.penup()
pen.goto(100, 0)
pen.pendown()
pen.left(45)
pen.forward(100)
pen.backward(50)
pen.left(90)
pen.forward(50)
pen.backward(100)

wn.mainloop()

