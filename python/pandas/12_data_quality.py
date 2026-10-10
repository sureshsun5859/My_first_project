"""Build basic data-quality checks for a pandas DataFrame."""

import pandas as pd


def main():
    data = {
        "customer_id": [1, 2, 2, 4, None],
        "age": [25, 30, 30, -5, 35],
        "email": [
            "alice@example.com",
            "bob@example.com",
            "bob@example.com",
            "david@example.com",
            "unknown",
        ],
        "status": ["active", "active", "inactive", "active", "active"],
    }
    df = pd.DataFrame(data)

    print("Original data:")
    print(df)

    # Count missing values.
    print("\nMissing values:")
    print(df.isna().sum())

    # Find duplicate rows.
    print("\nDuplicate rows:")
    print(df[df.duplicated(keep=False)])

    # Validate and clean simple business rules.
    invalid_age = df["age"] < 0
    invalid_email = ~df["email"].str.contains("@", na=False)
    invalid_customer = df["customer_id"].isna()

    print("\nInvalid rows:")
    print(df[invalid_age | invalid_email | invalid_customer])

    # Remove duplicate customer records and invalid rows.
    cleaned = (
        df.drop_duplicates(subset=["customer_id"], keep="first")
        .loc[lambda frame: frame["age"] >= 0]
        .loc[lambda frame: frame["email"].str.contains("@", na=False)]
    )
    print("\nCleaned data:")
    print(cleaned)


if __name__ == "__main__":
    main()
