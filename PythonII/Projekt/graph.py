import pygame, os

pygame.init()
#kolory
BLACK = pygame.color.THECOLORS['black']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
LIGHTGREEN = pygame.color.THECOLORS['lightgreen']
B_BLUE = pygame.Color('#e6f2ff')
PINK = pygame.Color('#f4427d')

# grafika player
stand_R = pygame.image.load(os.path.join('png', 'alien_stand_R.png'))
stand_L = pygame.image.load(os.path.join('png', 'alien_stand_L.png'))
walk_R1 = pygame.image.load(os.path.join('png', 'alien_walk1_R.png'))
walk_L1 = pygame.image.load(os.path.join('png', 'alien_walk1_L.png'))
walk_R2 = pygame.image.load(os.path.join('png', 'alien_walk2_R.png'))
walk_L2 = pygame.image.load(os.path.join('png', 'alien_walk2_L.png'))
up_R = pygame.image.load(os.path.join('png', 'alien_climb_R.png'))
up_L = pygame.image.load(os.path.join('png', 'alien_climb_L.png'))
image_left = [walk_L1, walk_L2]
image_right = [walk_R1, walk_R2]
image_up = [up_R, up_L]

#grafika platformy
PLATFORM_L = pygame.image.load(os.path.join('png', 'platf_L.png'))
PLATFORM_M = pygame.image.load(os.path.join('png', 'platf_M.png'))
PLATFORM_R = pygame.image.load(os.path.join('png', 'platf_R.png'))

#grafika wrogow
SPACE_L = pygame.image.load(os.path.join('png', 'spaceRocket_L.png'))
SPACE_R = pygame.image.load(os.path.join('png', 'spaceRocket_R.png'))
STAR = pygame.image.load(os.path.join('png', 'star.png'))
GROUND_LIST = [PLATFORM_L, PLATFORM_M, PLATFORM_R]

#grafika itemów
HEART = pygame.image.load(os.path.join('png', 'heart.png'))
WIN = pygame.image.load(os.path.join('png', 'ufoBlue.png'))
DRUG = pygame.image.load(os.path.join('png', 'pill_red.png'))
FRIEND1 = pygame.image.load(os.path.join('png', 'beige.png'))
FRIEND2 = pygame.image.load(os.path.join('png', 'green.png'))
FRIEND3 = pygame.image.load(os.path.join('png', 'blue.png'))
FRIEND4 = pygame.image.load(os.path.join('png', 'yellow.png'))

#muzyka
PAIN = pygame.mixer.Sound('pain.wav')