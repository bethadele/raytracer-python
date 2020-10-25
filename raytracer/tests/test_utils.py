import pytest
from pydantic import BaseModel
import math

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

class TestUtils:
    def test_point(self):
        p = Point(4.3, -4.2, 3.1)
        assert p.x == 4.3
        assert p.y == -4.2
        assert p.z == 3.1
        assert p.w == 1.0

    def test_vector(self):
        v = Vector(4.3, -4.2, 3.1)
        assert v.x == 4.3
        assert v.y == -4.2
        assert v.z == 3.1
        assert v.w == 0.0

    def test_tracer_tuple(self):
        t = TracerTuple(4.3, -4.2, 3.1, 1.0)
        assert t.x == 4.3
        assert t.y == -4.2
        assert t.z == 3.1
        assert t.w == 1.0

    def test_tracer_tuple_equals(self):
        t = TracerTuple(4.3, -4.2, 3.1, 1.0)
        o = TracerTuple(4.3, -4.2, 3.1, 0.0)
        assert t.equals(t) == True
        assert t.equals(o) == False

    def test_tracer_tuple_plus(self):
        p = Point(3.0, -2.0, 5.0)
        v = Vector(-2.0, 3.0, 1.0)
        result = p.plus(v)
        assert result.x == pytest.approx(1.0)
        assert result.y == pytest.approx(1.0)
        assert result.z == pytest.approx(6.0)
        assert result.w == pytest.approx(1.0)

    def test_subtracting_points_yields_vector(self):
        p1 = Point(3.0, 2.0, 1.0)
        p2 = Point(5.0, 6.0, 7.0)
        v = Vector(-2.0, -4.0, -6.0)
        result = p1.minus(p2)
        assert result.equals(v)

    def test_subtracting_vector_from_point_yields_point(self):
        p = Point(3.0, 2.0, 1.0)
        v = Vector(5.0, 6.0, 7.0)
        p2 = Point(-2.0, -4.0, -6.0)
        result = p.minus(v)
        assert result.equals(p2)

    def test_subtracting_two_vectors_yields_point(self):
        v1 = Vector(3.0, 2.0, 1.0)
        v2 = Vector(5.0, 6.0, 7.0)
        v3  = Vector(-2.0, -4.0, -6.0)
        result = v1.minus(v2)
        assert result.equals(v3)

    def test_subtracting_vector_from_zero_vector_reverses_it(self):
        z = Vector(0, 0, 0)
        v = Vector(1, -2, 3)
        result = z.minus(v)

        assert result.equals(Vector(-1, 2, -3))

    def test_negating_a_vector(self):
        a = TracerTuple(1, -2, 3, -4)
        c = TracerTuple(-1, 2, -3, 4)
        
        assert a.negate().equals(c)

    def test_multiplying_a_tuple_by_a_scalar(self):
        a = TracerTuple(1, -2, 3, -4)

        assert a.times(3.5).equals(TracerTuple(3.5, -7, 10.5, -14))

    def test_multiplying_a_tuple_by_a_fraction(self):
        a = TracerTuple(1, -2, 3, -4)

        assert a.times(0.5).equals(TracerTuple(0.5, -1, 1.5, -2))

    def test_dividing_a_tuple_by_a_scalar(self):
        a = TracerTuple(1, -2, 3, -4)

        assert a.over(2).equals(TracerTuple(0.5, -1, 1.5, -2))

    def test_computing_the_magnitude_of_vector_1_0_0(self):
        v = Vector(1, 0, 0)

        assert v.magnitude() == 1.0

    def test_computing_the_magnitude_of_vector_0_1_0(self):
        v = Vector(0, 1, 0)

        assert v.magnitude() == 1.0

    def test_computing_the_magnitude_of_vector_0_0_1(self):
        v = Vector(0, 0, 1)

        assert v.magnitude() == 1.0

    def test_computing_the_magnitude_of_vector_1_2_3(self):
        v = Vector(1, 2, 3)

        assert v.magnitude() == math.sqrt(14)

    def test_computing_the_magnitude_of_vector_m1_m2_m3(self):
        v = Vector(-1, -2, -3)

        assert v.magnitude() == math.sqrt(14)

    def test_normalizing_vector_4_0_0(self):
        v = Vector(4, 0, 0)

        assert v.normalize().equals(Vector(1, 0, 0))

    def test_normalizing_vector_1_2_3(self):
        v = Vector(1, 2, 3)

        assert v.normalize().equals(Vector(1/math.sqrt(14), 2/math.sqrt(14), 3/math.sqrt(14)))

    def test_magnitude_of_a_normalized_vector(self):
        v = Vector(1, 2, 3)

        assert v.normalize().magnitude() == 1

    def test_dot_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)

        assert a.dot(b) == 20

    def test_cross_product(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)

        assert a.cross(b).equals(Vector(-1, 2, -1))
        assert b.cross(a).equals(Vector(1, -2, 1))
