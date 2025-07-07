from turtle import Turtle

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    tim.reset()