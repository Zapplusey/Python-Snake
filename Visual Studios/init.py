import turtle

delay = 0.1

# set up rhe screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # turns of the screen update

# Snake head
class snake_head():
    def __init__(self, *direction):
        super.__init__()
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(0.75,0.75)
food.color("red")
food.penup()
food.goto(0, 100)