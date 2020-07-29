import turtle

win = turtle.Screen()
win.title("Pong by abhinav")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

score_1=0
score_2=0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_len=1, stretch_wid=5)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_len=1, stretch_wid=5)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0,270)
pen.write("Player 1 : 0  player 2 : 0", align="center",font=("Arial",20,"normal"))

winner=turtle.Turtle()
winner.speed(0)
winner.penup()
winner.hideturtle()
winner.goto(0,50)

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        score_1+=1
        pen.clear()
        pen.write("Player 1 : {}  player 2 : {}".format(score_1,score_2), align="center",font=("Arial",20,"normal"))
    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        score_2+=1
        pen.clear()
        pen.write("Player 1 : {}  player 2 : {}".format(score_1, score_2), align="center",font=("Arial",20,"normal"))
    if (paddle_a.xcor() + 50) > 300:
        paddle_a.setx(300)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() > paddle_b.ycor() - 40 and ball.ycor() < paddle_b.ycor() + 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() > paddle_a.ycor() - 40 and ball.ycor() < paddle_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1
    if score_1 == 5:
        winner.color("red")
        winner.write("Player 1 wins!",align="center",font=("Arial",20,"normal"))
        ball.dx*=0
        ball.dy *= 0
    if score_2 == 5:
        winner.color("blue")
        winner.write("Player 2 wins!",align="center",font=("Arial",20,"normal"))
        ball.dx *= 0
        ball.dy *= 0