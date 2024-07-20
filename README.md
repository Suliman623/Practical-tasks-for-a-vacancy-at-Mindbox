# Practical Tasks for a Vacancy at Mindbox

## Overview
This repository contains solutions for two practical tasks required for the application process at Mindbox. The tasks demonstrate creating a library in Python to calculate the area of various shapes and the ability to handle data manipulation using PySpark.

## Task 1: Shape Area Calculator

### Description
This task involves creating a library in Python to calculate the area of various shapes, including:
- Calculating the area of a circle by its radius.
- Calculating the area of a triangle by its three sides.
- Checking if a triangle is a right triangle.
- Allowing easy addition of other shapes.
- Calculating the area of a shape dynamically at runtime.

### Files
- `shape_area_calculator.py`: Contains the main logic for area calculations.
- `test_shape_area_calculator.py`: Contains unit tests for the functions.

### Usage
To use the shape area calculator:
```python
from shape_area_calculator import Circle, Triangle

circle = Circle(radius=5)
print("Circle Area:", circle.area())

triangle = Triangle(side1=3, side2=4, side3=5)
print("Triangle Area:", triangle.area())
print("Is Right Triangle:", triangle.is_right_triangle())
```

## Task 2: Product-Category Pair in PySpark

### Description
This task involves creating a PySpark application to handle product and category data. The application:
- Returns all Product Name – Category Name pairs in a single DataFrame.
- Identifies products without any categories.

### Files
- `product_category_pairs.py`: Contains the PySpark logic to process the CSV files and perform the required operations.
- `products.csv`: Contains product data.
- `categories.csv`: Contains category data.

### Usage
To run the PySpark application:
```python
from product_category_pairs import get_product_category_pairs

# Example usage
product_category_pairs, products_with_no_categories = get_product_category_pairs('products.csv', 'categories.csv')
product_category_pairs.show()
products_with_no_categories.show()
