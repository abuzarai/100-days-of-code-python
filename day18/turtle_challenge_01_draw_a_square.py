from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')

# TODO 1: Draw a square
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

screen = Screen()
screen.exitonclick()