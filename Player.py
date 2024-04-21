class Player:
    def __init__(self, name, side) -> None:
        self.name = name
        self.side = side
        self.score = 0
        self.won_current_game = False
        self.games_won = 0

    def score(self):
        return self.score

    def score_update(self):
        self.score += 1

    def name(self):
        return self.name
