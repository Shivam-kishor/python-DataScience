from turtle import *
bgcolor('black')

def rect():
    for i in range(201):#draw rect step by step
        right(1)#angle step
        forward(1)#len of distance
def circle():
    fillcolor('green')
    begin_fill()
    left(140)
    forward(113)
    rect()#left rect
    left(120)
    rect()#right rect
    forward(112)
    end_fill()



circle()


mainloop()
