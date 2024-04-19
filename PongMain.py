import pygame

from Ball import Ball


def play_pong():
    still_playing = True
    SCREEN_WIDTH = 1020
    SCREEN_HEIGHT = 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DASHED_LINE_COLOR = (204, 204, 204)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    new_ball = True
    pong_ball = None
    while still_playing:
        if new_ball:
            pong_ball = Ball(screen)
            new_ball = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                still_playing = False
        screen.fill(color=BLACK)
        # draw a line in the middle of the screen
        for ht in range(0, 600, 41):
            dashed_line_dot = pygame.Rect(500, ht, 20, 20)
            pygame.draw.rect(screen, DASHED_LINE_COLOR, dashed_line_dot)
        pong_ball.move(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    play_pong()
