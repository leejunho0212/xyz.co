import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(100):
    a = random.randint(1, 360)
    t.setheading(a)
    t.forward(50)
