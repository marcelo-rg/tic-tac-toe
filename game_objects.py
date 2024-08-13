import pygame
from pygame.sprite import Sprite
from pygame.image import load
from config import player_config
from typing import List
import config

class Grid(Sprite):
    def __init__(self) -> None:
        super().__init__()
        image = load('assets/images/grid.png')
        self.image = pygame.transform.scale(image, (config.SCREEN_HEIGHT, config.SCREEN_WITH))
        self.rect = self.image.get_rect()
        self.center_sprite()

    def center_sprite(self):
        # Center the sprite on the screen
        screen_rect = pygame.display.get_surface().get_rect()
        self.rect.center = screen_rect.center

    def update(self, position : int) -> None:
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the grid image to the screen

    def calculate_cell_centers(self) -> List[List[tuple[int, int]]]:
        # Calculate the width and height of each cell
        cell_width = self.rect.width // 3
        cell_height = self.rect.height // 3

        # Initialize an empty 3x3 matrix to store cell centers
        cell_centers = []

        for row in range(3):
            row_centers = []  # To store the centers of each cell in the current row
            for col in range(3):
                center_x = self.rect.left + (col * cell_width) + (cell_width // 2)
                center_y = self.rect.top + (row * cell_height) + (cell_height // 2)
                row_centers.append((center_x, center_y))
            cell_centers.append(row_centers)  # Add the current row to the matrix

        return cell_centers


class Icon(Sprite):
    def __init__(self, current_player : str, position : tuple) -> None:
        super().__init__()
        self.current_player = current_player
        image = load(player_config["icon_path"][self.current_player])
        self.image = pygame.transform.scale(image, (config.SCREEN_HEIGHT//3 -5, config.SCREEN_WITH//3 -15))
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)


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
