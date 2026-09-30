import pygame

from game.game_engine import GameEngine
from game.renderer import WINDOW_SIZE

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Balloon Pop")

font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

engine = GameEngine()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            engine.handle_click(event.pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and engine.game_over:
                engine.reset_game()

    engine.update()
    engine.draw(screen, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
