import turtle as t

t.bgcolor('black')
t.shape("turtle")
t.color('yellow')

t.penup()
t.goto(100,100)
t.pendown()

t.speed(50)

angle = 90

for x in range (500):
    t.forward(x)
    t.left(angle)
