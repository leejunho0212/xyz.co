import turtle as t
import random

te = t.Turtle()                 #te : 악당 거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

tf = t.Turtle()                 #tf : 먹이
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(9)

    if t.distance(tf) < 12:                     # tf가 12보다 작으면
        star_x = random.randint(-230, 230)      
        star_y = random.randint(-230, 230)
        tf.goto(star_x, star_y)         # (-230,230) 사이에 새로운 먹이가 랜덤으로 생성

    if t.distance(te) >= 12:                    # te가 12보다 크거나 같으면
        t.ontimer(play, 100)    # 0.1초 마다 play() 호출 # 시간은 mili second

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")

t.listen()
play()
