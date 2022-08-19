import pgzrun


HEIGHT=500
WIDTH=500
pic1=Actor('character_0022',pos=(HEIGHT//2,WIDTH//2))

def draw():
    screen.fill('white')
    pic1.draw()

def update():
    #pic1.x-=1
    #if pic1.x<0:
    #        pic1.x=WIDTH
  
  
    pic1.y+=3 #speed control
    if pic1.y>HEIGHT:
        pic1.y =0
pgzrun.go()
