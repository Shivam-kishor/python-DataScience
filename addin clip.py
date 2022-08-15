import pgzrun
HEIGHT=500
WIDTH=500  

abc=Actor('character_0000',pos=((HEIGHT//2),300))
#alien=Actor('character_0000')
alien=Actor('character_0002')

def draw():
    screen.fill('white')
    abc.draw(    )
    
    def update():
        abc.y +3

pgzrun.go()