import pygame
import constants
from Ball import Ball


def play_pong():
    still_playing = True

    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
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
        screen.fill(color=constants.BLACK)
        # draw a line in the middle of the screen
        for ht in range(0, 600, 41):
            dashed_line_dot = pygame.Rect(505, ht, 10, 20)
            pygame.draw.rect(screen, constants.DASHED_LINE_COLOR, dashed_line_dot)
        pong_ball.move(screen)
        pygame.display.flip()
        if pong_ball.check_position():
            new_ball = True
            del pong_ball
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    play_pong()
