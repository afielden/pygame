import pygame
pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pos = [size[0]/2, size[1]/2]
speed = 5
joystick = None

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                done = True

    if joystick:
        axis_x, axis_y = (joystick.get_axis(0), joystick.get_axis(1))
        if abs(axis_x) > 0.1:
            pos[0] += speed * axis_x
        if abs(axis_y) > 0.1:
            pos[1] += speed * axis_y
    else:
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            print("joystick initialized")

    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (255,255,255), (*pos, 10, 10))
    pygame.display.flip()
    