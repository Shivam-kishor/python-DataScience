#dfrom turtle import Screen
import pgzrun
HEIGHT =500
WIDTH= 800

linux = Actor('linux',pos=(WIDTH//2,220))
def draw():
    screen.fill('white')
    linux.draw()
    
def update():
    linux.x -=3
    if linux > WIDTH:
        linux.x=0
    


pgzrun.go() 