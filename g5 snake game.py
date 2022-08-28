#from turtle import width
import pgzrun
import pgzrun
from random import randint
HEIGHT=500
WIDTH=900
score=0
snake=Actor("character_0007",pos=(WIDTH//2,HEIGHT//2))
food=Actor('character_0015',pos=(50,50))
speed=3
def draw():
    screen.fill('black')
    snake.draw()
    food.draw()
    screen.draw.text(f'SCORE:{score}',topleft=(10,500-40),color='white')

    def update():
        global score
        snake.x +=speed
        if keyboard.up:
            snake.y -=speed
        if keyboard.down:
            snake.y +=speed
        if keyboard.left:
            snake.x -=speed
        if keyboard.right:
            snake.x +=speed 

            #boundary control
        if snake.x>WIDTH:
            snake.x=0
        if snake.x<0:
            snake.x=0
        if snake.y>HEIGHT:
            snake.y=0
        if snake.y<0:
            snake.y=0

        if snake.collidercet(food):
            score+=1
            food.x=randint(0,WIDTH)
            food.x=randint(0,WIDTH)
            food.y
            sounds.sound1.play()
pgzrun.go()