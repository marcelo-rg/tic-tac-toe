import numpy as np
import pygame
from pygame.sprite import Sprite
from typing import List

from game_objects import Grid, Icon, PlayerTurnDisplay
import config

CELL_WIDTH = config.SCREEN_HEIGHT //3

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_HEIGHT, config.SCREEN_WITH))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
running = True

# Create game objects
global player
player = "Player1"
game_matrix = np.zeros((3,3), dtype=np.int32)
grid = Grid()
cell_centers = grid.calculate_cell_centers()
print(cell_centers)
font = pygame.font.Font(None, 36)
player_turn_displays = PlayerTurnDisplay((400,0), font=font)


def get_grid_position(pos, cell_width):
    col, row = pygame.math.Vector2(pos) // cell_width
    return int(row), int(col)

def play_turn(current_player):
    global player

    # Define player mapping
    player_mapping = {
        "Player1": {"value": 1, "next": "Player2"},
        "Player2": {"value": 2, "next": "Player1"},
    }

    # Get the current mouse position and map to grid indices
    current_pos = pygame.mouse.get_pos()
    row, col = get_grid_position(current_pos, CELL_WIDTH)

    # Check if the selected cell is empty
    if game_matrix[row, col] == 0:
        # Update the game matrix and switch players
        game_matrix[row, col] = player_mapping[current_player]["value"]
        player = player_mapping[current_player]["next"]

def load_icons() -> List[Icon]:
    icons = []
    for i in range(3):  # Iterate over rows
        for j in range(3):  # Iterate over columns
            if game_matrix[i][j] == 1:
                icons.append(Icon(current_player="Player1", position= cell_centers[i][j]))
            elif game_matrix[i][j] == 2:
                icons.append(Icon(current_player="Player2", position= cell_centers[i][j]))
    return icons

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            play_turn(player)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("beige")

    player_turn_displays.update(player)
    icons = load_icons()

    grid.draw(screen)
    for icon in icons:
        icon.draw(screen)
    player_turn_displays.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()