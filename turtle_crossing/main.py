import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle crossing game')
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 275:
        player.reset_position()
        car_manager.level_up()
        scoreboard.update_scoreboard()

    for car in car_manager.all_cars:
        if player.distance(car) < 23:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()