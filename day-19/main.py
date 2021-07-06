from turtle import Turtle, Screen, title, turtles
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the rcae? enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x_cord = 230
y_cord = -70
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-x_cord, y= y_cord)
    y_cord +=30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        