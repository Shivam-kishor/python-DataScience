
import pgzrun
HEIGHT =500
WIDTH=800

#axis from origin⬇️    #box size⬇️
box = Rect((50,50),(100,100))
box2 =Rect((HEIGHT//2,WIDTH//2),(100,100))

def draw():         
    screen.fill('white')
    screen.draw.rect(box,'red')
    
    screen.fill("white")
    screen.draw.rect(box,'pink')
def update():
    box.x +=4
    if box.x>WIDTH:
        box.x=0
    
    box2.x +=4
    if box2.x>HEIGHT:
        box2.x=0
pgzrun.go()    