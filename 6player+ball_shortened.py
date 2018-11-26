import pygame

Green = (100, 250, 100)
pad_width = 1024
pad_height = 512

x = [0 for i in range(6)]
y = [0 for i in range(6)]
ball_x=0
ball_y=0

def ballchecker():
    global x, y, ball_x, ball_y

    for i in range(6):
        if abs(ball_x - x[i]) <= 50 and abs(ball_y - y[i]) <= 50:
            ball_x = x[i]
            ball_y = y[i]

def airplane():
    global x, y, ball_x, ball_y
    global gamepad, image, image_ball

    for i in range(6):
        gamepad.blit(image[i], (x[i], y[i]))
    gamepad.blit(image_ball, (ball_x, ball_y))

    #여기에 배열 생성해서 위치 정보 계속 저장

def runGame():
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

            #아래 if문은 배열에 키 넣어놓고 쓰면 될 듯
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    y1_change = -5
                elif event.key == pygame.K_w:
                    y1_change = 5
                elif event.key == pygame.K_q:
                    x1_change = -5
                elif event.key == pygame.K_e:
                    x1_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_2 or event.key == pygame.K_w:
                    y1_change = 0
                elif event.key == pygame.K_q or event.key == pygame.K_e:
                    x1_change = 0

            key = [[K_2, K_q, K_w, K_e], [K_5, K_r, K_t, K_y], [K_8, K_u, K_i, K_o], [K_s, K_z, K_x, K_c], [K_g, K_v, K_b, K_n], [K_UP, K_LEFT, K_DOWN, K_RIGHT]]

            if event.type == pygame.KEYDOWN:
                for i in range(6):
                    player = key[i]
                    for j in range(4):
                        direction = player[j]
                        if event.key == pygame.direction:
                            if j is 0:
                                y_change[i] = 5
                            if j is 1:
                                x_change[i] = -5
                            if j is 2:
                                y_change[i] = -5
                            if j is 3:
                                x_change[i] = 5

            if event.type == pygame.KEYUP:
                for i in range(6):
                    player = key[i]
                    for j in range(4):
                        direction = player[j]
                        if event.key == pygame.direction:
                            if j%2:
                                x_change[i] = 0
                            else:
                                y_change[i] = 0

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

        gamepad.fill(Green)
        airplane()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, image, image_ball, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFootball')

    for i in range(6):
        image[i] = pygame.image.load('image%d.png' % i+1)
    image_ball = pygame.image.load('image_ball.png')


    clock = pygame.time.Clock()
    runGame()

initGame()
