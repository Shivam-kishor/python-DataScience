
import pgzrun

#from g3 import HEIGHT, WIDTH
HEIGHT= 700
WIDTH=800

pic1=Actor('character_0006',pos=(300//2,250))
pic2=Actor('character_0015',bottomright=(90,50))

speed=3
def draw():
    screen.fill('black')
    pic1.draw()
    pic2.draw()

def update():
    pic1.x += 1
    if pic1.x> WIDTH:
        pic1.x=0
    if keyboard.left:
        pic2.x-=speed
    if keyboard.right:
        pic2.x+=speed
    if keyboard.up:
        pic2.y-=speed
    if keyboard.down:
        pic2.y+=speed    
    if pic2.colliderect(pic1):
       sounds.sound1.play()



pgzrun.go()
