import time, random
from init import *  

global score
score = 0
segments = []

# Snake move
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

# keyboard handling
def go_up():
	head.direction = "up"
def go_down():
	head.direction = "down"
def go_left():
	head.direction = "left"
def go_right():
	head.direction = "right"

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# check for collision with borders
def check_collision_borders():
	if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"				
	
		for i in segments:
			i.getturtle().reset()

		segments.clear()

		resetScore()
def resetScore():
    score = 0


# Main loop
while True:
    #updates Screen - render
	wn.update() 
	# conditions
	check_collision_borders()

	# check for collision with food
	if head.distance(food) < 20:
		x = random.randint(-290, 290)   
		y = random.randint(-290, 290)
		food.goto(x, y)

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color('grey')
		new_segment.penup()
		segments.append(new_segment)
		score += 10
    # executes segement movement (action)
	for index in range(len(segments)-1, -1,-1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
    # changes title, moves the head of the snake
	wn.title("Snake: " + str(score))
	move()
	time.sleep(delay)

wn.mainloop()