import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import winsound

#********************* Developed by Divyesh Dhole ********************************
screen = Screen()


##Screen dimensions
screen.setup(width = 800, height=600)
screen.title("Pong game")



bg = "img/bg.gif"

loader = Turtle()


developer_name = "Divyesh Dhole"
def loading():
    load_bg = "img/banner.gif"
    screen.register_shape(load_bg)
    screen.bgpic(load_bg)
    loader.hideturtle()
    loader.penup()
    #animation Start
    x = -150
    y = 40
    loader.goto(x, y)
    for i in range(0,10):
        loader.write(arg="🟨",font=("Courier", 20, "bold"))
        x = x + 30
        loader.goto(x, y)
        time.sleep(0.2)
    loader.clear()
    #animation end

    time.sleep(0.2)
    #for display the developed by text
    developer = Turtle()
    developer.hideturtle()
    developer.penup()
    x = -60
    y = 60
    developer.goto(x, y)
    developer.write("Developed BY", font=("Courier", 10, "bold"))
    #End

    time.sleep(0.5)

    #To display developer name
    x = -150
    y = 20
    loader.goto(x, y)
    loader.write(developer_name, font=("Arial", 30, "bold"))
    time.sleep(0.3)
    #End

    #for starting animation
    x = -110
    y = -20
    loader.goto(x, y)
    loader.color("White")
    loader.write("Starting", font=("Courier", 20, "bold"))
    #End
    #for '.' animation
    x = 20
    loader.goto(x, y)
    for i in range(0,5):
        loader.write(".", font=("Courier", 20, "bold"))
        loader.goto(x, y)
        x = x + 20
        time.sleep(0.2)
    screen.clear()
    #End



loading()      #Loadind animation on


loader.goto(0,0)
loader.color("Yellow")


screen.register_shape(bg)
screen.bgpic(bg)


for i in range(1,4):
    loader.write(f"{i}", font=("Arial", 30, "bold"))
    time.sleep(0.5)
    loader.clear()

screen.tracer(0)

#Create the ball
ball = Ball()

##scoreboard will show the score of left and right paddle
scoreboard = Scoreboard()



#Create the paddle object
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

##Listen the keys
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")





game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()


    #Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        winsound.Beep(1100, 10)
        ball.bounce_x()


    #Detect when r_paddle missing
    if ball.xcor() > 380 :
        winsound.Beep(200, 1000)
        ball.reset_position()
        scoreboard.l_point()

    #Detect when l_paddle missing
    if ball.xcor() < -380 :
        winsound.Beep(200, 1000)
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
# The code is ready