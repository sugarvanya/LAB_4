import unittest
from math import pi
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_string_radius(self):
        result = area("s")
        self.assertEqual(result, "error: r must be int")

    def test_perimeter_string_radius(self):
        result = perimeter("s")
        self.assertEqual(result, "error: r must be int")
        
    def test_area_negative_radius(self):
        result = area(-3)
        self.assertEqual(result, "error: circle's area can't be negative")

    def test_peimeter_negative_radius(self):
        result = perimeter(-3)
        self.assertEqual(result, "error: circle's perimeter can't be negative")

    def test_area_zero_radius(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_perimeter_zero_radius(self):
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_area_positive_radius(self):
        result = area(5)
        self.assertEqual(result, 25 * pi)

    def test_perimeter_poisitive_radius(self):
        result = perimeter(5)
        self.assertEqual(result, 10 * pi)
