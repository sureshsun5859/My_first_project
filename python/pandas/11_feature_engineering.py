"""Create useful features from raw data for analysis and machine learning."""

import pandas as pd


def main():
    data = {
        "customer_id": [1, 1, 2, 2, 3],
        "purchase_date": [
            "2026-01-01",
            "2026-01-15",
            "2026-01-03",
            "2026-02-01",
            "2026-02-10",
        ],
        "amount": [50.0, 100.0, 80.0, 120.0, 200.0],
        "product_category": ["Book", "Electronics", "Book", "Home", "Electronics"],
    }
    df = pd.DataFrame(data)

    # Convert dates and calculate time-based features.
    df["purchase_date"] = pd.to_datetime(df["purchase_date"])
    df["day_of_month"] = df["purchase_date"].dt.day
    df["month"] = df["purchase_date"].dt.month
    df["is_weekend"] = df["purchase_date"].dt.dayofweek.isin([5, 6]).astype(int)

    # Aggregate customer-level values.
    customer_features = (
        df.groupby("customer_id")
        .agg(
            total_spend=("amount", "sum"),
            average_order=("amount", "mean"),
            purchase_count=("amount", "size"),
            last_purchase=("purchase_date", "max"),
        )
        .reset_index()
    )

    print("Customer-level features:")
    print(customer_features)

    # Create categorical data that can be encoded for a model.
    df["category_code"] = pd.Categorical(df["product_category"]).codes
    print("\nEncoded category codes:")
    print(df[["product_category", "category_code"]])


if __name__ == "__main__":
    main()
