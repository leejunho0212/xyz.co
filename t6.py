import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.penup()

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()

                                            #on으로 시작하는 모든 함수는 이벤트 핸들러
window.onkeypress(turn_right,"Right")       # "Right" 눌렀을 때 turn_right() 호출
window.onkeypress(turn_up,"Up")             # "Up" 눌렀을 때 turn_up() 호출
window.onkeypress(turn_left,"Left")         # "Left" 눌렀을 때 turn_left() 호출
window.onkeypress(turn_down,"Down")         # "Down" 눌렀을 때 turn_down() 호출
window.onkeypress(blank,"Escape")           # "Escape" 눌렀을 때 blank() 호출

window.listen()

window.mainloop()
