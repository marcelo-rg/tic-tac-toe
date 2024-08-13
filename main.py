import pygame
from pygame.sprite import Sprite
from typing import List

from game_objects import Grid, Icon, PlayerTurnDisplay
import config

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_HEIGHT, config.SCREEN_WITH))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
running = True

# Create game objects
grid = Grid()
font = pygame.font.Font(None, 36)
player_turn_displays = PlayerTurnDisplay(position=(100,0), font=font)


def load_icons(icons : List[Sprite]):
    # for icon in icons
    pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("beige")

    grid.update(None)
    grid.draw(screen)
    player_turn_displays.update("Player1")
    player_turn_displays.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()