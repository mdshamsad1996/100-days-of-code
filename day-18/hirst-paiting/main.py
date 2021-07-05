
# Extract rgb list color from img and paste in form list of  tuple(rgb)
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('img.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen
import random
import turtle


turtle.colormode(255)
color_list = [(237, 242, 248), (249, 240, 244), (192, 140, 150), (25, 36, 55), (145, 178, 162), (137, 68, 76), (47, 36, 41), (55, 108, 89), (228, 167, 173), (189, 99, 107)]

tinny = Turtle()
tinny.speed("fastest")
tinny.penup()
tinny.hideturtle()
screen = Screen()

tinny.setheading(300)
tinny.forward(250)
tinny.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tinny.dot(20, random.choice(color_list))
    tinny.forward(50)
    if dot_count % 10 == 0:
        tinny.setheading(90)
        tinny.forward(58)
        tinny.setheading(180)
        tinny.forward(500)
        tinny.setheading(0)
screen.exitonclick()
        



