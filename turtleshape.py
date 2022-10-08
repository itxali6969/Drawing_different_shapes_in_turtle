import turtle as t
import random
uzair = t.Turtle()
colours = ["red", "green", "yellow", "tan", "brown", "grey", "black"]
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        uzair.forward(100)
        uzair.right(angle)
for shape_side_n in range(3,11):
    uzair.color(random.choice(colours))
    draw_shape(shape_side_n)
