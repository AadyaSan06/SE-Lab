import random
import pygame

from game.balloon import Balloon
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT, draw_banner

SPAWN_INTERVAL_FRAMES = 45
ROUND_DURATION = 30

BALLOON_SCORES = {
    "normal": 10,
    "bonus": 20,
    "penalty": -10,
}


class GameEngine:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.balloons = []
        self.frames_until_spawn = 0
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.start_ticks = pygame.time.get_ticks()
        self.time_left = ROUND_DURATION

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
        if self.game_over:
            return

        popped = check_pop(self.balloons, pos)

        if popped is not None:
            self.balloons.remove(popped)
            self.score += BALLOON_SCORES[popped.balloon_type]

    def update(self):
        if self.game_over:
            return

        elapsed = (
            pygame.time.get_ticks() - self.start_ticks
        ) / 1000

        self.time_left = max(0, ROUND_DURATION - int(elapsed))

        if self.time_left <= 0:
            self.game_over = True
            self.balloons.clear()
            return

        self.frames_until_spawn -= 1

        if self.frames_until_spawn <= 0:
            self._spawn_balloon()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        remaining_balloons = []

        for balloon in self.balloons:
            balloon.update()

            if balloon.is_past_bottom(HEIGHT):
                self.lives -= 1
            else:
                remaining_balloons.append(balloon)

        self.balloons = remaining_balloons

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
        renderer.draw_text(
            surface, font, f"Time: {self.time_left}s", (10, 70)
        )

        if self.game_over:
            draw_banner(
                surface,
                font,
                f"GAME OVER! Score: {self.score} - Press R to restart",
            )
