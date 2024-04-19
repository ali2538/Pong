import random
import pygame
import math

possible_angles_list = [
    10,
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55,
    60,
    110,
    115,
    120,
    130,
    135,
    140,
    145,
    200,
    210,
    215,
    220,
    320,
    330,
    335,
    340,
]


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, x=510, y=20) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.WHITE = (255, 255, 255)
        self.width = 20
        self.height = 20
        self.screen_area = screen.get_rect()
        self.starting_y = random.randint(10.0, 580.0)
        self.starting_x = 510
        self.new_ball = True
        self.position_y = self.starting_y
        self.position_x = self.starting_x
        self.pong_ball = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        self.speed = 2
        self.angle_in_degrees = random.choice(possible_angles_list)
        self.angle_in_radian = math.pi * self.angle_in_degrees / 180

    def __del__(self):
        print("Object removed")

    def update_angle(self):
        self.angle_in_radian = math.pi * self.angle_in_degrees / 180

    def new_xy_cord(self):
        self.position_x = self.position_x + math.cos(self.angle_in_radian) * self.speed
        self.position_y = self.position_y + math.sin(self.angle_in_radian) * self.speed

    def check_position(self) -> bool:
        if not self.screen_area.contains(self.pong_ball):
            if (self.pong_ball.top < 10.0 or self.pong_ball.bottom > 580.0) and (
                (not self.pong_ball.left < 10.0) or (not self.pong_ball.right > 1000.0)
            ):
                self.angle_in_degrees = -self.angle_in_degrees
                self.update_angle()
                return False
            if (
                (self.pong_ball.left < 10.0)
                or (self.pong_ball.right > 1000.0)
                or self.screen_area.collidepoint(
                    self.pong_ball.bottomleft, self.pong_ball.bottomleft
                )
                or self.screen_area.collidepoint(
                    self.pong_ball.topleft, self.pong_ball.topleft
                )
                or self.screen_area.collidepoint(
                    self.pong_ball.bottomright, self.pong_ball.bottomright
                )
                or self.screen_area.collidepoint(
                    self.pong_ball.topright, self.pong_ball.topright
                )
            ):
                return True

    def move(self, screen):
        self.position_x = self.position_x + math.cos(self.angle_in_radian) * self.speed
        self.position_y = self.position_y + math.sin(self.angle_in_radian) * self.speed
        self.pong_ball = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        pygame.draw.rect(screen, self.WHITE, self.pong_ball)
