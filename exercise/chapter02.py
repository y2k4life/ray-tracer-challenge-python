from pyray import Vector, Point
from pyray import Color, Canvas


class Projectile:
    """Projectile"""

    def __init__(self, position: Point, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity


class Environment:
    """Environment"""

    def __init__(self, gravity: Vector, wind: Vector) -> None:
        self.gravity = gravity
        self.wind = wind


def tick(env: Environment, proj: Projectile) -> Projectile:
    """Move projectile"""
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


p = Projectile(Point(0, 1, 0), Vector(1, 1.8, 0).normalize() * 11.25)
e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))
width = 900
height = 500
c = Canvas(width, height)

counter = 0
while p.position.y > 0:
    p = tick(e, p)

    x = int(p.position.x)
    y = int(height - p.position.y)

    if (x <= width - 1) & (y <= height - 1):
        c.canvas[x][y] = Color(1.0, 0.0, 0.0)

ppm = c.convert_to_ppm()
f = open('chapter2.ppm', 'wt', encoding='utf-8')
f.write(ppm)
