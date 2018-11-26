import pygame
from pygame import *
baller = [0, 0, 0, 0, 0, 0]
Green = (100, 250, 100)
pad_width = 1024
pad_height = 512
player_x=0
player_y=0

x = [0 for i in range(6)]
y = [0 for i in range(6)]
ball_x = 0
ball_y = 0

def ball_move(player_x, player_y):
    global dis, ball
    dis.blit(ball, (player_x,player_y))

def ball_direction(player_x, player_y, ball_x, ball_y):
    if player_x - ball_x > 0:
        if player_y- ball_y > 0:
            return 'Ball LeftUp'
        if player_y- ball_y == 0:
            return 'Ball Left'
        if player_y- ball_y < 0:
            return 'Ball LeftDown'
    if player_x - ball_x == 0:
        if player_y- ball_y > 0:
            return 'Ball Up'
        if player_y- ball_y == 0:
            return 'Ball Stop'
        if player_y- ball_y < 0:
            return 'Ball Down'
    if player_x - ball_x < 0:
        if player_y- ball_y > 0:
            return 'Ball RightUp'
        if player_y- ball_y == 0:
            return 'Ball Right'
        if player_y- ball_y < 0:
            return 'Ball RightDown'

def ball_pass(player_x, player_y, dir):
    if dir == 'Ball Left':
        for i in range(1,50):
            ball_move(player_x-12*i, player_y)
            pygame.display.update()
    if dir == 'Ball Right':
        for i in range(1,50):
            ball_move(player_x+12*i, player_y)
            pygame.display.update()
    if dir == 'Ball Up':
        for i in range(1,50):
            ball_move(player_x, player_y-12*i)
            pygame.display.update()
    if dir == 'Ball Down':
        for i in range(1,50):
            ball_move(player_x, player_y+12*i)
            pygame.display.update()
    if dir == 'Ball LeftUp':
        for i in range(1,50):
            ball_move(player_x-12*i, player_y-12*i)
            pygame.display.update()
    if dir == 'Ball RightUp':
        for i in range(1,50):
            ball_move(player_x+12*i, player_y-12*i)
            pygame.display.update()
    if dir == 'Ball LeftDown':
        for i in range(1,50):
            ball_move(player_x-12*i, player_y+12*i)
            pygame.display.update()
    if dir == 'Ball RightDown':
        for i in range(1,50):
            ball_move(player_x+12*i, player_y+12*i)
            pygame.display.update()
    return

def goalchcker():
    global ball_y, ball_x, image_goalsign
    if (0 < ball_x < 75 or 437< ball_x < 512) and (206 < ball_y < 306):
        gamepad.blit(image_goalsign, (256, 512))

def ballchecker():
    global x, y, ball_x, ball_y, baller

    for i in range(6):
        if abs(ball_x - x[i]) <= 50 and abs(ball_y - y[i]) <= 50:
            ball_x = x[i]
            ball_y = y[i]
            for j in (0, 5):
                baller[j]=0
            baller[i]=1



def airplane():
    global x, y, ball_x, ball_y
    global gamepad, image, image_ball, baller

    for i in range(6):
        gamepad.blit(image[i], (x[i], y[i]))
    gamepad.blit(image_ball, (ball_x, ball_y))

    # 여기에 배열 생성해서 위치 정보 계속 저장


def runGame():
    global player_x, player_y
    global x, y, ball_x, ball_y
    global gamepad, image, image_ball
    for i in range(6):
        x[i] = pad_width * 0.05
        y[i] = pad_height * 0.8
    ball_x = 0
    ball_y = 0

    x_change = [0 for i in range(6)]
    y_change = [0 for i in range(6)]
    ball_x_change = 0
    ball_y_change = 0

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                break

            key = [[K_2, K_q, K_w, K_e], [K_5, K_r, K_t, K_y], [K_8, K_u, K_i, K_o], [K_s, K_z, K_x, K_c],
                   [K_g, K_v, K_b, K_n], [K_UP, K_LEFT, K_DOWN, K_RIGHT]]

            if event.type == pygame.KEYDOWN:
                for i in range(6):
                    player = key[i]
                    for j in range(4):
                        direction = player[j]
                        if event.key == direction:
                            if j is 0:
                                y_change[i] = -5
                            if j is 1:
                                x_change[i] = -5
                            if j is 2:
                                y_change[i] = 5
                            if j is 3:
                                x_change[i] = 5

            if event.type == pygame.KEYUP:
                for i in range(6):
                    player = key[i]
                    for j in range(4):
                        direction = player[j]
                        if event.key == direction:
                            if j % 2:
                                x_change[i] = 0
                            else:
                                y_change[i] = 0


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_S3PACE:
                    print("Ball Shoot")
                    ball_pass(ball_x, ball_y, dir)

        for i in (0, 5):
            if baller[i] == 1:
                player_x = x[i]
                player_y = y[i]

        dir = ball_direction(player_x, player_y, ball_x, ball_y)

        for i in range(6):
            x[i] += x_change[i]

            if x[i] < 0:
                x[i] = 0
            if x[i] > pad_width:
                x[i] = pad_width

            y[i] += y_change[i]

            if y[i] < 0:
                y[i] = 0
            if y[i] > pad_height:
                y[i] = pad_height

        ball_x += ball_x_change

        if ball_x < 0:
            ball_x = 0
        if ball_x > pad_width:
            ball_x = pad_width

        ball_y += ball_y_change

        if ball_y < 0:
            ball_y = 0
        if ball_y > pad_height:
            ball_y = pad_height

        ballchecker()
        goalchcker()
        gamepad.fill(Green)
        airplane()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def initGame():
    global gamepad, image, image_ball, clock, image_goalsign

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    image = [0 for i in range(6)]
    pygame.display.set_caption('PyFootball')

    for i in range(6):
        image[i] = pygame.image.load('image%d.png' % (i + 1))
    image_ball = pygame.image.load('image_ball.png')
    image_goalsign = pygame.image.load('image_goalsign.png')

    clock = pygame.time.Clock()
    runGame()


initGame()
