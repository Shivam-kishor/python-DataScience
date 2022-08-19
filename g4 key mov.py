import pgzrun
HEIGHT=700
WIDTH=1400
pic1=Actor('character_0014',topright=(300,200))#by user keyboard
pic2=Actor('character_0024',pos=(50,89))#by system


speed=6  
#music.play('waves')

def draw():
    screen.fill('black')
    pic1.draw()
    pic2.draw()

def update():
    #pic2 x axis movement
    pic2.x+=3 
    if pic2.x>WIDTH: 
        pic2.x=0 
        
    #pic1 x&y axis movement VIA KEYBOARD
    if keyboard.left:
        pic1.x-=speed
        if pic1.x<0:
            pic1.x=WIDTH

    
    if keyboard.right:
        pic1.x+=speed
        if pic1.x>WIDTH:
            pic1.x=0

    if keyboard.up:
        pic1.y-=speed
        if pic1.y<0:
            pic1.y=HEIGHT
    if keyboard.down:
        pic1.y+=speed
        if pic1.y>HEIGHT:
            pic1.y=0
    if pic2.colliderect(pic1):
        #sounds.waves.play() #only waves file alowed
        sounds.sound2.play()



pgzrun.go()        