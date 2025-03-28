import pygame
from game.ball import Ball
from game.flipper import Flipper
import math
from game.bumper import Bumper
from mqtt.mqtt_client import MQTTClient
from game.score_panel import ScorePanel

WIDTH = 400
HEIGHT = 600
FPS = 60

BALL_RADIUS = 10

class GameDisplay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flipperkast Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.mqtt_client = MQTTClient()
        self.mqtt_client.connect()
        
        #maak de bumpers aan
        self.bumpers = [
            {"x": 120, "y": 150, "radius": 20, "obj": Bumper(self.mqtt_client, bumper_id="B1", score_value=100)},
            {"x": 280, "y": 200, "radius": 20, "obj": Bumper(self.mqtt_client, bumper_id="B2", score_value=150)},
        ]

        # Maak de bal
        self.ball = Ball(x=200, y=300, speed=5, angle=45)

        # Flippers maken
        self.left_flipper = Flipper(None, side="left")
        self.right_flipper = Flipper(None, side="right")

        #maak de scoreboard aan
        self.score_panel = ScorePanel()
        self.mqtt_client.set_score_handler(self.score_panel.handle_score_update)

        self.font = pygame.font.SysFont("Arial", 20)

    def draw_playfield(self):
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, (80, 80, 80), (10, 10, WIDTH - 20, HEIGHT - 20), 2)

    def draw_ball(self):
        x, y = self.ball.get_position()
        pygame.draw.circle(self.screen, (255, 255, 255), (x, y), BALL_RADIUS)

    def update_ball(self):
        self.ball.move()
        x, y = self.ball.get_position()

        # wall collision
        if x <= 10 + BALL_RADIUS or x >= WIDTH - 10 - BALL_RADIUS:
            self.ball.reflect_vertical()
        if y <= 10 + BALL_RADIUS or y >= HEIGHT - 10 - BALL_RADIUS:
            self.ball.reflect_horizontal()

    def draw_flippers(self):
        # Linker flipper
        base_left = (100, HEIGHT - 40)
        if self.left_flipper.active:
            end_left = (80, HEIGHT - 80)
        else:
            end_left = (60, HEIGHT - 40)
        pygame.draw.line(self.screen, (255, 0, 0), base_left, end_left, 8)

        # Rechter flipper
        base_right = (WIDTH - 100, HEIGHT - 40)
        if self.right_flipper.active:
            end_right = (WIDTH - 80, HEIGHT - 80)
        else:
            end_right = (WIDTH - 60, HEIGHT - 40)
        pygame.draw.line(self.screen, (0, 0, 255), base_right, end_right, 8)
    
    def check_flipper_collision(self):
        x, y = self.ball.get_position()

        # Check linkerflipper
        if self.left_flipper.active:
            if 80 < x < 120 and HEIGHT - 60 < y < HEIGHT - 30:
                print("Collision with LEFT flipper!")
                self.ball.reflect_horizontal()

        # Check rechterflipper
        if self.right_flipper.active:
            if WIDTH - 120 < x < WIDTH - 80 and HEIGHT - 60 < y < HEIGHT - 30:
                print("Collision with RIGHT flipper!")
                self.ball.reflect_horizontal()
    
    def draw_bumpers(self):
        for bumper in self.bumpers:
            pygame.draw.circle(self.screen, (0, 255, 0), (bumper['x'], bumper['y']), bumper['radius'])

    def check_bumper_collision(self):
        bx, by = self.ball.get_position()
        for bumper in self.bumpers:
            dx = bx - bumper['x']
            dy = by - bumper['y']
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < bumper['radius'] + 10: 
                print(f"Ball hit bumper {bumper['obj'].bumper_id}")
                bumper["obj"].hit("Player1")
                self.ball.reflect_horizontal() 

    def draw_score_panel(self):
        y_offset = 10
        for player, score in self.score_panel.scores.items():
            score_text = f"{player}: {score}"
            text_surface = self.font.render(score_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (20, y_offset))
            y_offset += 25

        if self.score_panel.highscore_player:
            hs_text = f"Highscore: {self.score_panel.highscore_player} ({self.score_panel.highscore})"
            hs_surface = self.font.render(hs_text, True, (255, 215, 0)) 
            self.screen.blit(hs_surface, (WIDTH // 2 - 50, 10))

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.left_flipper.activate()
            else:
                self.left_flipper.deactivate()

            if keys[pygame.K_l]:
                self.right_flipper.activate()
            else:
                self.right_flipper.deactivate()

            self.update_ball()
            self.check_flipper_collision()
            self.check_bumper_collision()

            self.draw_playfield()
            self.draw_ball()
            self.draw_flippers()
            self.draw_bumpers()
            self.draw_score_panel()

            pygame.display.flip()

        pygame.quit()