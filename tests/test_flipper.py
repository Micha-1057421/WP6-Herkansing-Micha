from game.flipper import Flipper

class DummyMQTT:
    def __init__(self):
        self.last_message = None
    def publish(self, topic_key, message):
        self.last_message = (topic_key, message)

def test_flipper_activation():
    mqtt = DummyMQTT()
    flipper = Flipper(mqtt_client=mqtt, side="left")

    flipper.activate()
    assert flipper.active is True
    assert mqtt.last_message == ("flipper_state", "left:active")

    flipper.deactivate()
    assert flipper.active is False
    assert mqtt.last_message == ("flipper_state", "left:idle")
