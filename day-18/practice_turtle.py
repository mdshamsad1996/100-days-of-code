from turtle import Turtle, Screen, color
import random
import turtle

tinny = Turtle()

# tinny.shape('square')
# screen = Screen(tinny.exitonclick())

# for _ in range(10):
#     tinny.forward(6)
#     tinny.penup()
#     tinny.forward(5)
#     tinny.pendown()
#     # tinny.left(90)

colors = ["navy", "light steel blue", "cornflower blue", "spring green", "firebrick", "magenta"]
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tinny.forward(100)
#         tinny.right(angle)

# for shape_side_n in range(3, 11):
#     tinny.color(random.choice(colors))
#     draw_shape(shape_side_n)

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# directions = [0, 90, 180, 270, 360]
# tinny.pensize(15)
tinny.speed("fastest")
# for _ in range(200):
#     # tinny.color(random.choice(colors))
#     tinny.color(random_color())
#     tinny.forward(15)
#     tinny.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tinny.color(random_color())
        tinny.circle(100)
        current_heading = tinny.heading()
        tinny.setheading(current_heading + size_of_gap)
        tinny.circle(100)

draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()