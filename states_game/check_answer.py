import pandas as pd
from turtle import Turtle


DATA = pd.read_csv('50_states.csv')

class Answer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.guessed_states = []

    def state_location(self, state_name, x, y):
        self.goto(x,y)
        self.write(state_name, align="center", font=("Arial", 8, "bold"))

    def scoreboard(self):
        self.score += 1

    def check_answer(self, user_answer):
        user_answer = user_answer.title()
        correct_answer = DATA['state'].to_list()
        if user_answer in correct_answer:
            row = DATA[DATA['state'] == user_answer]
            x = int(row.x)
            y = int(row.y)
            self.state_location(user_answer, x, y)
            self.scoreboard()
            self.guessed_states.append(user_answer)
        if user_answer == 'Exit':
            missing_states = [state for state in correct_answer if state not in self.guessed_states]
            report = pd.DataFrame(missing_states)
            report.to_csv('missing_states_to_guess.csv')
            exit()

        else:
            pass