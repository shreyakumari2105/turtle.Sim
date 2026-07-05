#!/usr/bin/env python3
import turtle
import time

# Screen setup karna
screen = turtle.Screen()
screen.title("Two Turtles Drawing Perfect Squares")
screen.bgcolor("white")

# Pehla Turtle (Red Turtle) banana
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.speed(2)  # Speed control karne ke liye

# Dusra Turtle (Blue Turtle) banana
turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("blue")
turtle2.speed(2)

# ---- STEP 1: Dono ko unki starting position par lana bina line banaye ----
turtle1.penup()
turtle2.penup()

# Turtle 1 ko thoda left me set karna (x = -100, y = 0)
turtle1.goto(-100, 0)

# Turtle 2 ko horizontally thoda right me rakhna (x = 100, y = 0)
turtle2.goto(100, 0)

# Drawing start karne ke liye pen down karna
turtle1.pendown()
turtle2.pendown()

# ---- STEP 2: Dono se ek sath Perfect Square banwana ----
side_length = 100

for _ in range(4):
    # Dono turtles ek sath aage badhenge
    turtle1.forward(side_length)
    turtle2.forward(side_length)
    
    time.sleep(0.2) # Chota sa pause realistic dikhne ke liye
    
    # Dono turtles ek sath 90 degrees left turn lenge
    turtle1.left(90)
    turtle2.left(90)
    
    time.sleep(0.2)

# Screen ko open rakhne ke liye jab tak aap click na karein
screen.exitonclick()