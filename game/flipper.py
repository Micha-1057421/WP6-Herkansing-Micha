class Flipper:
    def __init__(self, mqtt_client, side="left"):
        self.side = side  # "left" of "right"
        self.active = False
        self.mqtt_client = mqtt_client

    def activate(self):
        if not self.active:
            self.active = True
            self._publish_state()
            print(f"🕹️ Flipper '{self.side}' ACTIVATED")

    def deactivate(self):
        if self.active:
            self.active = False
            self._publish_state()
            print(f"🕹️ Flipper '{self.side}' released")

    def _publish_state(self):
        if self.mqtt_client:
            message = f"{self.side}:{'active' if self.active else 'idle'}"
            self.mqtt_client.publish("flipper_state", message)