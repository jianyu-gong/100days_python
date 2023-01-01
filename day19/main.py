from turtle import Turtle, Screen
import random
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def move_left():
#     tim.left(5)

# def move_right():
#     tim.right(5)

# def clear_screen():
#     tim.home()
#     tim.clear()


# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear_screen, "c")
# screen.exitonclick()

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_offsite = [-70, -40, -10, 20, 50]
all_turtles = []


for i in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_offsite[i])
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()

if user_bet == winning_turtle:
    print("You guessed right!")

else:
    print(f"You guessed wrong! The {winning_turtle} wins the race.")
screen.exitonclick()