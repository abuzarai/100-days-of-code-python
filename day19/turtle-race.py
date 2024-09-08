from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'green', 'blue', 'brown', 'purple', 'yellow']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# Create a turtle to display messages
message_turtle = Turtle(visible=False)
message_turtle.penup()
message_turtle.goto(0, 0) # Position where the message will be displayed

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                message_turtle.write("You've won! The {} turtle is the winner!".format(winning_color), align="center", font=("Arial", 16, "normal"))
            else:
                message_turtle.write("You've lost! The {} turtle is the winner!".format(winning_color), align="center", font=("Arial", 16, "normal"))
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
