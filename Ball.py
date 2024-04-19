import random
import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, x=510, y=20) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.WHITE = (255, 255, 255)
        self.width = 20
        self.height = 20
        self.screen_area = screen.get_rect()
        self.starting_y = random.randint(10, 580)
        self.starting_x = 510
        self.new_ball = True
        self.position_y = self.starting_y
        self.position_x = self.starting_x
        self.pong_ball = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        self.speed = 1

        self.initial_angle = math.pi * (random.randint(0, 360)) / 180

    def new_xy_cord(self):
        print(f"current angle is gggggggg {self.initial_angle}")
        self.position_x = self.position_x + math.cos(self.initial_angle) * self.speed
        self.position_y = self.position_y + math.sin(self.initial_angle) * self.speed

    def move(self, screen):
        self.pong_ball = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        pygame.draw.rect(screen, self.WHITE, self.pong_ball)
        self.position_x = self.position_x + math.cos(self.initial_angle) * self.speed
        self.position_y = self.position_y + math.sin(self.initial_angle) * self.speed
        print(f"current angle is gggggggg {self.initial_angle}")
