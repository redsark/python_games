import turtle
import os
# import winwound
# winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

wn = turtle.Screen()
wn.title("Pong by kidong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddel B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

PADDLE_MOVE = 30

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += PADDLE_MOVE
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= PADDLE_MOVE
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += PADDLE_MOVE
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= PADDLE_MOVE
    paddle_b.sety(y)

def updateScore():
    pen.clear()
    pen.write("A 플레이어 : {}, B 플레이어: {}".format( score_a, score_b), align="center", font=("Courier", 24, "normal")) 

def initRound():
    paddle_a.color("white")
    paddle_b.color("white");
    ball.color("white")
    ball.shape("circle")

def specialAttack(paddle):
    ball.dx *= -2
    ball.shape("turtle")
    paddle.color("red")

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

updateScore()

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -2
        score_a += 1
        updateScore()
        initRound()
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 2
        score_b += 1
        updateScore()
        initRound()
        
    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        if ball.ycor() <= paddle_b.ycor() + 10 and ball.ycor() >= paddle_b.ycor() - 10:
            specialAttack( paddle_b)
        else:
            ball.dx *= -1
        os.system("afplay bounce.wav&") # afplay only mac
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        if ball.ycor() <= paddle_a.ycor() + 10 and ball.ycor() >= paddle_a.ycor() - 10:
            specialAttack( paddle_a)
        else:
            ball.dx *= -1
        os.system("afplay bounce.wav&") # linux aplay