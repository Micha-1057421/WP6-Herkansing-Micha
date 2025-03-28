import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_PASSWORD, MQTT_USERNAME, MQTT_KEEPALIVE, TOPICS, USE_TLS

class MQTTClient:
    def __init__(self, client_id="flipperkast-client"):
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        if USE_TLS:
            self.client.tls_set()
        if MQTT_USERNAME and MQTT_PASSWORD:
            self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    def set_score_handler(self, handler_function):
        self.score_handler = handler_function
        
    def connect(self):
        print(f"Connecting to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}...")
        self.client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("✅ Connected to MQTT Broker!")
            for topic in TOPICS.values():
                client.subscribe(topic)
                print(f"🔔 Subscribed to: {topic}")
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
            message = msg.payload.decode()
            print(f"[MQTT] Message received on topic '{msg.topic}': {message}")

            if msg.topic == TOPICS["score_update"] and hasattr(self, "score_handler"):
                self.score_handler(message)

    def publish(self, topic_key, message):
        topic = TOPICS.get(topic_key)
        if topic:
            self.client.publish(topic, message)
            print(f"[MQTT] Published '{message}' to topic '{topic}'")
        else:
            print(f"[MQTT] Invalid topic key: {topic_key}")
 
