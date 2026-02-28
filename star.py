# star.py
import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, ai_game):
        """Initialize the star and set its random position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/star.png').convert_alpha()  # Make sure this file exists
        self.image = pygame.transform.scale(self.image, (20, 20))  
        self.rect = self.image.get_rect()

        # Start each star near the top left of the screen, adjusted later
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position
        self.x = float(self.rect.x)

    def update_position(self, x, y):
        """Set the star's position with optional randomness."""
        self.rect.x = x + randint(-80, 80)
        self.rect.y = y + randint(-80, 80)
