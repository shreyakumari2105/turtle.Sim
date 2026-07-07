import turtle

screen = turtle.Screen()
screen.title("Do Turtle - Ek Leader, Ek Follower")
screen.bgcolor("white")
screen.setup(width=800, height=600)

leader = turtle.Turtle()
leader.shape("turtle")
leader.color("blue")
leader.pendown()
leader.pensize(2)
leader.speed(0)

follower = turtle.Turtle()
follower.shape("turtle")
follower.color("red")
follower.pendown()
follower.pensize(2)
follower.speed(0)
follower.setposition(-100, 0)

STEP = 5
SAFE_DISTANCE = 50

def move_up():
    leader.setheading(90)
    leader.forward(STEP)
    follow_leader()

def move_down():
    leader.setheading(270)
    leader.forward(STEP)
    follow_leader()

def move_left():
    leader.setheading(180)
    leader.forward(STEP)
    follow_leader()

def move_right():
    leader.setheading(0)
    leader.forward(STEP)
    follow_leader()

def follow_leader():
    distance = follower.distance(leader)
    if distance > SAFE_DISTANCE:
        follower.setheading(follower.towards(leader))
        follower.forward(distance - SAFE_DISTANCE)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

# Window pe click karte hi focus mil jayega
def give_focus(x, y):
    root.focus_force()
    canvas.focus_set()

screen.onclick(give_focus)

# Har key press pe focus wapas set karo (extra safety)
root.bind("<Button-1>", lambda e: canvas.focus_set())

screen.listen()
canvas.focus_force()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.mainloop()