from turtle import  Turtle, Screen, colormode
import random
tim = Turtle()
screen = Screen()
colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(58, 106, 148), (225, 200, 109), (134, 84, 58), (223, 139, 64), (196, 145, 171), (224, 234, 230), (234, 226, 203), (142, 179, 204), (139, 81, 105)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
