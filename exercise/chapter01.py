from pyray import Vector, Point


class Projectile:
    """Projectile"""

    def __init__(self, postiion: Point, velocity: Vector) -> None:
        self.position = postiion
        self.velocity = velocity


class Environment:
    """Environment"""

    def __init__(self, gravity: Vector, wind: Vector) -> None:
        self.gravity = gravity
        self.wind = wind


def tick(env: Environment, proj: Projectile) -> Projectile:
    """Move projectile"""
    postision = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity
    return Projectile(postision, velocity)


p = Projectile(Point(0, 1, 0), Vector(1, 1, 0).normalized())
e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

counter = 0
while p.position.y > 0:
    print(f'Tick: {counter} Position: {p.position.y}')
    p = tick(e, p)
    counter = counter + 1
