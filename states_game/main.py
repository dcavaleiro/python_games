import turtle
from check_answer import Answer

screen = turtle.Screen()
check_answer = Answer()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f'Guess the State {check_answer.score}/50', prompt="What's a another state's name?")

    check_answer.check_answer(answer_state)

    if check_answer.score == 50:
        game_is_on = False
