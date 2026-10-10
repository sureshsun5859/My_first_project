"""Join and merge DataFrames using pandas."""

import pandas as pd


def main():
    customers = pd.DataFrame(
        {
            "customer_id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "city": ["New York", "London", "Paris"],
        }
    )

    orders = pd.DataFrame(
        {
            "customer_id": [1, 1, 2, 3],
            "order_id": [101, 102, 103, 104],
            "amount": [100.0, 50.0, 200.0, 75.0],
        }
    )

    # Keep every customer and show missing order information as NaN.
    merged = customers.merge(orders, on="customer_id", how="left")
    print("Left merge:")
    print(merged)

    # Keep only orders that have matching customers.
    inner_merge = customers.merge(orders, on="customer_id", how="inner")
    print("\nInner merge:")
    print(inner_merge)

    # Use a separate key for the two tables.
    customers_with_key = customers.rename(
        columns={"customer_id": "id"}
    )
    print("\nMerge using different column names:")
    print(customers_with_key.merge(orders, left_on="id", right_on="customer_id"))


if __name__ == "__main__":
    main()
