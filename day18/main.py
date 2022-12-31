from turtle import Turtle, Screen, colormode
import random

timmy_the_turtle = Turtle()
colormode(255)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# timmy_the_turtle.left(90)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon nonagon and decagon
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

# directions = [0, 90, 180, 270]
# for a in range(3, 11):
#     timmy_the_turtle.color(random.choice(colors))
#     for _ in range(a):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/a)

# Draw a random walk
# timmy_the_turtle.width(10)

# for _ in range(100):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.setheading(random.choice(directions))


# Make a Spirograph
angle = 0
timmy_the_turtle.speed("fastest")
while angle != 360:
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    angle += 5
    timmy_the_turtle.seth(angle)



screen = Screen()
screen.exitonclick()