import unittest
from shape_area_calculator import Circle, Triangle, calculate_area

class TestShapeAreaCalculator(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.5398, places=4)
    
    def test_circle_area_zero(self):
        circle = Circle(0)
        self.assertAlmostEqual(calculate_area(circle), 0, places=4)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            Circle(-5)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6)
    
    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())
    
    def test_non_right_triangle(self):
        triangle = Triangle(3, 3, 3)
        self.assertFalse(triangle.is_right_triangle())

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

if __name__ == '__main__':
    unittest.main()
    
