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
        # to make sure starting position of both pads are at the middle
        self.top = constants.SCREEN_HEIGHT / 2 - constants.PAD_HEIGHT / 2
        self.pad_rect = pygame.Rect(
            self.pad_left,
            self.top,
            constants.PAD_WIDTH,
            constants.PAD_HEIGHT,
        )

    def update(self, screen):
        self.pad_rect = pygame.Rect(
            self.pad_left,
            self.top,
            constants.PAD_WIDTH,
            constants.PAD_HEIGHT,
        )
        self.pad_rect.clamp_ip(screen.get_rect())
        pygame.draw.rect(screen, constants.WHITE, self.pad_rect)

    def move_up(self):
        self.top = self.top - constants.PAD_MOVE_INCREMENTS

    def move_down(self):
        self.top = self.top + constants.PAD_MOVE_INCREMENTS

    def __str__(self) -> str:
        return f"Player name {self.player} left side {self.pad_left} side {self.side} pad rect {self.pad_rect}"
