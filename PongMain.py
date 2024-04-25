import pygame
import constants
from Ball import Ball
from Paddle import Paddle
from Player import Player


def create_update_score(left_player_score, right_player_score):
    font = pygame.font.SysFont("Arial", 46)
    left_side_text = font.render(
        str(left_player_score),
        True,
        constants.SCORE_TEXT_COLOR,
        constants.BLACK,
    )
    right_side_text = font.render(
        str(right_player_score),
        True,
        constants.SCORE_TEXT_COLOR,
        constants.BLACK,
    )
    left_side_text_rect = left_side_text.get_rect()
    left_side_text_rect.top = 50
    left_side_text_rect.left = constants.SCREEN_WIDTH / 2 - 60
    right_side_text_rect = right_side_text.get_rect()
    right_side_text_rect.top = 50
    right_side_text_rect.left = constants.SCREEN_WIDTH / 2 + 40
    return {
        "left": (left_side_text, left_side_text_rect),
        "right": (right_side_text, right_side_text_rect),
    }


def game_prompt(message):
    font = pygame.font.SysFont("Times New Roman", 48)
    text = font.render(message, True, constants.SCORE_TEXT_COLOR, constants.BLACK)
    text_rect = text.get_rect()
    text_rect.top = constants.SCREEN_HEIGHT / 2
    text_rect.left = constants.SCREEN_WIDTH / 2 - text_rect.width / 2
    return (text, text_rect)


def play_pong():
    still_playing = True

    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    new_ball = True
    pong_ball = None
    new_game = True
    prompt_before_game_start = True
    player_won = False
    pause = False
    play_on = False

    pad1 = Paddle(constants.LEFT_SIDE_PAD, "player1")
    player_on_left = Player("player1-left", constants.LEFT_SIDE_PAD)
    pad2 = Paddle(constants.RIGHT_SIDE_PAD, "player2")
    player_on_right = Player("player2-right", constants.RIGHT_SIDE_PAD)

    while still_playing:
        screen.fill(color=constants.BLACK)
        # draw a line in the middle of the screen
        for ht in range(0, constants.SCREEN_HEIGHT, 41):
            dashed_line_dot = pygame.Rect(constants.SCREEN_WIDTH / 2, ht, 10, 20)
            pygame.draw.rect(screen, constants.DASHED_LINE_COLOR, dashed_line_dot)
        scores_list = create_update_score(player_on_left.score, player_on_right.score)
        screen.blit(scores_list["left"][0], scores_list["left"][1])
        screen.blit(scores_list["right"][0], scores_list["right"][1])
        if prompt_before_game_start:
            start_game_message = "Press Enter to Start the Game - Esq to Quit"
            initial_prompt = game_prompt(start_game_message)
            screen.blit(initial_prompt[0], initial_prompt[1])
        if play_on:
            if new_ball:
                pong_ball = Ball(screen)
                new_ball = False
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_UP]:
                pad2.move_up()
            if keypressed[pygame.K_DOWN]:
                pad2.move_down()

            if keypressed[pygame.K_w]:
                pad1.move_up()
            if keypressed[pygame.K_s]:
                pad1.move_down()
            pad1.update(screen)
            pad2.update(screen)
            pong_ball.move(screen)
            if pong_ball.check_position(
                left_pad=pad1,
                right_pad=pad2,
                left_side_score_update=player_on_left.score_update,
                right_side_score_update=player_on_right.score_update,
            ):
                new_ball = True
                del pong_ball
            if player_on_right.score == 3:
                player_won = True
                win_message = (
                    f"{player_on_right.name} Wins - Enter to Replay Esq to Quit"
                )
                player_on_right.games_won += 1
                play_on = False
            elif player_on_left.score == 3:
                player_won = True
                win_message = (
                    f"{player_on_left.name} Wins - Enter to Replay Esq to Quit"
                )
                player_on_left.games_won += 1
                play_on = False
        if player_won:
            win_prompt = game_prompt(win_message)
            screen.blit(win_prompt[0], win_prompt[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                still_playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if prompt_before_game_start:
                        prompt_before_game_start = False
                        play_on = True
                    if player_won:
                        new_game = True
                        player_on_left.reset()
                        player_on_right.reset()
                        prompt_before_game_start = True
                        player_won = False
                        play_on = False
                if event.key == pygame.K_ESCAPE:
                    if prompt_before_game_start or player_won:
                        still_playing = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    play_pong()
