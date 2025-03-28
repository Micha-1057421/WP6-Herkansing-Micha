class Bumper:
    def __init__(self, mqtt_client, bumper_id="bumper1", score_value=100):
        self.bumper_id = bumper_id
        self.score_value = score_value
        self.mqtt_client = mqtt_client

    def hit(self, player_id="Player1"):
        message = f"{player_id}:{self.bumper_id}:{self.score_value}"
        self.mqtt_client.publish("score_update", message)
        print(f"Bumper '{self.bumper_id}' hit by {player_id}! Score +{self.score_value}")