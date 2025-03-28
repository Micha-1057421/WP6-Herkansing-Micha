from config import TOPICS

class ScorePanel:
    def __init__(self):
        self.scores = {}
        self.highscore = 0
        self.highscore_player = None

    def handle_score_update(self, message):
        try:
            player_id, bumper_id, value = message.split(":")
            value = int(value)
        except ValueError:
            print(f"⚠️ Ongeldig scorebericht: {message}")
            return

        if player_id not in self.scores:
            self.scores[player_id] = 0

        self.scores[player_id] += value

        print(f"📈 {player_id} +{value} (via {bumper_id}) → Total: {self.scores[player_id]}")

        if self.scores[player_id] > self.highscore:
            self.highscore = self.scores[player_id]
            self.highscore_player = player_id
            print(f"🏆 Nieuwe highscore: {self.highscore} door {self.highscore_player}")