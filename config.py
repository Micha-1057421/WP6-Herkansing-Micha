MQTT_BROKER = "67c8ddfe101345209bc424d813259344.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = 'Flipperkast'
MQTT_PASSWORD = "Flipperkast123!"
MQTT_KEEPALIVE = 60
USE_TLS = True

TOPICS = {
    "score_update": "flipperkast/score/update",
    "ball_move": "flipperkast/ball/move",
    "flipper_state": "flipperkast/flipper/state",
    "highscore": "flipperkast/highscore"
}