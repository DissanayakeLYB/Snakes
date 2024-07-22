import pygame

pygame.init()

# #game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player  size
player = pygame.Rect((300, 250, 25, 25))

# food
food = pygame.Rect((500, 350, 25, 25))

# #game loop
run = True
while run:
    # to add color to the background or a trail will be left by moving things
    screen.fill((0, 0, 0))

    # adding a movable red player to the game
    pygame.draw.rect(screen, (0, 255, 0), player)

    # adding the food to the game
    pygame.draw.rect(screen, (255, 0, 0), food)

    # keyboard controls of the games
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    # #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
