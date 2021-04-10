import turtle as t
import random
tim=t.Turtle()
src=t.Screen()
t.colormode(255)
currentheading=tim.heading()
tim.speed("fastest")
def randomcolors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color=(r,g,b)
    return random_color

for i in range(361):
    tim.setheading(currentheading+i)
    tim.color(randomcolors())
    (0,i)
    tim.circle(100)
src.exitonclick()
