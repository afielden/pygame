"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example
 
Explanation video: http://youtu.be/8IRyt7ft7zg
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
 
import pygame
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    prev_x = 0
    prev_y = 0
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        #self.image = pygame.Surface([15, 15])
        #self.image.fill(WHITE)
        self.image = pygame.image.load("/home/andrew/pygame/images/PNG/Hulls_Color_D/Hull_01_64.png").convert()
        
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def rot_center(self, angle):
    
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = rotated_image.get_rect()
        self.image = rotated_image

 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
        #print('change_x ', self.change_x, ' change_y ', self.change_y)

    def setposition(self, x, y):

        
        print('prev = ', self.rect, ' ', x, ' ', y)
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        if (x > self.change_x and y == self.change_y):
            print('rotating')
            self.rot_center(10)
        else:
            print('moving')
            self.rect.x += x
            self.rect.y += y

        self.change_x = x
        self.change_y = y
        print('new = ', self.rect)

        #print(f"x={self.rect.x} y={self.rect.y} dx={x} dy={y}")

    def stop(self):
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        #self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            #print('hit wall ')
            #print('self: ', self.rect, ' block: ', block.rect)

            # print(abs(self.rect.left - block.rect.right))
            # if (abs(self.rect.left - block.rect.right) < 3):
            #     print('hit right')
            #     if (self.rect.x <= self.prev_x):
            #         self.rect.x = self.prev_x
            # elif (abs(self.rect.right - block.rect.left) < 3):
            #     print("hit left")
            #     if (self.rect.x > self.prev_x):
            #         self.rect.x = self.prev_x
            # elif (self.rect.top == block.rect.bottom-1):
            #     print("hit bottom")
            # elif (self.rect.bottom == block.rect.top+1):
            #     print("hit top")

            # if (self.rect.x < self.prev_x and self.rect.x < block.rect.right):
            #     self.rect.x = self.prev_x
            # elif (self.rect.y < self.prev_y and self.rect.y < block.rect.bottom):
            #     self.rect.y = self.prev_y

            self.rect.x = self.prev_x
            self.rect.y = self.prev_y
            #print('new self ', self.rect)
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(200,200, 100, 100)
wall_list.add(wall)
all_sprite_list.add(wall)
 
# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print('joysticks = ', joysticks)
speed = 2
dy = 0
dx = 0
 
while not done:
 
    for event in pygame.event.get():

        # axis_x, axis_y = (joysticks[0].get_axis(0), joysticks[0].get_axis(1))

        # player.setposition(speed * axis_x, speed * axis_y)
        
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.JOYBUTTONDOWN:
            print('joystick down event')

        

        # if abs(axis_x) > 0.1:
        #     dx = speed * axis_x
        #     player.setposition(dx, dy)
        # if abs(axis_y) > 0.1:
        #     dy = speed * axis_y
        #     player.setposition(dx, dy)
        

        # elif event.type == pygame.JOYAXISMOTION:
        #     print(f"axis = {event.axis} {event.value}")
        #     if event.axis == 0:
        #         # if event.value < 0:
        #         #     player.changespeed(0, event.value/10)
        #         # else:
        #         player.changespeed(event.value/10, 0)
        #     elif event.axis == 1:
        #         # if event.value < 0:
        #         #     player.changespeed(event.value/10, 0)
        #         # else:
        #         player.changespeed(0, event.value/10)

        # elif event.type == pygame.JOYHATMOTION:
        #     if (event.dict['value'] == (0,1)):
        #         player.changespeed(0,-3)
        #     elif (event.dict['value'] == (1,0)):
        #         player.changespeed(3,0)
        #     elif (event.dict['value'] == (0,-1)):
        #         player.changespeed(0,3)
        #     elif (event.dict['value'] == (-1,0)):
        #         player.changespeed(-3,0)
        #     elif (event.dict['value'] == (0,0)):
        #         player.stop()


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
 
    axis_x, axis_y = (joysticks[0].get_axis(0), joysticks[0].get_axis(1))
    player.setposition(speed * axis_x, speed * axis_y)
    #player.rot_center(45)
    all_sprite_list.update()
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()