import pygame, random, os
from gameUtils import loadImage, loadSoundFile

# -------------------------------------------
#     Global constants and objects
# -------------------------------------------
FRAMERATE = 120

WIDTH = 1000
HEIGHT = 540
SCREEN_SIZE = (WIDTH, HEIGHT)

ENEMY_TICKS = [25,30,50,75,100,150]
ENEMY_X_POS = [WIDTH/5, WIDTH/6, WIDTH/7, 4*WIDTH/5, 5*WIDTH/6, 6*WIDTH/7]
ENEMY_Y_POS = [HEIGHT/2, 6*HEIGHT/7]

TEXT_COLOR = (10,10,10)

BG_MUSIC = os.path.join("data","bgmusic.wav")

HERO = pygame.sprite.RenderClear()
FIREBALLS = pygame.sprite.RenderClear()
ENEMIES = pygame.sprite.RenderClear()
BLOCKS = pygame.sprite.RenderClear()


# -------------------------------------------
#         Mario-related constants
# -------------------------------------------
if FRAMERATE == 60:
	MARIO_X_ACC = 0.5
	MARIO_FRICTION = 0.92
	MARIO_JUMP_VEL = -10.75
	MARIO_GRAVITY = 0.4
else:
	MARIO_X_ACC = 0.25
	MARIO_FRICTION = 0.93
	MARIO_JUMP_VEL = -8
	MARIO_GRAVITY = 0.2
    
MARIO_MAX_FIREBALLS = 7


# -------------------------------------------
#       Fireball-related constants
# -------------------------------------------

### Old red/blue fireball stats
'''if FRAMERATE == 60:
	FIREBALL_GRAV = 0.5
	RED_Y_VEL = -6.5
	RED_X_VELS = [(x / 4.0) for x in range (12,21)]
	BLUE_Y_VEL = RED_Y_VEL * 1.8
	BLUE_X_VELS = [(x * 0.65) for x in RED_X_VELS]
else:
	FIREBALL_GRAV = 0.25
	RED_Y_VEL = -5
	RED_X_VELS = [((x / 4.0) / 2) for x in range (12,21)]
	BLUE_Y_VEL = RED_Y_VEL * 1.6
	BLUE_X_VELS = [(x * 0.9) for x in RED_X_VELS]'''

if FRAMERATE == 60:
    ###For red fireballs, they now shoot straight across.
    FIREBALL_GRAV = 0
    ###Blue fireballs now have their own gravity, the red fireballs old one (Blue fireballs now bounce like red ones)
    BLUE_FIREBALL_GRAV = 0.5
    RED_Y_VEL = 0
    ###All red fireballs now move at the same speed. 3 wasn't too slow nor too fast.
    RED_X_VELS = [3,3,3,3,3,3,3,3,3]
    BLUE_Y_VEL = -6.5
    BLUE_X_VELS = [(x / 4.0) for x in range (12,21)]
else:
    ###For red fireballs, they now shoot straight across.
    FIREBALL_GRAV = 0
    ###Blue fireballs now have their own gravity, the red fireballs old one (Blue fireballs now bounce like red ones)
    BLUE_FIREBALL_GRAV = 0.25
    RED_Y_VEL = 0
    ###All red fireballs now move at the same speed. 3 wasn't too slow nor too fast.
    RED_X_VELS = [3,3,3,3,3,3,3,3,3]
    BLUE_Y_VEL = -5
    BLUE_X_VELS = [(x / 4.0) for x in range (12,21)]


# -------------------------------------------
#       Shell-related constants
# -------------------------------------------

###Changed the shell's gravity, x_vel and y_vel to mimic the old blue fireball's stats.
if FRAMERATE == 60:
	SHELL_GRAVITY = 0.5
	SHELL_X_VEL = random.choice([(x * 0.65) for x in [(x / 4.0) for x in range(12,21)]])
	SHELL_Y_VEL = -11.7 #-6.5 * 1.8
else:
	SHELL_GRAVITY = 0.25
	SHELL_X_VEL = random.choice([(x * 0.9) for x in [((x / 4.0) / 2) for x in range (12,21)]])
	SHELL_Y_VEL = -8 #-5 * 1.6