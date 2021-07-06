from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_anticlcokwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key = 'w', fun = move_forward)
screen.onkey(key = 's', fun = move_backward)
screen.onkey(key = 'd', fun = move_clockwise)
screen.onkey(key = 'a', fun = move_anticlcokwise)
screen.onkey(key = 'c', fun = clear)
screen.exitonclick()