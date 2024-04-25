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

    def update_angle(self):
        self.angle_in_radian = math.pi * self.angle_in_degrees / 180

    def increase_speed(self, new_speed=0.1):
        self.speed += new_speed

    def check_position(
        self, left_pad, right_pad, left_side_score_update, right_side_score_update
    ) -> bool:
        if self.pong_ball.colliderect(left_pad.pad_rect) or self.pong_ball.colliderect(
            right_pad.pad_rect
        ):
            self.angle_in_degrees -= 90
            self.update_angle()
            self.increase_speed()
        if not self.screen_area.contains(self.pong_ball):
            if (
                self.pong_ball.top < 2
                or self.pong_ball.bottom > constants.SCREEN_HEIGHT - 2
            ) and (
                (not self.pong_ball.left < 10)
                and (not self.pong_ball.right > constants.SCREEN_WIDTH - 10)
            ):
                self.angle_in_degrees = -self.angle_in_degrees
                self.update_angle()
                return False
            if (self.pong_ball.left < 10.0) and self.screen_area.colliderect(
                self.pong_ball
            ):
                right_side_score_update()
                return True
            if (self.pong_ball.right > 1000.0) and self.screen_area.colliderect(
                self.pong_ball
            ):
                left_side_score_update()
                return True
            if self.pong_ball.top < 5.0 or self.pong_ball.bottom > 590.0:
                if self.pong_ball.left < 5.0:
                    right_side_score_update()
                    return True
                if self.pong_ball.right > 1010.0:
                    left_side_score_update()
                    return True

    def move(self, screen):
        self.position_x = self.position_x + math.cos(self.angle_in_radian) * self.speed
        self.position_y = self.position_y + math.sin(self.angle_in_radian) * self.speed
        self.pong_ball = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )
        pygame.draw.rect(screen, constants.WHITE, self.pong_ball)
