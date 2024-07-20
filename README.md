# Practical Tasks for a Vacancy at Mindbox

## Overview
This repository contains solutions for two practical tasks required for the application process at Mindbox. The tasks demonstrate development experience and the ability to handle data manipulation using PySpark.

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

triangle = Triangle(a=3, b=4, c=5)
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
from pyspark.sql import SparkSession
from product_category_pairs import get_product_category_pairs, get_products_without_categories

spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

products_df = spark.read.csv("products.csv", header=True, inferSchema=True)
categories_df = spark.read.csv("categories.csv", header=True, inferSchema=True)

product_category_pairs_df = get_product_category_pairs(products_df, categories_df)
product_category_pairs_df.show()

products_without_categories_df = get_products_without_categories(products_df, categories_df)
products_without_categories_df.show()


