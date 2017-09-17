import turtle
Pen = turtle.Pen()
v_das = turtle.Screen()
v_das.size = (600,800)
God = turtle.Turtle()
Tres = turtle.Pen()
Tres.pensize(10)
Tres.speed(0)
God.shape('turtle')

def coinBlue():
    Tres.pencolor("blue")
    Tres.up()
    Tres.left(135)
    Tres.forward(400)
    Tres.down()
    Tres.circle(10)
def coinRed():
    Tres.pencolor("red")
    Tres.up()
    Tres.right(170)
    Tres.forward(643)
    Tres.down()
    Tres.circle(10)
def coinGreen():
    Tres.pencolor("green")
    Tres.up()
    Tres.right(120)
    Tres.forward(300)
    Tres.down()
    Tres.circle(10)
def coinPurple():
    Tres.pencolor("purple")
    Tres.up()
    Tres.right(150)
    Tres.forward(400)
    Tres.down()
    Tres.circle(10)
    Tres.up()
Tres.hideturtle()


Pen.up()
God.up()

def forward():
    God.forward(60)
def left():
    God.left(60)
    God.forward(60)
def right():
    God.right(60)
    God.forward(60)

def follow_runner():
    Pen.setheading(Pen.towards(God))
    Pen.forward(4)
    v_das.ontimer(follow_runner, 10)

v_das.onkey(forward,"Up")
v_das.onkey(left,"Left")
v_das.onkey(right,"Right")

coinBlue()
coinRed()
coinGreen()
coinPurple()

follow_runner()
v_das.listen()

v_das.exitonclick()
