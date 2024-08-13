import numpy as np
import pygame
from pygame.sprite import Sprite
from pygame.image import load
from config import player_config
from typing import List

class Grid(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = load('assets/images/grid.png').convert_alpha()
        self.rect = self.image.get_rect()
        # screen = pygame.display.get_surface()
        # self.area = screen.get_rect()
        self.center_sprite()
        self.game_matrix = np.zeros((3,3), dtype=np.integer)

    def center_sprite(self):
        # Center the sprite on the screen
        screen_rect = pygame.display.get_surface().get_rect()
        self.rect.center = screen_rect.center

    def update(self, position : int) -> None:
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the grid image to the screen

    def calculate_cell_centers(self) -> List[tuple]:
        # Calculate the centers of the 9 grid cells
        cell_width = self.rect.width // 3
        cell_height = self.rect.height // 3

        cell_centers = []
        for row in range(3):
            for col in range(3):
                center_x = self.rect.left + (col * cell_width) + (cell_width // 2)
                center_y = self.rect.top + (row * cell_height) + (cell_height // 2)
                cell_centers.append((center_x, center_y))

        return cell_centers


class Icon(Sprite):
    def __init__(self) -> None:
        super().__init__()


class PlayerTurnDisplay:
    def __init__(self, position, font):
        self.font = font
        self.position = position
        self.text = ""
        self.color = (0,0,0)

    def update(self, current_player : str):
        self.text = f"{current_player}'s Turn"
        self.color = player_config["color"][current_player]

    def draw(self, screen):
        rendered_text = self.font.render(self.text, True, self.color)
        screen.blit(rendered_text, self.position)
