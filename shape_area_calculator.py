# shape_area_calculator

import math

class ShapeAreaCalculator:
    @staticmethod
    def circle_area(radius):
        """Calculate the area of a circle given its radius."""
        return math.pi * radius**2
    
    @staticmethod
    def triangle_area(side1, side2, side3):
        """
        Calculate the area of a triangle given its three sides using Heron's formula.
        
        Parameters:
        side1 (float): Length of the first side of the triangle.
        side2 (float): Length of the second side of the triangle.
        side3 (float): Length of the third side of the triangle.
        
        Returns:
        float: Area of the triangle.
        """
        # Calculate semi-perimeter
        s = (side1 + side2 + side3) / 2
        # Calculate area using Heron's formula
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area
    
    @staticmethod
    def is_right_triangle(side1, side2, side3):
        """
        Check if a triangle is a right triangle.
        
        Parameters:
        side1 (float): Length of the first side of the triangle.
        side2 (float): Length of the second side of the triangle.
        side3 (float): Length of the third side of the triangle.
        
        Returns:
        bool: True if the triangle is a right triangle, False otherwise.
        """
        # Sort sides in ascending order
        sides = [side1, side2, side3]
        sides.sort()
        # Check if it satisfies Pythagorean theorem
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# Unit tests
if __name__ == "__main__":
    def test_circle_area():
        """Unit test for circle_area function."""
        assert math.isclose(ShapeAreaCalculator.circle_area(3), 28.274, rel_tol=1e-3)
    
    def test_triangle_area():
        """Unit test for triangle_area function."""
        assert math.isclose(ShapeAreaCalculator.triangle_area(3, 4, 5), 6.0, rel_tol=1e-3)
    
    def test_is_right_triangle():
        """Unit test for is_right_triangle function."""
        assert ShapeAreaCalculator.is_right_triangle(3, 4, 5) == True
        assert ShapeAreaCalculator.is_right_triangle(5, 12, 13) == True
        assert ShapeAreaCalculator.is_right_triangle(6, 8, 10) == True
        assert ShapeAreaCalculator.is_right_triangle(7, 8, 9) == False
    
    # Run tests
    test_circle_area()
    test_triangle_area()
    test_is_right_triangle()
    print("All tests passed.")
