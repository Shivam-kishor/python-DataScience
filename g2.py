#basic of GUI😁👌

import pgzrun
height =500
width=800

#axis from origin⬇️             #box size⬇️
box1 = Rect((50,50)  ,          (200,300))
box2 =Rect((height//2,width//2),  (100,100))

#music.play('sound1')


#define⬇️
def draw():         
    screen.fill('black')
    screen.draw.rect(box1,'red')
    
    
    screen.draw.rect(box2,'green')

# to append
def update():
    box1.x +=4
    if box1.x>width:
        box1.x=0
    
    box2.x +=4
    if box2.x>height:
        box2.x=0
pgzrun.go()    