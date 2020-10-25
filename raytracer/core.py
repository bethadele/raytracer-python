from tracer_tuple import Point, Vector


# A projectile has a position (a point) and a velocity (a vector).
# An environment has gravity (a vector) and wind (a vector).
class Projectile():
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

class Environment():
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind

def tick(env, proj):
    pos = proj.position.plus(proj.velocity)
    vel = proj.velocity.plus(env.gravity).plus(env.wind)

    return Projectile(pos, vel)

p = Projectile(Point(0, 1, 0), Vector(1, 0.5, 0).normalize().times(3))
grav = Vector(0, -0.1, 0.001)
wind = Vector(-0.01, 0, 0)
e = Environment(grav, wind)

print(f'Projectile begins at {p.position.x}, {p.position.y}, {p.position.x}')
print('and then:')
for s in range(500):
    p = tick(e, p)
    if p.position.y <= 0:
       print('--------------------------')
       print(f'Landed at x = {p.position.x}, z = {p.position.z} after {s} seconds')
       break
    else:
        print(f' {s} s   altitude: {p.position.y}        {p.position.x}, {p.position.z}')
