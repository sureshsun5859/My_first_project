"""Apply transformations and calculate statistics with pandas."""

import pandas as pd


def main():
    data = {
        "product": ["A", "A", "B", "B", "C"],
        "price": [10.0, 20.0, 15.0, 25.0, 30.0],
        "quantity": [2, 3, 4, 1, 5],
    }
    df = pd.DataFrame(data)

    # Calculate a new column from existing columns.
    df["total_value"] = df["price"] * df["quantity"]
    print("Calculated values:")
    print(df)

    # Group and aggregate by product.
    grouped = df.groupby("product").agg(
        total_value=("total_value", "sum"),
        average_price=("price", "mean"),
        total_quantity=("quantity", "sum"),
    )
    print("\nGrouped statistics:")
    print(grouped)

    # Basic descriptive statistics.
    print("\nStatistics for price:")
    print(df["price"].describe())

    # Calculate a percentage change.
    df["price_change"] = df["price"].pct_change()
    print("\nPercentage change:")
    print(df[["product", "price", "price_change"]])


if __name__ == "__main__":
    main()
