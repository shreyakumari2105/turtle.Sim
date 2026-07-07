import turtle

screen = turtle.Screen()
screen.title("Do Turtle - Mouse Pointer Follow")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

leader = turtle.Turtle()
leader.shape("turtle")
leader.color("blue")
leader.penup()
leader.speed(0)

follower = turtle.Turtle()
follower.shape("turtle")
follower.color("red")
follower.penup()
follower.speed(0)
follower.setposition(-150, 0)

SAFE_DISTANCE = 50

def mouse_move(x, y):
    leader.setheading(leader.towards(x, y))
    leader.goto(x, y)

    distance = follower.distance(leader)
    if distance > SAFE_DISTANCE:
        follower.setheading(follower.towards(leader))
        follower.goto(
            follower.xcor() + (leader.xcor() - follower.xcor()) * 0.1,
            follower.ycor() + (leader.ycor() - follower.ycor()) * 0.1
        )

    screen.update()

canvas = screen.getcanvas()
canvas.bind('<Motion>', lambda event: mouse_move(
    event.x - screen.window_width() / 2,
    screen.window_height() / 2 - event.y
))

canvas.focus_force()
screen.listen()
screen.mainloop()