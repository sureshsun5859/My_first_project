import argparse

from pyspark.sql import SparkSession


def main():
    parser = argparse.ArgumentParser(description="Read a CSV file with PySpark")
    parser.add_argument(
        "csv_path",
        nargs="?",
        default="python/sample_data.csv",
        help="Path to the CSV file to read",
    )
    args = parser.parse_args()

    spark = SparkSession.builder \
        .appName("ReadCSVExample") \
        .master("local[*]") \
        .getOrCreate()

    df = spark.read.option("header", "true").option("inferSchema", "true").csv(args.csv_path)

    print("CSV schema:")
    df.printSchema()

    print("\nCSV data:")
    df.show()

    print(f"\nTotal rows: {df.count()}")

    spark.stop()


if __name__ == "__main__":
    main()
