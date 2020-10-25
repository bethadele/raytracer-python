import math
import pydantic

#TODO:
# - convert plus, minus, negate to overloaded operators
# - figure out proper implementation of pydantic & test

class TracerTuple():
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def equals(self, other):
        return (math.isclose(self.w, other.w)) and \
               (math.isclose(self.x, other.x)) and \
               (math.isclose(self.y, other.y)) and \
               (math.isclose(self.z, other.z))

    def plus(self, other):
        return TracerTuple( \
                self.x + other.x, \
                self.y + other.y, \
                self.z + other.z, \
                self.w + other.w
                )

    def minus(self, other):
        return TracerTuple( \
                self.x - other.x, \
                self.y - other.y, \
                self.z - other.z, \
                self.w - other.w
                )

    def negate(self):
        return TracerTuple( \
                0.0 - self.x, \
                0.0 - self.y, \
                0.0 - self.z, \
                0.0 - self.w \
                )

    # scalar multiplication
    def times(self, scalar: float):
        return TracerTuple( \
                self.x * scalar, \
                self.y * scalar, \
                self.z * scalar, \
                self.w * scalar \
                )

    # scalar division
    def over(self, scalar: float):
        return TracerTuple( \
                self.x / scalar, \
                self.y / scalar, \
                self.z / scalar, \
                self.w / scalar \
                )

    def magnitude(self):
        return math.sqrt( \
                math.pow(self.x, 2) + \
                math.pow(self.y, 2) + \
                math.pow(self.z, 2) + \
                math.pow(self.w, 2) \
                )

    def normalize(self):
        return TracerTuple( \
            self.x / self.magnitude(), \
            self.y / self.magnitude(), \
            self.z / self.magnitude(), \
            self.w / self.magnitude() \
            )

    def dot(self, other):
        return self.x * other.x + \
                self.y * other.y + \
                self.z * other.z + \
                self.w * other.w

class Point(TracerTuple):
    def __init__(self, x: float, y: float, z: float):
        TracerTuple.__init__(self, x, y, z, 1.0)

class Vector(TracerTuple):
    def __init__(self, x: float, y: float, z: float):
        TracerTuple.__init__(self, x, y, z, 0.0)

    def cross(self, other):
        return Vector( \
                self.y * other.z - self.z * other.y, \
                self.z * other.x - self.x * other.z, \
                self.x * other.y - self.y * other.x \
                )
