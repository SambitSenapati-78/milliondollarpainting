import random
import turtle as turtle_module
import colorgram
from turtle import Turtle, Screen
color_dictionary = {}
color_codec = []
total_colors = 22
colors = colorgram.extract('hirst.jpg', total_colors)

for color in range(total_colors):
    extracted_color = colors[color]
    rgb = extracted_color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    my_tuple = (r, g, b)
    color_codec.append(my_tuple)

turtle_module.colormode(255)
scoot = Turtle()
scoot.penup()
scoot.setheading(225)
scoot.forward(300)
scoot.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    scoot.dot(20, random.choice(color_codec))
    scoot.forward(50)
    if dot_count % 10 == 0:
        scoot.setheading(90)
        scoot.forward(50)
        scoot.setheading(180)
        scoot.forward(500)
        scoot.setheading(0)
scoot.isvisible()
my_screen = Screen()
my_screen.exitonclick()


# scoot.shape("circle")
# scoot.home()
# for i in range(10):
#     for j in range(10):
#         scoot.pendown()
#         scoot.dot(20)
#         scoot.penup()
#         scoot.forward(50)
#     scoot.backward(50 * 10)
#     scoot.right(90)
#     scoot.forward(50)
#     scoot.left(90)
