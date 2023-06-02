class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        filename = 'score.txt'
        with open(filename) as file_object:
            for score in file_object:
                self.highestscore = int(score)
        self.high_score = self.highestscore

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
