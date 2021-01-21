import pygame, sys

def draw_floor():
        screen.blit(floor_surface, (floor_x_pos,900))
        screen.blit(floor_surface, (floor_x_pos + 576, 900))


pygame.init()

#create window
screen = pygame.display.set_mode((576,1024))

#clock for frame rate
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

while True:

    #exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(bg_surface, (0,0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0








    pygame.display.update()
    #frame rate
    clock.tick(120)
