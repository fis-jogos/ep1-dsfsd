import random

WIDTH = 1024
HEIGHT = 768
cfv = 0.3
viscosidade = -cfv
gameover = False
score = 0
gravidade = 3

#actors
player = Actor('player', pos=(200, HEIGHT / 2))
redfish = Actor('redfish')
yellowfish = Actor('yellowfish')
seahorse = Actor('seahorse')
seahorse.vx = 0
seahorse.vy = 0
yellowfish.vx = 0
yellowfish.vy = 0
redfish.vx = 0
redfish.vy = 0


def pos_inic():
  return (1024, random.randint(0, HEIGHT))

def vel_inic_yellowfish():
  return (random.randint(-15, -10), 0)

def vel_inic_seahorse():
  return (random.randint(-13, -7), 0)

def vel_inic_redfish():
  return (random.randint(-9, -5), 0)


def pos_yellowfish():
    #posição inicial do yellowfish
    (yellowfish.x, yellowfish.y) = pos_inic()
    #velocidade inicial do yellowfish
    (yellowfish.vx, yellowfish.vy) = vel_inic_yellowfish()

def pos_seahorse():
    #posição inicial do seahorse
    (seahorse.x, seahorse.y) = pos_inic()
    #velocidade inicial do seahorse
    (seahorse.vx, seahorse.vy) = vel_inic_seahorse()

def pos_redfish():
    #posição inicial do redfish
    (redfish.x, redfish.y) = pos_inic()
    #velocidade inicial do redfish
    (redfish.vx, redfish.vy) = vel_inic_redfish()

def initialPositions():
    global score
    global gameover
    player.pos = 200, HEIGHT / 2
    pos_yellowfish()
    pos_redfish()
    pos_seahorse()

def score_update():
    global score
    score = score + 1

initialPositions()

def draw():
    screen.clear()
    screen.blit('background', pos=(0, 0))
    player.draw()
    redfish.draw()
    yellowfish.draw()
    seahorse.draw()
    screen.draw.text("Score : " + str(score), center=(WIDTH/2 - 100, HEIGHT - 80))
    if gameover:
        screen.draw.text("GAME OVER!", center=(WIDTH/2, HEIGHT/2))
        screen.draw.text("(r para reiniciar)", center=(WIDTH/2, HEIGHT/2 + 20))

def updateplayer():
    player.y+= (gravidade*viscosidade)+gravidade

    if keyboard.left and player.left > 2:
        player.x -= 5*viscosidade+5
        if player.image != 'player0':
            player.image = 'player0'

    if keyboard.right and player.right < WIDTH+2:
        player.x += 5*viscosidade+5
        if player.image != 'player':
            player.image = 'player'

    if keyboard.up and player.top > 2:
        player.y -= 5*viscosidade+5

    if keyboard.down and player.bottom > 2:
        player.y += 5*viscosidade+5

def updateyellowfish():
    if yellowfish.right < 0:
        pos_yellowfish()
        score_update()
    yellowfish.x += yellowfish.vx * viscosidade + yellowfish.vx
    yellowfish.y += yellowfish.vy * viscosidade + yellowfish.vy

def updateseahorse():
    if seahorse.right < 0:
        pos_seahorse()
        score_update()
    seahorse.x += seahorse.vx * viscosidade + seahorse.vx
    seahorse.y += seahorse.vy * viscosidade + seahorse.vy

def updateredfish():
    if redfish.right < 0:
        pos_redfish()
        score_update()
    redfish.x += redfish.vx * viscosidade + redfish.vx
    redfish.y += redfish.vy * viscosidade + redfish.vy

def update(dt):
    global score
    global gameover

    if not gameover:
        updateplayer()
        updateseahorse()
        updateyellowfish()
        updateredfish()
    else:
        if keyboard.r:
            initialPositions()
            gameover = False
            score = 0

    collision = player.colliderect(yellowfish)
    collision2 = player.colliderect(seahorse)
    collision3 = player.colliderect(redfish)

    if collision:
        gameover = True

    if collision2:
        gameover = True

    if collision3:
        gameover = True
