
"""
Balloon: falls from the top of the screen.
Each balloon has a type, colour, and scoring value.
"""

import pygame


class Balloon:
    def __init__(
        self,
        x,
        y,
        radius,
        speed,
        balloon_type="normal",
        color=None,
    ):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.balloon_type = balloon_type

        # Each balloon type has a distinct colour.
        colors = {
            "normal": (220, 90, 120),    # Pink
            "bonus": (255, 200, 40),     # Yellow
            "penalty": (100, 100, 240),  # Blue
        }

        self.color = color if color is not None else colors[balloon_type]

    def update(self):
        self.y += self.speed

    def is_past_bottom(self, height):
        return self.y - self.radius > height

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2,
        )
