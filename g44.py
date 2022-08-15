import pgzrun
HEIGHT=600
WIDTH=800
pic1=Actor('character_0014',topright=(800,200))
pic2=Actor('character_0024',pos=(HEIGHT//2,WIDTH//2))
speed=3
def draw():
    screen.fill('black')
    pic1.draw()
    pic2.draw()

def update():
    #pic2 x axis movement
    pic2.x+=speed 
    if pic2.x>WIDTH: 
        pic2.x=0 
        
    #pic1 x&y axis movement VIA KEYBOARD
    if keyboard.left:
        pic1.x-=0
    if keyboard.right:
        pic1.x+=0
    if keyboard.up:
        pic1.y-=0
    if keyboard.down:
        pic1.y+=0




pgzrun.go()        