import pygame
import constants


class Paddle(pygame.sprite.Sprite):
    def __init__(self, side, player):
        pygame.sprite.Sprite.__init__(self)
        self.side = side
        self.player = player
        self.pad_left = (
            0
            if self.side == constants.LEFT_SIDE_PAD
            else (constants.SCREEN_WIDTH - constants.BALL_WIDTH)
        )
        self.pad_rect = pygame.Rect(
            self.pad_left,
            constants.SCREEN_HEIGHT / 2
            - constants.PAD_HEIGHT
            / 2,  # to make sure starting postion of both pads are at the middle
            constants.PAD_WIDTH,
            constants.PAD_HEIGHT,
        )

    def draw(self, screen):
        pygame.draw.rect(screen, constants.WHITE, self.pad_rect)

    def move(self):
        pass

    def __str__(self) -> str:
        return f"Player name {self.player} left side {self.pad_left} side {self.side} pad rect {self.pad_rect}"
