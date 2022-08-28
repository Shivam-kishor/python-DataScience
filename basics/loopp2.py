from turtle import*
colors=['red','blue','green']
pensize(7)
for i in range(3):
    pencolor(colors[-(i+1)])
    forward(100)
    left(360/3)
    #circle(40)
dot(i*10)

mainloop()
