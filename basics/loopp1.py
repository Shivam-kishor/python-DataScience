from turtle import*

speed('slowest')
#forward(100)
#left(36)#degree

#forward(100)
#left(36)

#forward(100)
#left(36)
#
#forward(100)
#left(36)
#
#forward(100)
#left(36)
#

#forward(100)

#left(36)

#

#forward(100)

#left(36)

#

#

#forward(100)

#left(36)

#

#

#forward(100)

#left(36)

#

#forward(100)

#left(36)

#

#

#forward(100)

#left(36)

#forward(100)

#left(36)

#forward(100)

#left(36)

#forward(100)

#left(36)

#forward(100)

#left(36)



print ('------------------------via LOOP----------------------------')
#for i in range(12):
#    forward(100)
#    left(30)

sides=int(input('enter side OR Distance to draw shape'))#angle turn
distance=int(input('how far do u want 2 go'))#straight
fillcolor('blue')


for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill
mainloop()