from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100


class Paddle(Turtle):

    def __init__(self, position_cor):
        super().__init__()
        self.position_cor = position_cor
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.position_cor)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
