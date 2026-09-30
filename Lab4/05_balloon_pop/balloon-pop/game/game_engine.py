
"""
GameEngine: manages balloons, spawning, scoring, lives, and clicks.
"""

import random

from game.balloon import Balloon
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT, draw_banner

SPAWN_INTERVAL_FRAMES = 45

BALLOON_SCORES = {
    "normal": 10,
    "bonus": 20,
    "penalty": -10,
}


class GameEngine:
    def __init__(self):
        self.balloons = []
        self.frames_until_spawn = 0
        self.score = 0

        # Lives system
        self.lives = 3
        self.game_over = False

    def _spawn_balloon(self):
        if self.game_over:
            return

        radius = random.randint(16, 44)
        x = random.randint(radius + 10, WIDTH - radius - 10)
        speed = random.uniform(1.5, 3.0)

        balloon_type = random.choices(
            population=["normal", "bonus", "penalty"],
            weights=[0.6, 0.2, 0.2],
            k=1,
        )[0]

        self.balloons.append(
            Balloon(
                x=x,
                y=-radius,
                radius=radius,
                speed=speed,
                balloon_type=balloon_type,
            )
        )

    def handle_click(self, pos):
        # Ignore clicks after game over.
        if self.game_over:
            return

        popped = check_pop(self.balloons, pos)

        if popped is not None:
            self.balloons.remove(popped)
            self.score += BALLOON_SCORES[popped.balloon_type]

    def update(self):
        # Freeze gameplay after all lives are lost.
        if self.game_over:
            return

        self.frames_until_spawn -= 1

        if self.frames_until_spawn <= 0:
            self._spawn_balloon()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        for balloon in self.balloons:
            balloon.update()

        # Count every missed balloon exactly once by removing it.
        remaining_balloons = []

        for balloon in self.balloons:
            if balloon.is_past_bottom(HEIGHT):
                self.lives -= 1
            else:
                remaining_balloons.append(balloon)

        self.balloons = remaining_balloons

        # End the round when no lives remain.
        if self.lives <= 0:
            self.lives = 0
            self.game_over = True
            self.balloons.clear()

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(surface, self.balloons)

        renderer.draw_text(
            surface, font, f"Score: {self.score}", (10, 10)
        )

        renderer.draw_text(
            surface, font, f"Lives: {self.lives}", (10, 40)
        )

        if self.game_over:
            draw_banner(
                surface,
                font,
                f"GAME OVER! Final Score: {self.score}",
            )
