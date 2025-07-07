from turtle import Screen
from move_keys import move_forward, move_backwards, move_clockwise, move_counter_clockwise, clear_drawing

screen = Screen()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(clear_drawing, "c")

screen.exitonclick()