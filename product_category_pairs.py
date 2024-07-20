from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs(products_csv, categories_csv):
    # Initialize Spark session
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()
    
    # Read CSV files into DataFrames
    products_df = spark.read.csv(products_csv, header=True, inferSchema=True)
    categories_df = spark.read.csv(categories_csv, header=True, inferSchema=True)
    
    # Perform left outer join to get all product-category pairs and products with no categories
    product_category_df = products_df.join(categories_df, "product_id", "left_outer")
    
    # Select relevant columns
    product_category_pairs = product_category_df.select("product_name", "category_name")
    
    # Filter products with no categories
    products_with_no_categories = product_category_df.filter(col("category_name").isNull()).select("product_name")
    
    return product_category_pairs, products_with_no_categories

# Example usage
if __name__ == "__main__":
    product_category_pairs, products_with_no_categories = get_product_category_pairs('products.csv', 'categories.csv')
    product_category_pairs.show()
    products_with_no_categories.show()
