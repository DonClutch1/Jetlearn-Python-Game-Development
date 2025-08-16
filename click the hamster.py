import pgzrun
from random import randint
TITLE="Shoot The Hamster!"
WIDTH=500
HEIGHT=500
message=" "
score=0
hamster=Actor('hamster')
hamster.pos=60,60
def draw():
    screen.clear()
    screen.fill((0,0,0))
    hamster.draw()
    screen.draw.text(message,center=(400,100),fontsize=35)
    screen.draw.text(str(score),center=(200,120),fontsize=20)
    #place the alien randomly on the screen
def place_hamster():
    hamster.x = randint(50,WIDTH-50)
    hamster.y = randint(50,HEIGHT-50)
#mouse event
score = 0
def on_mouse_down(pos):
    global message
    global score
    if hamster.collidepoint(pos):
        score+=1
        message="GOOD"
        
        place_hamster()
    else:
        message="Better luck next time"
place_hamster()
pgzrun.go()
