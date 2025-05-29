from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.listen()
screen.setup(500, 400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color from the list [red, orange, yellow, green, blue, purple]: ")

# turtles

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)

turtles = []

y_positions = [-100, -60, -20, 20, 60, 100]

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, y_positions[i])
    turtles.append(t)


# movement
if user_bet:
    is_race_on = True

while is_race_on is True:
    for t in turtles:

        if t.xcor() > 240:
            is_race_on = False
            winning_color = t.pencolor()

            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)


screen.exitonclick()