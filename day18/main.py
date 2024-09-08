'''Extracting colors:

import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


print(rgb_colors)
'''
import turtle as t
import random

tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
t.colormode(255)
color_list = [(250, 246, 242), (250, 245, 247), (208, 155, 102), (242, 249, 247), (241, 244, 248), (55, 107, 129), (168, 81, 40), (124, 79, 97), (121, 156, 171), (197, 142, 37), (125, 175, 159), (225, 198, 132), (189, 88, 109), (54, 37, 19), (189, 130, 145), (13, 48, 61), (48, 166, 128), (59, 123, 115), (163, 21, 31), (218, 92, 76)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()