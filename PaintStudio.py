import turtle

# defining window looks
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)

# The square
loc = turtle.Turtle()
loc.speed(0)
loc.shape("square")
loc.color("white")
loc.penup()
loc.goto(0, 0)

# Filling pen
fill = turtle.Turtle()
fill.speed(0)
fill.color("white")
fill.hideturtle()

# Pen writing hash
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()

# Hash x up
pen.penup()
pen.goto(-625, 7.5)
pen.pendown()
pen.goto(625, 7.5)
pen.penup()
pen.goto(-625, 22.5)
pen.pendown()
pen.goto(625, 22.5)
pen.penup()
pen.goto(-625, 37.5)
pen.pendown()
pen.goto(625, 37.5)
pen.penup()
pen.goto(-625, 52.5)
pen.pendown()
pen.goto(625, 52.5)
pen.penup()
pen.goto(-625, 67.5)
pen.pendown()
pen.goto(625, 67.5)
pen.penup()
pen.goto(-625, 82.5)
pen.pendown()
pen.goto(625, 82.5)
pen.penup()
pen.goto(-625, 97.5)
pen.pendown()
pen.goto(625, 97.5)
pen.penup()
pen.goto(-625, 112.5)
pen.pendown()
pen.goto(625, 112.5)
pen.penup()
pen.goto(-625, 127.5)
pen.pendown()
pen.goto(625, 127.5)
pen.penup()
pen.goto(-625, 142.5)
pen.pendown()
pen.goto(625, 142.5)
pen.penup()
pen.goto(-625, 157.5)
pen.pendown()
pen.goto(625, 157.5)
pen.penup()
pen.goto(-625, 172.5)
pen.pendown()
pen.goto(625, 172.5)
pen.penup()
pen.goto(-625, 187.5)
pen.pendown()
pen.goto(625, 187.5)
pen.penup()
pen.goto(-625, 202.5)
pen.pendown()
pen.goto(625, 202.5)
pen.penup()
pen.goto(-625, 217.5)
pen.pendown()
pen.goto(625, 217.5)
pen.penup()
pen.goto(-625, 232.5)
pen.pendown()
pen.goto(625, 232.5)
pen.penup()
pen.goto(-625, 247.5)
pen.pendown()
pen.goto(625, 247.5)
pen.penup()
pen.goto(-625, 262.5)
pen.pendown()
pen.goto(625, 262.5)
pen.penup()
pen.goto(-625, 277.5)
pen.pendown()
pen.goto(625, 277.5)
pen.penup()



# Hash x down
pen.penup()
pen.goto(-625, -7.5)
pen.pendown()
pen.goto(625, -7.5)
pen.penup()
pen.goto(-625, -22.5)
pen.pendown()
pen.goto(625, -22.5)
pen.penup()
pen.goto(-625, -37.5)
pen.pendown()
pen.goto(625, -37.5)
pen.penup()
pen.goto(-625, -52.5)
pen.pendown()
pen.goto(625, -52.5)
pen.penup()
pen.goto(-625, -67.5)
pen.pendown()
pen.goto(625, -67.5)
pen.penup()
pen.goto(-625, -82.5)
pen.pendown()
pen.goto(625, -82.5)
pen.penup()
pen.goto(-625, -97.5)
pen.pendown()
pen.goto(625, -97.5)
pen.penup()
pen.goto(-625, -112.5)
pen.pendown()
pen.goto(625, -112.5)
pen.penup()
pen.goto(-625, -127.5)
pen.pendown()
pen.goto(625, -127.5)
pen.penup()
pen.goto(-625, -142.5)
pen.pendown()
pen.goto(625, -142.5)
pen.penup()
pen.goto(-625, -157.5)
pen.pendown()
pen.goto(625, -157.5)
pen.penup()
pen.goto(-625, -172.5)
pen.pendown()
pen.goto(625, -172.5)
pen.penup()
pen.goto(-625, -187.5)
pen.pendown()
pen.goto(625, -187.5)
pen.penup()
pen.goto(-625, -202.5)
pen.pendown()
pen.goto(625, -202.5)
pen.penup()
pen.goto(-625, -217.5)
pen.pendown()
pen.goto(625, -217.5)
pen.penup()
pen.goto(-625, -232.5)
pen.pendown()
pen.goto(625, -232.5)
pen.penup()
pen.goto(-625, -247.5)
pen.pendown()
pen.goto(625, -247.5)
pen.penup()
pen.goto(-625, -262.5)
pen.pendown()
pen.goto(625, -262.5)
pen.penup()
pen.goto(-625, -277.5)
pen.pendown()
pen.goto(625, -277.5)
pen.penup()

# Hash y left
pen.penup()
pen.goto(-7.5, 275)
pen.pendown()
pen.goto(-7.5, -275)
pen.penup()
pen.goto(-22.5, 275)
pen.pendown()
pen.goto(-22.5, -275)
pen.penup()
pen.goto(-37.5, 275)
pen.pendown()
pen.goto(-37.5, -275)
pen.penup()
pen.goto(-52.5, 275)
pen.pendown()
pen.goto(-52.5, -275)
pen.penup()
pen.goto(-67.5, 275)
pen.pendown()
pen.goto(-67.5, -275)
pen.penup()
pen.goto(-82.5, 275)
pen.pendown()
pen.goto(-82.5, -275)
pen.penup()
pen.goto(-97.5, 275)
pen.pendown()
pen.goto(-97.5, -275)
pen.penup()
pen.goto(-112.5, 275)
pen.pendown()
pen.goto(-112.5, -275)
pen.penup()
pen.goto(-425, 275)
pen.pendown()
pen.goto(-425, -275)
pen.penup()
pen.goto(-475, 275)
pen.pendown()
pen.goto(-475, -275)
pen.penup()
pen.goto(-525, 275)
pen.pendown()
pen.goto(-525, -275)
pen.penup()
pen.goto(-575, 275)
pen.pendown()
pen.goto(-575, -275)
pen.penup()
pen.goto(-625, 275)
pen.pendown()
pen.goto(-625, -275)
pen.penup()

# Hash y right
pen.penup()
pen.goto(25, 275)
pen.pendown()
pen.goto(25, -275)
pen.penup()
pen.goto(75, 275)
pen.pendown()
pen.goto(75, -275)
pen.penup()
pen.goto(125, 275)
pen.pendown()
pen.goto(125, -275)
pen.penup()
pen.goto(175, 275)
pen.pendown()
pen.goto(175, -275)
pen.penup()
pen.goto(225, 275)
pen.pendown()
pen.goto(225, -275)
pen.penup()
pen.goto(275, 275)
pen.pendown()
pen.goto(275, -275)
pen.penup()
pen.goto(325, 275)
pen.pendown()
pen.goto(325, -275)
pen.penup()
pen.goto(375, 275)
pen.pendown()
pen.goto(375, -275)
pen.penup()
pen.goto(425, 275)
pen.pendown()
pen.goto(425, -275)
pen.penup()
pen.goto(475, 275)
pen.pendown()
pen.goto(475, -275)
pen.penup()
pen.goto(525, 275)
pen.pendown()
pen.goto(525, -275)
pen.penup()
pen.goto(575, 275)
pen.pendown()
pen.goto(575, -275)
pen.penup()
pen.goto(625, 275)
pen.pendown()
pen.goto(625, -275)
pen.penup()



# defining and zeroing variables
y_axis = 0
x_axis = 0
coins = 0

# defining movement and number of coins
def go_north():
    y = loc.ycor()
    y += 15
    loc.sety(y)

def go_south():
    y = loc.ycor()
    y -= 15
    loc.sety(y)

def go_east():
    x = loc.xcor()
    x += 15
    loc.setx(x)

def go_west():
    x = loc.xcor()
    x -= 15
    loc.setx(x)

wn.listen()
wn.onkeypress(go_north, "w")
wn.onkeypress(go_south, "s")
wn.onkeypress(go_east, "d")
wn.onkeypress(go_west, "a")
# wn.onkeypress(human, "1")


def draw():
    def square():
        fill.goto(loc.xcor(), loc.ycor())
        fill.penup()
        fill.forward(7.5)
        fill.right(90)
        fill.pendown()
        fill.forward(7.5)
        fill.right(90)
        fill.forward(15)
        fill.right(90)
        fill.forward(15)
        fill.right(90)
        fill.forward(15)
        fill.right(90)
        fill.forward(7.5)
        fill.penup()
        fill.right(90)
        fill.forward(7.5)
        fill.right(180)
        fill.penup()
       
    fill.fillcolor("red")
    fill.begin_fill()
    square()
    fill.end_fill()


# game function
while True:
    wn.update()
    draw()
