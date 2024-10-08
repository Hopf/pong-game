import turtle as t
import os

playerAscore=0
playerBscore=0
  
#create a window and declare a variable called window and call the screen()
window=t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)
  
#Creating the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)
  
#Creating the right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)
  
#Code for creating the ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.1
ballydirection=0.1
# Remove or use ball_dx as intended
  
#Code for creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))
  
#code for moving the leftpaddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)
  
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)
  
#code for moving the rightpaddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)
  
def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)
  
#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')
  
while True:
    window.update()
  
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
  
    #border set up
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1
          
    if ball.xcor() > 390:
        ball.goto(0,0)

        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")
  
  
  
    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)

        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")
  
     # Handling the collisions with paddles.
  
    def handle_paddle_collision(ball, paddle, is_right_paddle):
        paddle_x = 340 if is_right_paddle else -340
        if ((ball.xcor() > paddle_x and is_right_paddle) or (ball.xcor() < paddle_x and not is_right_paddle)) and \
           (abs(ball.xcor() - paddle_x) < 10) and \
           (ball.ycor() < paddle.ycor() + 40 and ball.ycor() > paddle.ycor() - 40):
            ball.setx(paddle_x)
            global ballxdirection
            ballxdirection *= -1
            os.system("afplay paddle.wav&")

    handle_paddle_collision(ball, rightpaddle, True)
    handle_paddle_collision(ball, leftpaddle, False)
