import turtle
from turtle import Turtle

paddle = "img\paddle.gif"
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        turtle.register_shape(paddle)
        self.shape(paddle)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("White")
        self.penup()
        self.goto(position)


    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)