import colorgram
import random
from turtle import Turtle, Screen, colormode


colors_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
               (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
               (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
               (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]


def draw_randomly_colored_dot(tim):
    tim.dot(20, random.choice(colors_list))


def hirst_painting(tim):
    tim.penup()
    tim.setposition(-250, 200)
    x = tim.xcor()
    y = tim.ycor()
    for _ in range(10):
        for _ in range(10):
            draw_randomly_colored_dot(tim)
            tim.forward(50)
        y -= 50
        tim.setposition(x, y)

# colors = colorgram.extract("image.jpg", 25)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)

tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.speed(0)
tim.hideturtle()
hirst_painting(tim)

screen = Screen()
screen.exitonclick()
