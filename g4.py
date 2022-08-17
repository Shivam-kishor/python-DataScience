import pgzrun
HEIGHT=600
WIDTH=800
pic1=Actor('character_0014',topright=(800,200))
pic2=Actor('character_0024',pos=(HEIGHT//2,WIDTH//2))
#doubts
speed=3   
speeds=speed
#music.play('waves')

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
        pic1.x-=speed
    if keyboard.right:
        pic1.x+=speed
    if keyboard.up:
        pic1.y-=speed
    if keyboard.down:
        pic1.y+=speed
    if pic2.colliderect(pic1):
        #sounds.waves.play() #only waves file alowed
        sounds.sound2.play()



pgzrun.go()        