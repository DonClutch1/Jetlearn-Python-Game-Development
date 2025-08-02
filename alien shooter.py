import pgzrun
from random import randint
#pygame standard for adding the title and with the height of the game screen.
TITLE="Shoot The Alien!!!"
#screen setup
WIDTH=500
HEIGHT=500
#variable to store a message
message=" "
score=0
#adding the character
alien=Actor('alien')
alien.pos=60,60
#funtion to update the screen
def draw():
    screen.clear()
    screen.fill((0,0,0))
    #place the actor
    alien.draw()
    screen.draw.text(message,center=(400,100),fontsize=35)
    screen.draw.text(str(score),center=(200,120),fontsize=20)
    #place the alien randomly on the screen
def place_alien():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)
#mouse event
score = 0
def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        score+=1
        message="GOOD"
        
        place_alien()
    else:
        message="Better luck next time"
place_alien()
pgzrun.go()
