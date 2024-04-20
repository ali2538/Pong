import random
import pygame
import math

import constants


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, x=510, y=20) -> None:
        pygame.sprite.Sprite.__init__(self)
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
        self.speed = 3
        self.angle_in_degrees = random.choice(
            [
                ang
                for ang in range(20, 340, 5)
                if ang not in constants.INITIAL_ANGLES_TO_AVOID
            ]
        )
        self.angle_in_radian = math.pi * self.angle_in_degrees / 180

    def __del__(self):
        print("Object removed")

    def update_angle(self):
        self.angle_in_radian = math.pi * self.angle_in_degrees / 180

    # def new_xy_cord(self):
    #     self.position_x = self.position_x + math.cos(self.angle_in_radian) * self.speed
    #     self.position_y = self.position_y + math.sin(self.angle_in_radian) * self.speed

    def check_position(self) -> bool:
        if not self.screen_area.contains(self.pong_ball):
            print(f"Stop 1: 111111111 {self.pong_ball}")
            if (self.pong_ball.top < 5.0 or self.pong_ball.bottom > 590.0) and (
                (not self.pong_ball.left < 10.0) and (not self.pong_ball.right > 1000.0)
            ):
                print(
                    f"Stop 2: 2222222222222 pong left {self.pong_ball.left} and right {self.pong_ball.right}"
                )
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
                print(
                    f"Stop 3: 3333333333333333 pong left {self.pong_ball.left} pong right {self.pong_ball.right}"
                )
                return True
            if (self.pong_ball.top < 5.0 or self.pong_ball.bottom > 590.0) and (
                (self.pong_ball.left < 5.0) or (self.pong_ball.right > 1010.0)
            ):
                print(
                    f"Stop 4: 444444444444444444444 pong left {self.pong_ball.left} pong right {self.pong_ball.right}"
                )
                return True

    def move(self, screen):
        self.position_x = self.position_x + math.cos(self.angle_in_radian) * self.speed
        self.position_y = self.position_y + math.sin(self.angle_in_radian) * self.speed
        self.pong_ball = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        pygame.draw.rect(screen, constants.WHITE, self.pong_ball)
