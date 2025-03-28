import math

class Ball:
    def __init__(self, x=100, y=100, speed=5, angle=45):
        self.x = x
        self.y = y
        self.speed = speed  # pixels per tick
        self.angle = math.radians(angle)  # richting in radialen

    def move(self):
        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)
        self.x += dx
        self.y += dy
        print(f"Ball moved to ({int(self.x)}, {int(self.y)})")

    def reflect_horizontal(self):
        self.angle = -self.angle
        print("Ball reflected horizontally")

    def reflect_vertical(self):
        self.angle = math.pi - self.angle
        print("Ball reflected vertically")

    def get_position(self):
        return int(self.x), int(self.y)