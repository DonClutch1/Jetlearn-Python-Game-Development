import pgzrun
from random import randint
WIDTH=600
HEIGHT=500
score=0
game_over=False

ash=Actor("ash")
ash.pos=100,100

pika=Actor("pika")
pika.pos=200,200

def draw():
    screen.blit("ground",(0,0))
    ash.draw()
    pika.draw()
    screen.draw.text("Score : "+str(score), color="black", topleft=(10,10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's Up! Your final score is: "+str(score), midtop=(WIDTH/2,10), fontsize=40, color="red")
def place_pika():
    pika.x=randint(70, (WIDTH-70))
    pika.y=randint(70, (HEIGHT-70))
def times_up():
    global game_over
    game_over=True
def update():
    global score
    if keyboard.left:
        ash.x = ash.x - 3
    if keyboard.right:
        ash.x = ash.x + 3
    if keyboard.up:
        ash.y = ash.y - 3
    if keyboard.down:
        ash.y = ash.y + 3
    flower_collected = ash.colliderect(pika)
    if flower_collected:
        score = score + 10
        place_pika()
clock.schedule(times_up, 60.0)
pgzrun.go()
