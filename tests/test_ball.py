import math
import pytest
from game.ball import Ball

def test_ball_initial_position():
    ball = Ball(x=50, y=100, speed=10, angle=0)
    assert ball.get_position() == (50, 100)

def test_ball_movement():
    ball = Ball(x=0, y=0, speed=10, angle=0)  # rechte lijn naar rechts
    ball.move()
    x, y = ball.get_position()
    assert x > 0
    assert y == 0  # geen verticale beweging bij 0 graden

def test_ball_reflect_vertical():
    ball = Ball(x=0, y=0, speed=10, angle=0)
    original_angle = ball.angle
    ball.reflect_vertical()
    assert math.isclose(ball.angle, math.pi - original_angle)

def test_ball_reflect_horizontal():
    ball = Ball(x=0, y=0, speed=10, angle=0.5)
    original_angle = ball.angle
    ball.reflect_horizontal()
    assert math.isclose(ball.angle, -original_angle)