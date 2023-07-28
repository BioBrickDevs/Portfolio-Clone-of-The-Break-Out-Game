import pygame
import random

colors = ["green", "yellow", "purple"]


pygame.init()
pygame.font.init()

score_text = pygame.font.SysFont("Comic Sans MS", 30)
lives_text = pygame.font.SysFont("Comic Sans MS", 30)

main_screen_text = pygame.font.SysFont("Comic Sans MS", 30)


clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((1280, 720))
game_started = False
box = pygame.Rect((100, 100), (200, 30))
# define the start postion of the paddle
box.bottom = 680
box.centerx = 1280 / 2

# define game started to start playing after main screen

list_of_boxes = []
# adds boxes to the screen to be shoot at
for x in range(6, 1280, 64):
    box_to_be_added = pygame.Rect(
        (x, 100),
        (50, 30),
        borders=0,
    )
    box_to_be_added_2 = pygame.Rect((x, 200), (50, 30), borders=0)
    box_to_be_added_3 = pygame.Rect((x, 300), (50, 30), borders=0)
    list_of_boxes.append(box_to_be_added)
    list_of_boxes.append(box_to_be_added_2)
    list_of_boxes.append(box_to_be_added_3)


# movement for the ball
move_x = box.centerx  # defines start postion for the ball
move_y = box.top - 8  # defines start postion for the ball
movement_y = -5
one_time = True
score = 0
lives = 3
random_number = random.randint(1, 2)
level = 1

level_cleared = False
if random_number == 1:
    movement_x = 3
else:
    movement_x = -3

# detect if ball is released
ball_release = False
# detect if ball is hit and must change direction
hit = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while not game_started:
        screen.fill((0, 18, 51))
        line_height = 20
        for (
            row_of_text
        ) in "Breakout Game Clone\n Control the paddle with left and \n right key\npress enter to start the game and when playing press space to send the ball".split(
            "\n"
        ):
            main_screen_surface = main_screen_text.render(
                row_of_text, True, (247, 157, 101)
            )
            screen.blit(main_screen_surface, (10, line_height))
            line_height += 30
        print("display here start screen when red")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_started = True

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                game_started = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 18, 51))

    # RENDER YOUR GAME HERE
    if box:
        pygame.draw.rect(screen, (51, 65, 92), box, 0, 5)
    for x in list_of_boxes:
        pygame.draw.rect(screen, (3, 83, 164), x, 0, 3)

    ball = pygame.draw.circle(screen, (247, 157, 101), (move_x, move_y), 8)
    # borders = pygame.draw.rect(screen, "black", (0, 0, 1280, 720), 3)
    for index, x in enumerate(list_of_boxes):
        if x.colliderect(ball):  # target hits with ball
            hit = True
            score += 20
            list_of_boxes.pop(index)
            print(hit)
            movement_y *= -1
            hit = False
            print(ball.left)

            if x.collidepoint(ball.midleft) or x.collidepoint(ball.midright):
                print("collision")
                movement_y *= -1
                movement_x *= -1

        else:
            hit = False

    if not list_of_boxes:
        level_cleared = True

    # if game level is cleared then reset and speed up
    if level_cleared:
        level_cleared = False
        pause = True
        level += 1
        while pause:
            screen.fill((0, 18, 51))
            line_height = 20
            for (
                row_of_text
            ) in f"{level -1} level cleared.\n press enter to start but\
            remember the game is \n now faster be careful!".split(
                "\n"
            ):
                main_screen_surface = main_screen_text.render(
                    row_of_text, True, (247, 157, 101)
                )
                screen.blit(main_screen_surface, (10, line_height))
                line_height += 30
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pause = False

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    running = False
                    pause = False

                if keys[pygame.K_RETURN]:
                    pause = False

                    # reset the game if user wants to play again
                    move_x = box.centerx  # defines start postion for the ball
                    move_y = box.top - 8  # defines start postion for the ball

                    movement_y = -5
                    random_number = random.randint(1, 2)

                    if random_number == 1:
                        movement_x = 3
                    else:
                        movement_x = -3
                    one_time = True
                    box.bottom = 680
                    box.centerx = 1280 / 2
                    move_x = box.centerx  # defines start postion for the ball
                    move_y = box.top - 8  # defines start postion for the ball

                    lives = 3
                    list_of_boxes = []
                    ball_release = False
                    # adds boxes to the screen to be shoot at
                    for x in range(6, 1280, 64):
                        box_to_be_added = pygame.Rect(
                            (x, 100),
                            (50, 30),
                            borders=0,
                        )
                        box_to_be_added_2 = pygame.Rect((x, 200), (50, 30), borders=0)
                        box_to_be_added_3 = pygame.Rect((x, 300), (50, 30), borders=0)
                        list_of_boxes.append(box_to_be_added)
                        list_of_boxes.append(box_to_be_added_2)
                        list_of_boxes.append(box_to_be_added_3)

                    pygame.display.flip()

        print("level cleared")
        print("display_level_cleared")

        level_cleared = False

    # if ball hits the paddle
    if box.colliderect(ball):
        hit = True

        if ball.centery >= box.top:
            if one_time:
                one_time = False
                movement_x *= -1
                print("pöö")

        else:
            movement_y *= -1

    if ball.top > 720:  # if ball goes out of the screen bellow the paddle
        lives -= 1
        if lives > 0:
            print("death")
            move_x = box.centerx  # defines start postion for the ball
            move_y = box.top - 8  # defines start postion for the ball
            ball_release = False
            movement_y *= -1
            random_number = random.randint(1, 2)

            if random_number == 1:
                movement_x = 3
            else:
                movement_x = -3

        else:
            game_over = True
            while game_over:
                screen.fill((0, 18, 51))
                line_height = 20
                for (
                    row_of_text
                ) in "Game over \n Press enter to play again.  \n press  ESC to quit. ".split(
                    "\n"
                ):
                    main_screen_surface = main_screen_text.render(
                        row_of_text, True, (247, 157, 101)
                    )
                    screen.blit(main_screen_surface, (10, line_height))
                    line_height += 30
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_over = False

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        running = False
                        game_over = False

                    if keys[pygame.K_RETURN]:
                        game_over = False
                        print()
                        # reset the game if user wants to play again
                        move_x = box.centerx  # defines start postion for the ball
                        move_y = box.top - 8  # defines start postion for the ball

                        movement_y = -5
                        one_time = True
                        score = 0
                        box.bottom = 680
                        box.centerx = 1280 / 2
                        move_x = box.centerx  # defines start postion for the ball
                        move_y = box.top - 8  # defines start postion for the ball
                        level = 1
                        lives = 3
                        list_of_boxes = []
                        ball_release = False
                        # adds boxes to the screen to be shoot at
                        for x in range(6, 1280, 64):
                            box_to_be_added = pygame.Rect(
                                (x, 100),
                                (50, 30),
                                borders=0,
                            )
                            box_to_be_added_2 = pygame.Rect(
                                (x, 200), (50, 30), borders=0
                            )
                            box_to_be_added_3 = pygame.Rect(
                                (x, 300), (50, 30), borders=0
                            )
                            list_of_boxes.append(box_to_be_added)
                            list_of_boxes.append(box_to_be_added_2)
                            list_of_boxes.append(box_to_be_added_3)

                        pygame.display.flip()

            print("Put here your program code for death")
            print("Display score and if restart")

    else:
        hit = False

    score_surface = score_text.render(f"Score: {score}", True, (4, 102, 200))
    lives_surface = score_text.render(f"Lives: {lives}", True, (4, 102, 200))

    screen.blit(score_surface, (10, 0))
    screen.blit(lives_surface, (1160, 0))
    # if borders.colliderect(ball):
    # hit = True
    # movement_y*=-1
    # else:
    # hit = False

    # checks for if the ball hits left or right of window
    if ball.left < 0 + 4 or ball.right > 1280 - 4:
        movement_x *= -1
    # checks if the ball hits top of window
    if ball.top < 4:
        movement_y *= -1

        print(ball.left, ball.right, ball.top)
        hit = True
    else:
        hit = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        # Move Down
        # l_paddle.down()
        if not(box.left < 0):
            box = box.move(-6, 0)

    if keys[pygame.K_RIGHT]:
        # l_paddle.up()
        if not(box.right >1280):
            box = box.move(6, 0)

    if keys[pygame.K_SPACE]:
        ball_release = True

    if ball_release:
        # if hit:
        # movement_y *= -1
        # else:
        # movement *= -1
        # pass
        move_x += movement_x
        move_y += movement_y
    else:
        move_x = box.centerx  # defines start postion for the ball
        move_y = box.top - 8  # defines start postion for the ball

    if running:
        pygame.display.flip()
    if level == 1:
        clock.tick(60)
    else:
    
        clock.tick(round(60 + (5 * level), 0))  # limits FPS to 60

pygame.quit()
