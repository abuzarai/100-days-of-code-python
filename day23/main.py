import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    if player.ycor() > 310:
        scoreboard.player_point()
        player.starting_position()
        car_manager.increase_speed()

    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()