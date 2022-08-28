from turtle import*
speed(0)
pencolor('green')
bgcolor('black')
val=1
while True:
    forward(9*val)
    left(360/6)
    dot(100,'blue')
    circle(10,val)
    val+=1