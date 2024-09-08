from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.ymove *= -1
        self.ball_speed * 0.9

    def bounce_x(self):
        self.xmove *= -1
        self.ball_speed * 0.9

    def reset_positon(self):
        self.goto(x=0, y=0)
        self.ball_speed = 0.1
        self.bounce_x()
