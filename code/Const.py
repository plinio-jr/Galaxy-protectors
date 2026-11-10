import pygame

#C
COLOR_WHITE = (255, 255, 255)
COlOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 5,
    'Level1Bg7': 5,
    'Level1Bg8': 4,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 4,
    'Enemy1': 1,
    'Enemy1Shot':3,
    'Enemy2': 3,
    'Enemy2Shot':4,
    'Enemy3':5,
    'Enemy3Shot':3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level1Bg8': 999,
    'Player1': 500,
    'Player1Shot': 1,
    'Player2': 500,
    'Player2Shot': 1,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy3':150,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot':1,

}

ENTITY_SHOT_DELAY = {
    'Player1': 40,
    'Player2': 35,
    'Enemy1': 50,
    'Enemy2': 55,
    'Enemy3': 45,
}

#M
MENU_OPTION = (
    "NEW GAME 1P - HISTORY",
    "NEW GAME 2P - COOPERATIVE",
    "SCORE",
    "CONFIGURATION",
    "EXIT",
)

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

