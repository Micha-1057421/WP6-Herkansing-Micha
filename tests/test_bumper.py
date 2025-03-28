from game.bumper import Bumper

class DummyMQTT:
    def __init__(self):
        self.last_message = None
    def publish(self, topic_key, message):
        self.last_message = (topic_key, message)

def test_bumper_hit():
    mqtt = DummyMQTT()
    bumper = Bumper(mqtt_client=mqtt, bumper_id="B99", score_value=200)

    bumper.hit("PlayerX")

    assert mqtt.last_message[0] == "score_update"
    assert mqtt.last_message[1] == "PlayerX:B99:200"