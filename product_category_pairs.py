# product_category_pairs

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ProductCategoryPairs") \
    .getOrCreate()

# Step 1: Read CSV files into Spark DataFrames
products_df = spark.read.csv("products.csv", header=True, inferSchema=True)
categories_df = spark.read.csv("categories.csv", header=True, inferSchema=True)

# Step 2: Join products_df and categories_df to get Product Name - Category Name pairs
joined_df = products_df.join(categories_df, products_df.ProductID == categories_df.ProductID, "left")

# Step 3: Select Product Name and Category Name columns
result_df = joined_df.select(products_df.ProductName, categories_df.CategoryName.alias("CategoryName"))

# Step 4: Identify products with no categories
products_with_no_categories_df = products_df.join(categories_df, products_df.ProductID == categories_df.ProductID, "left_anti") \
    .select(products_df.ProductName)

# Step 5: Union results to include products with no categories
final_result_df = result_df.union(products_with_no_categories_df.select("ProductName", col("CategoryName").cast("string")))

# Show the final result
final_result_df.show(truncate=False)

# Stop the SparkSession
spark.stop()
